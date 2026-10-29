import { createInstance } from 'i18next';
import { describe, expect, it } from 'vitest';
import { addDays, formatDate, mondayOf, validSession } from '../src/lib/calendar';
import de from '../src/locales/de.json';
import fr from '../src/locales/fr.json';
import en from '../src/locales/en.json';
import { isLanguage, isTheme } from '../src/lib/preferences';
import { createIdentityClient } from '../src/lib/identityClient';
describe('Kalendergrenzen ohne unbeabsichtigte Zeitzonenverschiebung', () => {
  it('wechselt Wochen über Monats-, Jahres- und Sommerzeitgrenzen', () => {
    expect(addDays('2026-10-19', 7)).toBe('2026-10-26');
    expect(addDays('2026-12-28', 7)).toBe('2027-01-04');
    expect(addDays('2026-03-30', -7)).toBe('2026-03-23');
    expect(mondayOf('2026-10-25')).toBe('2026-10-19');
  });
  it('weist ungültige Datum-, Zeit-, Modul- und Titeldaten zurück', () => {
    for (const input of [
      ['', 'math', '2026-10-22', '09:00'],
      ['x', 'unknown', '2026-10-22', '09:00'],
      ['x', 'math', '2026-02-30', '09:00'],
      ['x', 'math', '2026-10-22', '25:00'],
      ['x'.repeat(81), 'math', '2026-10-22', '09:00'],
    ])
      expect(validSession(...(input as [string, string, string, string]))).toBe(false);
    expect(validSession('Review', 'math', '2028-02-29', '09:00')).toBe(true);
  });
  it('lokalisiert denselben Kalendertag in drei Sprachen', () => {
    expect(formatDate('2026-10-22', 'de')).toBe('22. Oktober');
    expect(formatDate('2026-10-22', 'fr')).toBe('22 octobre');
    expect(formatDate('2026-10-22', 'en')).toBe('October 22');
  });
});
describe('Übersetzungen und lokale Auswahl', () => {
  it('hat vollständige und nichtleere DE-/FR-/EN-Schlüssel', () => {
    for (const resource of [fr, en]) {
      expect(Object.keys(resource).sort()).toEqual(Object.keys(de).sort());
      expect(Object.values(resource).every((value) => value.trim().length > 0)).toBe(true);
    }
  });
  it('erhält die Interpolationsvariablen in allen Sprachen', () => {
    for (const key of Object.keys(de) as (keyof typeof de)[]) {
      const variables = (s: string) => (s.match(/{{\w+}}/g) || []).sort();
      expect(variables(fr[key])).toEqual(variables(de[key]));
      expect(variables(en[key])).toEqual(variables(de[key]));
    }
  });
  it('akzeptiert nur bekannte Präferenzen aus dem Browserspeicher', () => {
    expect(isLanguage('fr')).toBe(true);
    expect(isLanguage('xx')).toBe(false);
    expect(isTheme('system')).toBe(true);
    expect(isTheme('<script>')).toBe(false);
  });
});

it('übersetzt einzelne und mehrere Suchtreffer grammatisch korrekt', async () => {
  const instance = createInstance();
  await instance.init({
    lng: 'de',
    resources: { de: { translation: de }, fr: { translation: fr }, en: { translation: en } },
  });
  expect(instance.t('results', { count: 1 })).toBe('1 Ergebnis');
  expect(instance.t('results', { count: 2 })).toBe('2 Ergebnisse');
  await instance.changeLanguage('fr');
  expect(instance.t('results', { count: 1 })).toBe('1 résultat');
  await instance.changeLanguage('en');
  expect(instance.t('results', { count: 1 })).toBe('1 result');
});

