import { modules } from '../data/demo';
import type { Language } from './preferences';
export function dateValue(value: string): Date {
  return new Date(`${value}T12:00:00Z`);
}
export function addDays(value: string, amount: number): string {
  const day = dateValue(value);
  day.setUTCDate(day.getUTCDate() + amount);
  return day.toISOString().slice(0, 10);
}
export function mondayOf(value: string): string {
  const day = dateValue(value).getUTCDay();
  return addDays(value, -(day === 0 ? 6 : day - 1));
}
export function formatDate(
  value: string,
  language: Language,
  options: Intl.DateTimeFormatOptions = { day: 'numeric', month: 'long' },
): string {
  return new Intl.DateTimeFormat(language, { ...options, timeZone: 'UTC' }).format(
    dateValue(value),
  );
}
export function validSession(title: string, module: string, date: string, time: string): boolean {
  return (
    title.trim().length > 0 &&
    title.trim().length <= 80 &&
    modules.some((item) => item.id === module) &&
    /^\d{4}-\d{2}-\d{2}$/.test(date) &&
    date >= '2020-01-01' &&
    date <= '2099-12-31' &&
    !Number.isNaN(dateValue(date).valueOf()) &&
    dateValue(date).toISOString().slice(0, 10) === date &&
    /^([01]\d|2[0-3]):[0-5]\d$/.test(time)
  );
}
