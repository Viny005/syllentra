import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './locales/i18n';
import App from './App';
import './styles/tokens.css';
import './styles/app.css';
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
