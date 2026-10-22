import { useTranslation } from 'react-i18next';
import { Sun, Moon, Monitor, Languages, LockKeyhole } from 'lucide-react';
import type { Language, Theme } from '../lib/preferences';
import { PageHeading, TextLink } from '../ui/primitives';
export function Settings({
  language,
  theme,
  setLanguage,
  setTheme,
  storageAvailable,
}: {
  language: Language;
  theme: Theme;
  setLanguage: (language: Language) => void;
  setTheme: (theme: Theme) => void;
  storageAvailable: boolean;
}) {
  const { t } = useTranslation();
  return (
    <>
      <PageHeading title={t('settings')} description={t('settingsIntro')} />
      <div className="settings-grid">
        <section className="panel">
          <Languages className="muted" aria-hidden="true" size={24} />
          <h2>{t('language')}</h2>
          <p className="muted">{t('languageHelp')}</p>
          <div className="segmented" aria-label={t('language')}>
            {(['de', 'fr', 'en'] as const).map((lang) => (
              <button
                key={lang}
                lang={lang}
                onClick={() => setLanguage(lang)}
                aria-pressed={language === lang}
              >
                {{ de: 'Deutsch', fr: 'Français', en: 'English' }[lang]}
              </button>
            ))}
          </div>
        </section>
        <section className="panel">
          <Monitor className="muted" aria-hidden="true" size={24} />
          <h2>{t('theme')}</h2>
          <p className="muted">{t('themeHelp')}</p>
          <div className="segmented" aria-label={t('theme')}>
            {(['light', 'dark', 'system'] as const).map((choice, index) => {
              const Icon = [Sun, Moon, Monitor][index];
              return (
                <button
                  key={choice}
                  onClick={() => setTheme(choice)}
                  aria-pressed={theme === choice}
                >
                  <Icon size={16} aria-hidden="true" />
                  {t(choice)}
                </button>
              );
            })}
          </div>
        </section>
      </div>
      <p className="notice">{t('prefsNotice')}</p>
      {!storageAvailable && (
        <p role="status" className="notice">
          {t('storageUnavailable')}
        </p>
      )}
      <section className="panel unavailable-panel">
        <LockKeyhole size={24} aria-hidden="true" />
        <div>
          <h2>{t('unavailable')}</h2>
          <p className="muted">{t('unavailableBody')}</p>
          <TextLink href="#/administration">{t('administration')}</TextLink>
        </div>
      </section>
      <a className="button secondary" href="#/identity">
        {t('identityTitle')}
      </a>
    </>
  );
}
