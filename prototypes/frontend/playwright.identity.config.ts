import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: './tests/identity',
  workers: 1,
  fullyParallel: false,
  reporter: [['list'], ['json', { outputFile: 'test-results/identity-results.json' }]],
  use: {
    baseURL: 'https://127.0.0.1:5174',
    headless: true,
    ignoreHTTPSErrors: true,
    viewport: { width: 1280, height: 1000 },
    launchOptions: {
      executablePath: process.env.CHROMIUM_PATH || '/usr/bin/chromium',
      args: ['--no-sandbox'],
    },
    trace: 'off',
    screenshot: 'off',
    video: 'off',
  },
  webServer: [
    {
      command:
        'cd ../backend && .venv/bin/python scripts/migrate.py --test && PYTHONPATH=src .venv/bin/python -m scripts.identity_server --test',
      url: 'https://127.0.0.1:8443/health',
      ignoreHTTPSErrors: true,
      reuseExistingServer: false,
      timeout: 30000,
    },
    {
      command: 'npm run build && npm run preview:identity',
      url: 'https://127.0.0.1:5174',
      ignoreHTTPSErrors: true,
      reuseExistingServer: false,
      timeout: 30000,
    },
  ],
});
