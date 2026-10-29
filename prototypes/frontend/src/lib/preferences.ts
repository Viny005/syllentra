export type Language = 'de' | 'fr' | 'en';
export type Theme = 'light' | 'dark' | 'system';
export const isLanguage = (value: unknown): value is Language =>
  ['de', 'fr', 'en'].includes(String(value));
export const isTheme = (value: unknown): value is Theme =>
  ['light', 'dark', 'system'].includes(String(value));
export function readPreference(key: string): string | null {
  try {
    return localStorage.getItem(`syllentra-demo:${key}`);
  } catch {
    return null;
  }
}
export function writePreference(key: string, value: string): boolean {
  try {
    localStorage.setItem(`syllentra-demo:${key}`, value);
    return true;
  } catch {
    return false;
  }
}