describe('CSRF-Behandlung über mehrere Tabs mit geteiltem Cookie-Speicher (echter Client)', () => {
  const tokenInitial = 'a'.repeat(43);
  const tokenTab2 = 'b'.repeat(43);
  const tokenRefreshed = 'c'.repeat(43);

  it('erneuert CSRF-Token nach csrf_denied bei Cookie-Aktualisierung durch zweiten Tab kontrolliert einmal', async () => {
    const cookies: Record<string, string> = {
      '__Host-syllentra-csrf': tokenInitial,
    };
    let csrfFetches = 0;
    let postAttempts = 0;

    const mockFetch = (async (
      input: string | URL | Request,
      init?: RequestInit,
    ): Promise<Response> => {
      const url = String(input);
      if (url === '/api/auth/csrf') {
        csrfFetches++;
        const fresh = csrfFetches === 1 ? tokenTab2 : tokenRefreshed;
        cookies['__Host-syllentra-csrf'] = fresh;
        return new Response(JSON.stringify({ csrf_token: fresh }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' },
        });
      }
      if (url === '/api/auth/login' && init?.method === 'POST') {
        postAttempts++;
        const headers = init.headers as Record<string, string>;
        const sentToken = headers?.['X-CSRF-Token'];
        const cookieToken = cookies['__Host-syllentra-csrf'];
        if (!sentToken || sentToken !== cookieToken) {
          return new Response(JSON.stringify({ detail: 'csrf_denied' }), {
            status: 403,
            headers: { 'Content-Type': 'application/json' },
          });
        }
        return new Response(JSON.stringify({ status: 'ok' }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' },
        });
      }
      return new Response(JSON.stringify({}), { status: 404 });
    }) as typeof fetch;

    // Tab 1 wird initialisiert und hält tokenInitial
    const client = createIdentityClient({ isLocalEnabled: () => true, fetchFn: mockFetch });
    client.setCsrf(tokenInitial);

    // Tab 2 öffnet und aktualisiert den gemeinsamen Cookie-Speicher auf tokenTab2
    await mockFetch('/api/auth/csrf');
    expect(cookies['__Host-syllentra-csrf']).toBe(tokenTab2);

    // Tab 1 führt die mutierende Anfrage über die echte Produktionsfunktion aus
    const result = await client.call('/auth/login', { login: 'student@example.test' });
    expect(result).toEqual({ status: 'ok' });
    expect(postAttempts).toBe(2); // Genau 1 kontrollierter Retry
    expect(csrfFetches).toBe(2); // 1x Tab 2, 1x Tab 1 Refresh
    expect(client.getCsrf()).toBe(tokenRefreshed);
  });

  it('stoppt nach genau 2 Versuchen bei persistentem csrf_denied', async () => {
    let postAttempts = 0;
    const mockFetch = (async (input: string | URL | Request): Promise<Response> => {
      const url = String(input);
      if (url === '/api/auth/csrf') {
        return new Response(JSON.stringify({ csrf_token: tokenRefreshed }), { status: 200 });
      }
      if (url === '/api/auth/login') {
        postAttempts++;
        return new Response(JSON.stringify({ detail: 'csrf_denied' }), { status: 403 });
      }
      return new Response(JSON.stringify({}), { status: 404 });
    }) as typeof fetch;

    const client = createIdentityClient({ isLocalEnabled: () => true, fetchFn: mockFetch });
    client.setCsrf(tokenInitial);

    await expect(client.call('/auth/login', { login: 'student@example.test' })).rejects.toThrow(
      'identityFailed',
    );
    expect(postAttempts).toBe(2); // Die zweite Abweisung ist definitiv die letzte
  });

  it('wiederholt niemals bei origin_denied', async () => {
    let postAttempts = 0;
    const mockFetch = (async (): Promise<Response> => {
      postAttempts++;
      return new Response(JSON.stringify({ detail: 'origin_denied' }), { status: 403 });
    }) as typeof fetch;

    const client = createIdentityClient({ isLocalEnabled: () => true, fetchFn: mockFetch });
    client.setCsrf(tokenInitial);

    await expect(client.call('/auth/login', { login: 'student@example.test' })).rejects.toThrow(
      'identityFailed',
    );
    expect(postAttempts).toBe(1); // Kein Wiederholungsversuch
  });

  it('wiederholt niemals bei Netzwerkfehlern oder Serverfehlern', async () => {
    let attempts = 0;
    const failingFetch = (async (): Promise<Response> => {
      attempts++;
      throw new TypeError('Failed to fetch');
    }) as typeof fetch;

    const client1 = createIdentityClient({ isLocalEnabled: () => true, fetchFn: failingFetch });
    client1.setCsrf(tokenInitial);
    await expect(client1.call('/auth/login', { login: 'a@example.test' })).rejects.toThrow(
      'Failed to fetch',
    );
    expect(attempts).toBe(1);

    let serverAttempts = 0;
    const serverErrorFetch = (async (): Promise<Response> => {
      serverAttempts++;
      return new Response(JSON.stringify({ detail: 'internal' }), { status: 500 });
    }) as typeof fetch;

    const client2 = createIdentityClient({ isLocalEnabled: () => true, fetchFn: serverErrorFetch });
    client2.setCsrf(tokenInitial);
    await expect(client2.call('/auth/login', { login: 'a@example.test' })).rejects.toThrow(
      'identityFailed',
    );
    expect(serverAttempts).toBe(1);
  });

  it('lehnt ungültige erneuerte Token ab und bricht ohne unberechtigten Retry ab', async () => {
    let postAttempts = 0;
    const mockFetch = (async (input: string | URL | Request): Promise<Response> => {
      const url = String(input);
      if (url === '/api/auth/csrf') {
        // Zu kurzer Token (keine 43 Zeichen)
        return new Response(JSON.stringify({ csrf_token: 'too-short' }), { status: 200 });
      }
      if (url === '/api/auth/login') {
        postAttempts++;
        return new Response(JSON.stringify({ detail: 'csrf_denied' }), { status: 403 });
      }
      return new Response(JSON.stringify({}), { status: 404 });
    }) as typeof fetch;

    const client = createIdentityClient({ isLocalEnabled: () => true, fetchFn: mockFetch });
    client.setCsrf(tokenInitial);

    await expect(client.call('/auth/login', { login: 'a@example.test' })).rejects.toThrow(
      'identityUnavailable',
    );
    expect(postAttempts).toBe(1); // Kein Retry mit ungültigem Token
  });

  it('verweigert Aufrufe außerhalb der erlaubten lokalen Umgebung', async () => {
    let fetchCalled = false;
    const mockFetch = (async (): Promise<Response> => {
      fetchCalled = true;
      return new Response(JSON.stringify({}), { status: 200 });
    }) as typeof fetch;

    const client = createIdentityClient({ isLocalEnabled: () => false, fetchFn: mockFetch });
    await expect(client.call('/notes')).rejects.toThrow('identityUnavailable');
    expect(fetchCalled).toBe(false);
  });
});
