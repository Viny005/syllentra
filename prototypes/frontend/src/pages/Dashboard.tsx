import { ArrowRight, Sparkles, CalendarDays, ArrowUpRight, StickyNote } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { modules } from '../data/demo';
import type { StudyEvent } from '../data/demo';
import { ModuleCard } from '../features/ModuleCard';
import { Badge, TextLink } from '../ui/primitives';
import { formatDate } from '../lib/calendar';
import type { Language } from '../lib/preferences';
export function Dashboard({
  onPlan,
  events,
  language,
}: {
  onPlan: () => void;
  events: StudyEvent[];
  language: Language;
}) {
  const { t } = useTranslation();
  return (
    <>
      <div className="dashboard-heading">
        <div>
          <p className="eyebrow">{t('welcome')}</p>
          <h1>{t('dashboard')}</h1>
        </div>
        <span className="date-line">
          <CalendarDays size={16} aria-hidden="true" />
          {formatDate('2026-10-22', language, { weekday: 'long', day: 'numeric', month: 'long' })}
        </span>
      </div>
      <div className="dashboard-grid">
        <div className="dashboard-main">
          <section className="hero">
            <div className="hero-content">
              <Badge>
                <span className="tiny-dot" />
                {t('semester')}
              </Badge>
              <h2>{t('greeting')}</h2>
              <p>{t('heroText')}</p>
              <div className="hero-actions">
                <button className="button primary" onClick={onPlan}>
                  {t('start')}
                  <ArrowRight size={18} aria-hidden="true" />
                </button>
                <a className="button subtle" href="#/courses">
                  {t('explore')}
                </a>
              </div>
            </div>
            <div className="hero-art" aria-hidden="true">
              <div className="orbit orbit-one" />
              <div className="orbit orbit-two" />
              <div className="orbital-card">
                <span>∑</span>
                <i />
                <i />
                <i />
              </div>
              <span className="art-spark">✦</span>
              <span className="art-dot" />
            </div>
          </section>
          <section className="section-block" aria-labelledby="your-courses">
            <div className="section-heading">
              <h2 id="your-courses">{t('yourCourses')}</h2>
              <TextLink href="#/courses">{t('allCourses')}</TextLink>
            </div>
            <div className="module-grid">
              {modules.map((module) => (
                <ModuleCard key={module.id} module={module} />
              ))}
            </div>
          </section>
          <section className="continue-card">
            <span className="course-icon lavender">
              <StickyNote size={22} aria-hidden="true" />
            </span>
            <div>
              <p className="eyebrow">{t('keepGoing')}</p>
              <h3>{t('noteVectors')}</h3>
              <p className="muted">
                {t('recentNote')} · {t('math')}
              </p>
            </div>
            <a className="button secondary" href="#/notes">
              {t('noteAction')}
              <ArrowUpRight size={17} aria-hidden="true" />
            </a>
          </section>
        </div>
        <aside className="dashboard-aside">
          <section className="focus-card">
            <div className="focus-label">
              <Sparkles size={17} aria-hidden="true" />
              <span>{t('studyTip')}</span>
            </div>
            <h2>{t('focusTitle')}</h2>
            <p>{t('focusBody')}</p>
            <a href="#/assistant" className="focus-link">
              {t('focusAction')}
              <ArrowRight size={18} aria-hidden="true" />
            </a>
            <div className="focus-mark" aria-hidden="true">
              ✳
            </div>
          </section>
          <section className="agenda">
            <div className="section-heading">
              <h2>{t('upNext')}</h2>
              <span className="small-label">{t('demoShort')}</span>
            </div>
            <p className="muted agenda-date">{t('thisWeek')}</p>
            <div className="agenda-list">
              {events
                .filter((event) => event.date >= '2026-10-22')
                .slice()
                .sort((a, b) => (a.date + a.time).localeCompare(b.date + b.time))
                .slice(0, 3)
                .map((event) => (
                  <a key={event.id} href="#/calendar" className="agenda-item">
                    <span className="agenda-time">
                      {event.time}
                      <small>
                        {formatDate(event.date, language, { day: 'numeric', month: 'short' })}
                      </small>
                    </span>
                    <span className={`agenda-rule ${event.module}`} />
                    <span>
                      <strong>{event.translated ? t(event.title) : event.title}</strong>
                      <small>{t(event.module)}</small>
                    </span>
                  </a>
                ))}
            </div>
            <TextLink href="#/calendar">{t('openCalendar')}</TextLink>
          </section>
        </aside>
      </div>
      <p className="demo-footnote">{t('fiction')}</p>
    </>
  );
}
