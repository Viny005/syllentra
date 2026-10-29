import { expect, test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
const routes = [
  ['/', 'Übersicht'],
  ['/courses', 'Meine Kurse'],
  ['/library', 'Bibliothek'],
  ['/assistant', 'KI-Lernbegleiter'],
  ['/notes', 'Notizen'],
  ['/calendar', 'Studienkalender'],
  ['/progress', 'Lernfortschritt'],
  ['/settings', 'Einstellungen'],
] as const;
test('alle Seiten in beiden Themes: Routen, Konsole, Netzwerk, Kontrast und Screenshots', async ({
  page,
}) => {
  const errors: string[] = [];
  const remote: string[] = [];
  page.on('pageerror', (error) => errors.push(error.message));
  page.on('request', (request) => {
    if (!request.url().startsWith('http://127.0.0.1:4173/')) remote.push(request.url());
  });
  await page.goto('/');
  for (const theme of ['light', 'dark']) {
    await page.evaluate((value) => localStorage.setItem('syllentra-demo:theme', value), theme);
    await page.reload();
    for (const [route, title] of routes) {
      await page.goto(`/#${route}`);
      await expect(page.getByRole('heading', { name: title, exact: true, level: 1 })).toBeVisible();
      await expect(page.locator('html')).toHaveAttribute('data-theme', theme);
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(
        true,
      );
      const result = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'])
        .analyze();
      expect(result.violations, JSON.stringify(result.violations, null, 2)).toEqual([]);
      await page.screenshot({
        path: `artifacts/screenshots/${route.slice(1) || 'dashboard'}-${theme}.png`,
        fullPage: true,
      });
    }
  }
  expect(errors).toEqual([]);
  expect(remote).toEqual([]);
});
test('Moduldetails, leere Liste und Browser-Zurück', async ({ page }) => {
  await page.goto('/#/courses');
  await page
    .getByRole('link')
    .filter({ has: page.getByRole('heading', { name: 'Lineare Algebra', exact: true }) })
    .click();
  await expect(page.getByRole('heading', { name: 'Lernziele', exact: true })).toBeVisible();
  await page.goBack();
  await page.getByRole('button', { name: 'Frühere Semester', exact: true }).click();
  await expect(page.getByRole('heading', { name: 'Hier ist noch Raum für Neues.' })).toBeVisible();
  await page.getByRole('button', { name: 'Aktuell', exact: true }).first().click();
  await expect(page.locator('.module-card')).toHaveCount(3);
});
test('lokale Dokumentfilter, Dialogfokus, Escape und Vorschau', async ({ page }) => {
  await page.goto('/#/library');
  await page.getByRole('searchbox', { name: 'Suchen', exact: true }).fill('kein-treffer');
  await expect(page.getByRole('heading', { name: 'Keine passenden Materialien' })).toBeVisible();
  await page.getByRole('button', { name: 'Filter zurücksetzen' }).click();
  await page.getByRole('combobox', { name: 'Format', exact: true }).selectOption('audio');
  await expect(page.locator('.document-card')).toHaveCount(1);
  const trigger = page.getByRole('button', { name: 'Vorschau öffnen: Lernimpuls: Vektoren' });
  await trigger.click();
  await expect(page.getByRole('dialog')).toBeVisible();
  await expect(page.getByRole('dialog')).toContainText('Keine echte Datei geladen');
  await page.getByRole('dialog').getByRole('button', { name: 'Schließen', exact: true }).focus();
  await page.keyboard.press('Shift+Tab');
  await expect(page.getByRole('dialog').getByRole('link')).toBeFocused();
  await page.keyboard.press('Tab');
  await expect(
    page.getByRole('dialog').getByRole('button', { name: 'Schließen', exact: true }),
  ).toBeFocused();
  await page.keyboard.press('Escape');
  await expect(page.getByRole('dialog')).toHaveCount(0);
  await expect(trigger).toBeFocused();
});
test('Kalenderformular: Fehler, einmalige lokale Speicherung und keine Persistenz', async ({
  page,
}) => {
  await page.goto('/#/calendar');
  await page.getByRole('button', { name: 'Neue Lernsession', exact: true }).click();
  await page.getByRole('button', { name: 'Für diese Demo speichern' }).click();
  await expect(page.getByRole('alert')).toBeVisible();
  await page.getByRole('textbox', { name: 'Titel', exact: true }).fill('Synthetischer Termin');
  await page.getByRole('button', { name: 'Für diese Demo speichern' }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  await expect(
    page.getByRole('heading', { name: 'Synthetischer Termin', exact: true }),
  ).toHaveCount(1);
  await page.getByRole('button', { name: 'Nächste Woche', exact: true }).click();
  await expect(page.getByRole('status').filter({ hasText: 'Keine Termine' })).toContainText(
    'Keine Termine',
  );
  await page.reload();
  await expect(
    page.getByRole('heading', { name: 'Synthetischer Termin', exact: true }),
  ).toHaveCount(0);
});
test('Chat: Fehler, feste Simulation, Stop und kein HTML', async ({ page }) => {
  await page.goto('/#/assistant');
  await page.getByRole('button', { name: 'Nachricht senden' }).click();
  await expect(page.getByRole('alert')).toBeVisible();
  await page
    .getByRole('textbox', { name: 'Deine Nachricht' })
    .fill('<script>window.example=true</script>');
  await page.getByRole('button', { name: 'Nachricht senden' }).click();
  await expect(page.getByRole('button', { name: 'Simulation stoppen' })).toBeVisible();
  await page.getByRole('button', { name: 'Simulation stoppen' }).click();
  await expect(page.locator('.chat-status')).toContainText('Simulation gestoppt');
  await page.getByRole('textbox', { name: 'Deine Nachricht' }).fill('Fiktive Testfrage');
  await page.getByRole('button', { name: 'Nachricht senden' }).click();
  await expect(page.locator('.chat-message.assistant')).toContainText('feste Beispielantwort');
  expect(await page.evaluate(() => Object.hasOwn(window, 'example'))).toBe(false);
  await expect(
    page.getByRole('link', { name: 'Beispielquelle · Vektorräume, S. 3' }),
  ).toBeVisible();
});
test('Sprachen, Datumsformate, Theme-System und erlaubte lokale Speicherung', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.goto('/#/settings');
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
  await page.getByRole('button', { name: 'Hell', exact: true }).click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
  await page.getByRole('button', { name: 'Français', exact: true }).click();
  await expect(page.locator('html')).toHaveAttribute('lang', 'fr');
  await page.getByRole('button', { name: 'English', exact: true }).click();
  await expect(
    page.getByRole('heading', { name: 'Settings', exact: true, level: 1 }),
  ).toBeVisible();
  await page.getByRole('button', { name: 'System', exact: true }).click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
  await page.emulateMedia({ colorScheme: 'light' });
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
  await page.goto('/');
  await expect(page.locator('.date-line')).toContainText('October');
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  expect(await page.evaluate(() => Object.keys(localStorage).sort())).toEqual([
    'syllentra-demo:language',
    'syllentra-demo:theme',
  ]);
});
test('Mobile Navigation, Reflow und reduzierte Bewegung in DE/FR/EN', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto('/');
  for (const lang of ['de', 'fr', 'en']) {
    await page.getByRole('combobox', { name: /Sprache|Langue|Language/ }).selectOption(lang);
    for (const [route] of routes) {
      await page.goto(`/#${route}`);
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(
        true,
      );
      await expect(page.locator('h1')).toBeVisible();
    }
  }
  await page.getByRole('button', { name: 'Open navigation' }).click();
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByRole('dialog').getByRole('link', { name: 'My courses', exact: true }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  await expect(
    page.getByRole('heading', { name: 'My courses', exact: true, level: 1 }),
  ).toBeVisible();
  await page.goto('/');
  await page.screenshot({ path: 'artifacts/screenshots/mobile-light.png', fullPage: true });
  await page.getByRole('button', { name: 'Change appearance: System' }).click();
  await page.getByRole('button', { name: 'Change appearance: Light' }).click();
  await page.screenshot({ path: 'artifacts/screenshots/mobile-dark.png', fullPage: true });
  await page.setViewportSize({ width: 320, height: 800 });
  for (const [route] of routes) {
    await page.goto(`/#${route}`);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(
      true,
    );
  }
});
test('Notizen, Herkunft, Adminabgrenzung und unbekannte Route', async ({ page }) => {
  await page.goto('/#/notes');
  await page.getByRole('button', { name: 'Prozesse in eigenen Worten Informatiksysteme' }).click();
  await expect(page.locator('.note-paper')).toContainText('laufendes Programm');
  await page.goto('/#/progress');
  await page.getByRole('button', { name: 'Herkunft ansehen' }).first().click();
  await expect(page.getByRole('dialog')).toContainText('keine Antworten bewertet');
  await page.keyboard.press('Escape');
  await page.goto('/#/administration');
  await expect(page.locator('.admin-boundary')).toContainText(
    'weder Anmeldung noch Rechteverwaltung',
  );
  await expect(page.getByRole('textbox')).toHaveCount(0);
  await page.goto('/#/unknown');
  await expect(page.getByRole('heading', { name: 'Dieser Lernpfad ist noch leer.' })).toBeVisible();
  await page.getByRole('link', { name: 'Zur Übersicht', exact: true }).click();
  await expect(
    page.getByRole('heading', { name: 'Übersicht', exact: true, level: 1 }),
  ).toBeVisible();
});

test('blockierter Browserspeicher, Tastaturzugang und französische mobile Zugänglichkeit', async ({
  page,
}) => {
  await page.addInitScript(() => {
    Object.defineProperty(Storage.prototype, 'getItem', {
      value: () => {
        throw new Error('blocked');
      },
    });
    Object.defineProperty(Storage.prototype, 'setItem', {
      value: () => {
        throw new Error('blocked');
      },
    });
  });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/#/settings');
  await page.getByRole('button', { name: 'Français', exact: true }).click();
  await expect(page.getByRole('status')).toContainText('stockage');
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'])
        .analyze()
    ).violations,
  ).toEqual([]);
  await page.getByRole('button', { name: 'Ouvrir la navigation' }).focus();
  await page.keyboard.press('Enter');
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.getByRole('button', { name: 'Ouvrir la navigation' })).toBeFocused();
});
