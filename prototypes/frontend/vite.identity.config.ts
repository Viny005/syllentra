import { readFileSync } from 'node:fs';
import { Agent } from 'node:https';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
const root = fileURLToPath(new URL('.', import.meta.url));
const cert = readFileSync(new URL('../backend/.local/identity.pem', import.meta.url));
export default defineConfig({
  plugins: [react()],
  preview: {
    host: '127.0.0.1',
    port: 5174,
    strictPort: true,
    https: { key: readFileSync(new URL('../backend/.local/identity.key', import.meta.url)), cert },
    proxy: {
      '/api': {
        target: 'https://127.0.0.1:8443',
        secure: true,
        agent: new Agent({ ca: cert }),
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
  server: {
    host: '127.0.0.1',
    port: 5174,
    strictPort: true,
    https: { key: readFileSync(new URL('../backend/.local/identity.key', import.meta.url)), cert },
    fs: { strict: true, allow: [root], deny: ['**/.local/**', '**/.env*', '**/*.key', '**/*.pem'] },
    proxy: {
      '/api': {
        target: 'https://127.0.0.1:8443',
        secure: true,
        agent: new Agent({ ca: cert }),
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
});
