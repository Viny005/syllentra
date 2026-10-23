import { readFileSync, mkdirSync } from 'node:fs';
import { randomUUID } from 'node:crypto';
import { test, expect } from '@playwright/test';
import type { Page } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
const password = 'synthetic-browser-password';
const newPassword = 'synthetic-renewed-password';
function internalSecret(email: string, purpose: string, offline = false): string {
  const file = new URL(
    offline
      ? '../../../backend/.local/offline/recovery.jsonl'
      : '../../../backend/.local/mail/otp.jsonl',
    import.meta.url,
  );
  const rows = readFileSync(file, 'utf8')
    .trim()
    .split('\n')
    .map((line) => JSON.parse(line) as Record<string, string>);
  const found = rows.reverse().find((row) => row.recipient === email && row.purpose === purpose);
  if (!found) throw new Error('Controlled internal test message missing');
  return found.secret;
}
async function enter(page: Page) {
  await page.goto('/#/identity');
  await expect(page.getByRole('heading', { name: 'Lokaler Identitätsversuch' })).toBeVisible();
}
async function register(page: Page, email: string) {
  await enter(page);
  await page.getByRole('button', { name: 'Registrieren', exact: true }).click();
  await page.getByLabel('Künstliche E-Mail-Adresse').fill(email);
  await page.getByLabel('Passwort', { exact: true }).fill(password);
  await page.getByRole('button', { name: 'Fortfahren', exact: true }).click();
  await expect(page.getByRole('heading', { name: 'E-Mail-Adresse verifizieren' })).toBeVisible();
  const code = internalSecret(email, 'email');
  const field = page.getByLabel('Einmalcode aus dem privaten Testkanal');
  await expect(field).toHaveAttribute('type', 'password');
  await field.fill(code);
  await expect(page.locator('body')).not.toContainText(code);
  await page.getByRole('button', { name: 'Fortfahren', exact: true }).click();
  await expect(page.getByText('Verifikation abgeschlossen.', { exact: false })).toBeVisible();
}
async function login(page: Page, email: string, supplied = password) {
  await page.getByLabel('Künstliche E-Mail-Adresse').fill(email);
  await page.getByLabel('Passwort', { exact: true }).fill(supplied);
  await page.getByRole('button', { name: 'Fortfahren', exact: true }).click();
}
async function connected(page: Page) {
  await expect(page.getByRole('heading', { name: 'Eigene Sitzungen' })).toBeVisible();
}
async function axe(page: Page) {
  const result = await new AxeBuilder({ page }).analyze();
  expect(result.violations).toEqual([]);
}

test('Registrierung, OTP, sichere Sitzung, Demoabgrenzung und Abmeldung', async ({
  page,
  context,
}) => {
  const email = `browser-${randomUUID()}@example.test`;
  await register(page, email);
  await login(page, email);
  await connected(page);
  await axe(page);
  const cookies = await context.cookies();
  const session = cookies.find((c) => c.name === '__Host-syllentra-session');
  expect(session?.secure && session.httpOnly && session.sameSite === 'Strict').toBe(true);
  expect(await page.evaluate(() => document.cookie)).not.toContain('__Host-syllentra-session');
  expect(
    await page.evaluate(() =>
      Object.keys(localStorage).every((key) => key.startsWith('syllentra-demo:')),
    ),
  ).toBe(true);
  await page.getByRole('link', { name: 'Zu den unabhängigen Demo-Lernräumen' }).click();
  await expect(page.getByRole('heading', { name: 'Übersicht' })).toBeVisible();
  await page.goto('/#/identity');
  await connected(page);
  await page.getByRole('button', { name: 'Sitzung 1 widerrufen' }).click();
  await expect(
    page.getByText('Keine verbundene Kontositzung', { exact: true }).first(),
  ).toBeVisible();
  await login(page, email);
  await connected(page);
  await page.getByRole('button', { name: 'Abmelden', exact: true }).click();
  await expect(
    page.getByText('Keine verbundene Kontositzung', { exact: true }).first(),
  ).toBeVisible();
  expect((await context.cookies()).some((c) => c.name === '__Host-syllentra-session')).toBe(false);
});

