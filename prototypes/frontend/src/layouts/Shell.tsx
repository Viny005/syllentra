import { useState } from 'react';
import type { ReactNode } from 'react';
import { useTranslation } from 'react-i18next';
import {
  LayoutDashboard,
  BookOpen,
  FolderOpen,
  Sparkles,
  StickyNote,
  CalendarDays,
  ChartNoAxesCombined,
  Settings,
  LockKeyhole,
  Menu,
  Search,
  Sun,
  Moon,
  Monitor,
  CircleHelp,
  ChevronRight,
} from 'lucide-react';
import type { Language, Theme } from '../lib/preferences';
import { Dialog } from '../ui/primitives';
const primary = [
  ['/', 'dashboard', LayoutDashboard],
  ['/courses', 'courses', BookOpen],
  ['/library', 'library', FolderOpen],
  ['/assistant', 'assistant', Sparkles],
  ['/notes', 'notes', StickyNote],
] as const;
const secondary = [
  ['/calendar', 'calendar', CalendarDays],
  ['/progress', 'progress', ChartNoAxesCombined],
  ['/settings', 'settings', Settings],
] as const;
export function Shell({
  route,
  language,
  theme,
  setLanguage,
  setTheme,
  children,
}: {
  route: string;
  language: Language;
  theme: Theme;
  setLanguage: (value: Language) => void;
  setTheme: (value: Theme) => void;
  children: ReactNode;
}) {
  const { t } = useTranslation();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [about, setAbout] = useState(false);
  const current = [...primary, ...secondary].find(([path]) =>
    path === '/' ? route === '/' : route === path || route.startsWith(path + '/'),
  );
  const ThemeIcon = theme === 'dark' ? Moon : theme === 'light' ? Sun : Monitor;
  function nav(items: typeof primary | typeof secondary) {
    return items.map(([path, key, Icon]) => {
      const active = path === '/' ? route === '/' : route.startsWith(path);
      return (
        <a
          key={path}
          href={`#${path}`}
          className={active ? 'nav-link active' : 'nav-link'}
          aria-current={active ? 'page' : undefined}
          onClick={() => setMobileOpen(false)}
        >
          <Icon size={19} aria-hidden="true" />
          <span>{t(key)}</span>
          {active && <span className="nav-dot" />}
        </a>
      );
    });
  }
  return (
    <div className="app-shell">
      <a
        className="skip-link"
        href="#main-content"
        onClick={(event) => {
          event.preventDefault();
          document.getElementById('main-content')?.focus();
        }}
      >
        {t('skip')}
      </a>
      <aside className="sidebar">
        <a className="brand" href="#/">
          <span className="brand-mark" aria-hidden="true">
            s<span>✦</span>
          </span>
          <span>
            syllentra<span className="brand-ai">AI</span>
          </span>
        </a>
        <div className="workspace-card">
          <span className="workspace-avatar" aria-hidden="true">
            S
          </span>
          <div>
            <strong>{t('workspace')}</strong>
            <small>{t('demoShort')} · 2026</small>
          </div>
        </div>
        <nav aria-label={t('workspace')}>
          <p className="nav-label">{t('learning')}</p>
          {nav(primary)}
          <p className="nav-label second-label">{t('organize')}</p>
          {nav(secondary)}
        </nav>
        <div className="sidebar-footer">
          <a href="#/administration" className="admin-link">
            <LockKeyhole size={17} aria-hidden="true" />
            {t('administration')}
          </a>
          <button className="help-link" onClick={() => setAbout(true)}>
            <CircleHelp size={17} aria-hidden="true" />
            {t('about')}
          </button>
          <span className="local-label">
            <span className="tiny-dot" />
            {t('localOnly')}
          </span>
        </div>
      </aside>
      <div className="app-column">
        <header className="topbar">
          <button
            className="icon-button mobile-menu"
            onClick={() => setMobileOpen(true)}
            aria-label={t('menu')}
          >
            <Menu size={22} aria-hidden="true" />
          </button>
          <div className="breadcrumb">
            <span>Syllentra AI</span>
            <ChevronRight size={14} aria-hidden="true" />
            <strong>
              {t(
                current?.[1] ||
                  (route === '/identity'
                    ? 'identityTitle'
                    : route === '/administration'
                      ? 'administration'
                      : 'notFound'),
              )}
            </strong>
          </div>
          <div className="topbar-actions">
            <span className="prototype-badge">
              <span className="tiny-dot" />
              <span className="prototype-wide">
                {t(route === '/identity' ? 'identityBadge' : 'demo')}
              </span>
              <span className="prototype-compact">
                {t(route === '/identity' ? 'identityBadge' : 'demoShort')}
              </span>
            </span>
            <a
              href="#/library"
              className="icon-button search-shortcut"
              aria-label={t('searchLibrary')}
            >
              <Search size={19} aria-hidden="true" />
            </a>
            <label>
              <span className="sr-only">{t('language')}</span>
              <select
                className="language-select"
                value={language}
                onChange={(event) => setLanguage(event.target.value as Language)}
              >
                <option value="de">DE</option>
                <option value="fr">FR</option>
                <option value="en">EN</option>
              </select>
            </label>
            <button
              className="icon-button"
              onClick={() =>
                setTheme(theme === 'light' ? 'dark' : theme === 'dark' ? 'system' : 'light')
              }
              aria-label={`${t('switchTheme')}: ${t(theme)}`}
            >
              <ThemeIcon size={19} aria-hidden="true" />
            </button>
          </div>
        </header>
        <main id="main-content" tabIndex={-1} key={route}>
          {children}
        </main>
        <footer className="app-footer">
          <span>Syllentra AI</span>
          <span>
            {t('demo')} · {t('localOnly')}
          </span>
        </footer>
      </div>
      {mobileOpen && (
        <Dialog title={t('workspace')} onClose={() => setMobileOpen(false)}>
          <nav className="mobile-nav" aria-label={t('menu')}>
            {nav(primary)}
            {nav(secondary)}
            <a href="#/administration" onClick={() => setMobileOpen(false)}>
              <LockKeyhole size={18} aria-hidden="true" />
              {t('administration')}
            </a>
          </nav>
        </Dialog>
      )}
      {about && (
        <Dialog title={t('about')} onClose={() => setAbout(false)}>
          <p className="reading-copy">{t('aboutBody')}</p>
          <button className="button primary" onClick={() => setAbout(false)}>
            {t('close')}
          </button>
        </Dialog>
      )}
    </div>
  );
}
