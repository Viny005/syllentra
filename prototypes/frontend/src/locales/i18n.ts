import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import de from './de.json';
import fr from './fr.json';
import en from './en.json';
import { isLanguage, readPreference } from '../lib/preferences';
const stored = readPreference('language');
void i18n.use(initReactI18next).init({
  resources: { de: { translation: de }, fr: { translation: fr }, en: { translation: en } },
  lng: isLanguage(stored) ? stored : 'de',
  fallbackLng: 'de',
  supportedLngs: ['de', 'fr', 'en'],
  interpolation: { escapeValue: false },
});
export default i18n;