test('Neues Browsergerät erst nach Bestätigung im autorisierten Browser', async ({
  page,
  browser,
}) => {
  const email = `device-${randomUUID()}@example.test`;
  await register(page, email);
  await login(page, email);
  await connected(page);
  const secondContext = await browser.newContext({ ignoreHTTPSErrors: true });
  const second = await secondContext.newPage();
  await second.goto('https://127.0.0.1:5174/#/identity');
  await login(second, email);
  await expect(second.getByRole('heading', { name: 'Neues Gerät verifizieren' })).toBeVisible();
  expect((await secondContext.cookies()).some((c) => c.name === '__Host-syllentra-session')).toBe(
    false,
  );
  await page.getByRole('button', { name: 'Sitzung und Rechte neu prüfen' }).click();
  await page.getByLabel('Passwort zur Bestätigung der Geräteaktion').fill(password);
  await page.getByRole('button', { name: 'Anfrage 1 freigeben' }).click();
  await second.getByRole('button', { name: 'Gerätefreigabe prüfen' }).click();
  await expect(second.getByRole('heading', { name: 'Anmelden', exact: true })).toBeVisible();
  await login(second, email);
  await connected(second);
  await axe(second);
  await secondContext.close();
});

test('Recovery mit getrenntem Offlinecode beendet alte Sitzungen', async ({ page, browser }) => {
  const email = `recovery-${randomUUID()}@example.test`;
  await register(page, email);
  await login(page, email);
  await connected(page);
  const recoveryContext = await browser.newContext({ ignoreHTTPSErrors: true });
  const recovery = await recoveryContext.newPage();
  await recovery.goto('https://127.0.0.1:5174/#/identity');
  await recovery.getByRole('button', { name: 'Kontozugang wiederherstellen', exact: true }).click();
  await recovery.getByLabel('Künstliche E-Mail-Adresse').fill(email);
  await recovery.getByRole('button', { name: 'Fortfahren', exact: true }).click();
  await expect(
    recovery.getByRole('heading', { name: 'Wiederherstellung bestätigen' }),
  ).toBeVisible();
  await recovery
    .getByLabel('Einmalcode aus dem privaten Testkanal')
    .fill(internalSecret(email, 'recovery'));
  await recovery
    .getByLabel('Persönlicher Offline-Recoverycode')
    .fill(internalSecret(email, 'offline-recovery', true));
  await recovery.getByLabel('Neues Passwort').fill(newPassword);
  await axe(recovery);
  await recovery.getByRole('button', { name: 'Fortfahren', exact: true }).click();
  await expect(recovery.getByText('Kontozugang erneuert;', { exact: false })).toBeVisible();
  await login(recovery, email, newPassword);
  await connected(recovery);
  await page.getByRole('button', { name: 'Sitzung und Rechte neu prüfen' }).click();
  await expect(
    page.getByText('Keine verbundene Kontositzung', { exact: true }).first(),
  ).toBeVisible();
  await recoveryContext.close();
});

test('Identitätsformular in drei Sprachen, Themes und schmaler Ansicht', async ({ page }) => {
  mkdirSync('artifacts/identity', { recursive: true });
  for (const language of ['de', 'fr', 'en'])
    for (const theme of ['light', 'dark']) {
      await page.goto('/');
      await page.evaluate(
        ({ language, theme }) => {
          localStorage.setItem('syllentra-demo:language', language);
          localStorage.setItem('syllentra-demo:theme', theme);
        },
        { language, theme },
      );
      await page.reload();
      await page.setViewportSize({ width: 390, height: 844 });
      await page.goto('/#/identity');
      await expect(page.locator('html')).toHaveAttribute('lang', language);
      await expect(page.locator('html')).toHaveAttribute('data-theme', theme);
      await axe(page);
      expect(
        await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth),
      ).toBe(true);
      if (language === 'de')
        await page.screenshot({ path: `artifacts/identity/login-${theme}.png`, fullPage: true });
    }
});
