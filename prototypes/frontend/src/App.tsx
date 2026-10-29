import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { LockKeyhole } from 'lucide-react';
import { Shell } from './layouts/Shell';
import { Dashboard } from './pages/Dashboard';
import { Courses } from './pages/Courses';
import { Library } from './pages/Library';
import { Notes } from './pages/Notes';
import { Calendar } from './pages/Calendar';
import { Progress } from './pages/Progress';
import { Settings } from './pages/Settings';
import { Assistant } from './pages/Assistant';
import { Identity } from './pages/Identity';
import { SessionForm } from './features/SessionForm';
import { Badge, Dialog, EmptyState, PageHeading } from './ui/primitives';
import { initialEvents } from './data/demo';
import type { DemoDocument, StudyEvent } from './data/demo';
import { isLanguage, isTheme, readPreference, writePreference } from './lib/preferences';
import type { Language, Theme } from './lib/preferences';
import { useRoute } from './lib/useRoute';
export default function App() {
  const { t, i18n } = useTranslation();
  const route = useRoute();
  const language: Language = isLanguage(i18n.language) ? i18n.language : 'de';
  const [theme, setThemeState] = useState<Theme>(() => {
    const value = readPreference('theme');
    return isTheme(value) ? value : 'system';
  });
  const [storageAvailable, setStorageAvailable] = useState(true);
  const [events, setEvents] = useState(initialEvents);
  const [modal, setModal] = useState<'session' | 'evidence' | null>(null);
  const [preview, setPreview] = useState<DemoDocument | null>(null);
  const [notice, setNotice] = useState('');
  useEffect(() => {
    const media = window.matchMedia('(prefers-color-scheme: dark)');
    const update = () => {
      document.documentElement.dataset.theme =
        theme === 'system' ? (media.matches ? 'dark' : 'light') : theme;
    };
    update();
    media.addEventListener('change', update);
    return () => media.removeEventListener('change', update);
  }, [theme]);
  useEffect(() => {
    document.documentElement.lang = language;
    document.title = `Syllentra AI · ${t('demo')}`;
  }, [language, t]);
  useEffect(() => {
    document.getElementById('main-content')?.focus();
    window.scrollTo(0, 0);
    setNotice('');
  }, [route]);
  function setLanguage(value: Language) {
    void i18n.changeLanguage(value);
    setStorageAvailable(writePreference('language', value));
  }
  function setTheme(value: Theme) {
    setThemeState(value);
    setStorageAvailable(writePreference('theme', value));
  }
  function saveSession(event: StudyEvent) {
    setEvents((previous) => [...previous, event]);
    setModal(null);
    setNotice('sessionSaved');
  }
  let page;
  if (route === '/')
    page = <Dashboard onPlan={() => setModal('session')} events={events} language={language} />;
  else if (route === '/courses' || route.startsWith('/courses/'))
    page = <Courses selected={route.startsWith('/courses/') ? route.slice(9) : undefined} />;
  else if (route === '/library') page = <Library language={language} onPreview={setPreview} />;
  else if (route === '/assistant') page = <Assistant language={language} />;
  else if (route === '/identity') page = <Identity />;
  else if (route === '/notes') page = <Notes />;
  else if (route === '/calendar')
    page = <Calendar events={events} language={language} onPlan={() => setModal('session')} />;
  else if (route === '/progress') page = <Progress onEvidence={() => setModal('evidence')} />;
  else if (route === '/settings')
    page = (
      <Settings
        language={language}
        theme={theme}
        setLanguage={setLanguage}
        setTheme={setTheme}
        storageAvailable={storageAvailable}
      />
    );
  else if (route === '/administration')
    page = (
      <>
        <PageHeading title={t('administration')} description={t('adminTitle')} />
        <section className="admin-boundary">
          <LockKeyhole size={40} aria-hidden="true" />
          <h2>{t('adminTitle')}</h2>
          <p>{t('adminBody')}</p>
          <a className="button secondary" href="#/">
            {t('backHome')}
          </a>
        </section>
      </>
    );
  else
    page = (
      <EmptyState title={t('notFound')} description={t('notFoundBody')}>
        <a className="button primary" href="#/">
          {t('backHome')}
        </a>
      </EmptyState>
    );
  return (
    <Shell
      route={route}
      language={language}
      theme={theme}
      setLanguage={setLanguage}
      setTheme={setTheme}
    >
      {notice && (
        <p className="success-message" role="status">
          {t(notice)}
        </p>
      )}
      {page}
      {modal && (
        <Dialog
          title={t(modal === 'session' ? 'planSession' : 'evidence')}
          onClose={() => setModal(null)}
        >
          {modal === 'session' ? (
            <SessionForm onSave={saveSession} />
          ) : (
            <>
              <p className="reading-copy">{t('evidenceBody')}</p>
              <button className="button primary" onClick={() => setModal(null)}>
                {t('close')}
              </button>
            </>
          )}
        </Dialog>
      )}
      {preview && (
        <Dialog title={t(preview.title)} onClose={() => setPreview(null)}>
          <Badge>{t('previewNotice')}</Badge>
          <div className="preview-paper">
            <p className="eyebrow">{t(preview.module)}</p>
            <h3>{t(`${preview.module}Topic`)}</h3>
            <p>{t(`${preview.module}Goal`)}</p>
            <p className="muted">{t('pdfFuture')}</p>
          </div>
          <a href="#/assistant" className="button primary" onClick={() => setPreview(null)}>
            {t('sourceAsk')}
          </a>
        </Dialog>
      )}
    </Shell>
  );
}
