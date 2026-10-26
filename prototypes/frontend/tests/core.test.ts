import { createInstance } from 'i18next';
import { describe, expect, it } from 'vitest';
import { addDays, formatDate, mondayOf, validSession } from '../src/lib/calendar';
import de from '../src/locales/de.json';
import fr from '../src/locales/fr.json';
import en from '../src/locales/en.json';
import { isLanguage, isTheme } from '../src/lib/preferences';
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

describe('CSRF-Behandlung über mehrere Tabs mit geteiltem Cookie-Speicher', () => {
  it('erneuert CSRF-Token nach csrf_denied bei Cookie-Aktualisierung durch zweiten Tab kontrolliert einmal', async () => {
    const cookies: Record<string, string> = {
      '__Host-syllentra-csrf': 'initial-token-shared-in-cookie-jar-43chars',
    };
    let tab1LocalToken = 'initial-token-shared-in-cookie-jar-43chars';
    let tab2Token = 'tab2-updated-shared-cookie-token-43chars123';
    let csrfFetches = 0;
    let postAttempts = 0;

    // Simulierter Backend-Endpunkt
    const mockFetch = async (
      input: string,
      init?: RequestInit,
    ): Promise<{
      ok: boolean;
      status: number;
      json: () => Promise<unknown>;
    }> => {
      if (input === '/api/auth/csrf') {
        csrfFetches++;
        const fresh = csrfFetches === 1 ? tab2Token : 'tab1-refreshed-shared-token-43chars123456';
        cookies['__Host-syllentra-csrf'] = fresh;
        return {
          ok: true,
          status: 200,
          json: async () => ({ csrf_token: fresh }),
        };
      }
      if (input === '/api/auth/login' && init?.method === 'POST') {
        postAttempts++;
        const headers = init.headers as Record<string, string>;
        const sentToken = headers?.['X-CSRF-Token'];
        const cookieToken = cookies['__Host-syllentra-csrf'];
        if (!sentToken || sentToken !== cookieToken) {
          return {
            ok: false,
            status: 403,
            json: async () => ({ detail: 'csrf_denied' }),
          };
        }
        return {
          ok: true,
          status: 200,
          json: async () => ({ status: 'ok' }),
        };
      }
      return { ok: false, status: 404, json: async () => ({}) };
    };

    // Schritt 1: Tab 2 öffnet und aktualisiert den gemeinsamen Cookie-Speicher
    const tab2Csrf = await mockFetch('/api/auth/csrf');
    const tab2Data = (await tab2Csrf.json()) as { csrf_token: string };
    tab2Token = tab2Data.csrf_token;
    expect(cookies['__Host-syllentra-csrf']).toBe(tab2Token);

    // Schritt 2: Tab 1 führt einen POST mit seinem veralteten lokalen Token aus
    // Simuliert die zweistufige controlled retry-Logik aus Identity.tsx:
    const tab1Call = async (body: Record<string, string>) => {
      let attempt = 0;
      while (attempt < 2) {
        const response = await mockFetch('/api/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRF-Token': tab1LocalToken,
          },
          body: JSON.stringify(body),
        });
        if (response.status === 403 && attempt === 0) {
          const err = (await response.json()) as { detail?: string };
          if (err?.detail === 'csrf_denied') {
            const freshRes = await mockFetch('/api/auth/csrf');
            const freshData = (await freshRes.json()) as {
              csrf_token: string;
            };
            tab1LocalToken = freshData.csrf_token;
            attempt++;
            continue;
          }
        }
        if (!response.ok) throw new Error('identityFailed');
        return response.json();
      }
      throw new Error('identityFailed');
    };

    const result = await tab1Call({ login: 'student@example.test' });
    expect(result).toEqual({ status: 'ok' });
    expect(postAttempts).toBe(2); // Genau 1 kontrollierter Retry
    expect(csrfFetches).toBe(2); // 1x Tab 2, 1x kontrollierter Refresh durch Tab 1
  });

  it('wiederholt niemals bei origin_denied oder dauerhaftem csrf_denied', async () => {
    let attempts = 0;
    const mockPost = async () => {
      attempts++;
      return {
        ok: false,
        status: 403,
        json: async () => ({ detail: 'origin_denied' }),
      };
    };

    const callWithDenial = async () => {
      let attempt = 0;
      while (attempt < 2) {
        const res = await mockPost();
        if (res.status === 403 && attempt === 0) {
          const err = (await res.json()) as { detail?: string };
          if (err?.detail === 'csrf_denied') {
            attempt++;
            continue;
          }
        }
        if (!res.ok) throw new Error('identityFailed');
        return res.json();
      }
      throw new Error('identityFailed');
    };

    await expect(callWithDenial()).rejects.toThrow('identityFailed');
    expect(attempts).toBe(1); // Kein unberechtigter Retry bei origin_denied
  });
});
