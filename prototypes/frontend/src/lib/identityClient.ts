export const localEnabled = () =>
  typeof location !== 'undefined' &&
  location.protocol === 'https:' &&
  location.hostname === '127.0.0.1' &&
  location.port === '5174';

export const object = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);

export interface IdentityClientOptions {
  isLocalEnabled?: () => boolean;
  onUnauthorized?: (path: string) => void;
  fetchFn?: typeof fetch;
}

export function createIdentityClient(options: IdentityClientOptions = {}) {
  const isLocalEnabled = options.isLocalEnabled ?? localEnabled;
  const fetchFn = options.fetchFn ?? ((...args: Parameters<typeof fetch>) => fetch(...args));
  const onUnauthorized = options.onUnauthorized ?? (() => {});
  let csrfToken = '';

  async function refreshCsrf(): Promise<string> {
    const response = await fetchFn('/api/auth/csrf', {
      credentials: 'same-origin',
      cache: 'no-store',
      signal: AbortSignal.timeout(8000),
    });
    const data: unknown = await response.json().catch(() => null);
    if (
      !response.ok ||
      !object(data) ||
      typeof data.csrf_token !== 'string' ||
      data.csrf_token.length !== 43
    ) {
      throw new Error('identityUnavailable');
    }
    csrfToken = data.csrf_token;
    return data.csrf_token;
  }

  async function call(
    path: string,
    body?: Record<string, string>,
  ): Promise<Record<string, unknown> | unknown[]> {
    if (!isLocalEnabled()) throw new Error('identityUnavailable');
    if (body && !csrfToken) {
      await refreshCsrf();
    }
    let attempt = 0;
    while (attempt < 2) {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 8000);
      try {
        const response = await fetchFn(`/api${path}`, {
          method: body ? 'POST' : 'GET',
          credentials: 'same-origin',
          cache: 'no-store',
          signal: controller.signal,
          headers: body ? { 'Content-Type': 'application/json', 'X-CSRF-Token': csrfToken } : {},
          body: body ? JSON.stringify(body) : undefined,
        });
        if (response.status === 403 && body && attempt === 0) {
          // Kontrollierte Wiederherstellung bei eindeutigem csrf_denied
          const errData: unknown = await response.json().catch(() => null);
          if (object(errData) && errData.detail === 'csrf_denied') {
            csrfToken = '';
            await refreshCsrf();
            attempt++;
            continue;
          }
        }
        if (response.status === 401) {
          onUnauthorized(path);
          throw new Error(path === '/auth/login' ? 'identityFailed' : 'identityDisconnected');
        }
        if (!response.ok) {
          throw new Error(response.status === 429 ? 'identityLimited' : 'identityFailed');
        }
        if (response.status === 204) return {};
        const data: unknown = await response.json();
        if (!object(data) && !Array.isArray(data)) throw new Error('identityFailed');
        return data;
      } finally {
        clearTimeout(timer);
      }
    }
    throw new Error('identityFailed');
  }

  return {
    call,
    refreshCsrf,
    getCsrf: () => csrfToken,
    setCsrf: (token: string) => {
      csrfToken = token;
    },
  };
}
