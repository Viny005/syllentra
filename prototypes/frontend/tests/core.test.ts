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
