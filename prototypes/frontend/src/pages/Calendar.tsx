import { ChevronLeft, ChevronRight, Plus } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { useState } from 'react';
import type { StudyEvent } from '../data/demo';
import type { Language } from '../lib/preferences';
import { addDays, formatDate } from '../lib/calendar';
import { Badge, PageHeading } from '../ui/primitives';
export function Calendar({
  events,
  language,
  onPlan,
}: {
  events: StudyEvent[];
  language: Language;
  onPlan: () => void;
}) {
  const { t } = useTranslation();
  const [start, setStart] = useState('2026-10-19');
  return (
    <>
      <PageHeading title={t('calendar')} description={t('calendarIntro')}>
        <button className="button primary" onClick={onPlan}>
          <Plus size={18} aria-hidden="true" />
          {t('planSession')}
        </button>
      </PageHeading>
      <div className="calendar-toolbar">
        <div className="week-navigation">
          <button
            className="icon-button"
            onClick={() => setStart(addDays(start, -7))}
            aria-label={t('previousWeek')}
          >
            <ChevronLeft aria-hidden="true" size={20} />
          </button>
          <h2 aria-live="polite">
            {formatDate(start, language)} – {formatDate(addDays(start, 6), language)}
          </h2>
          <button
            className="icon-button"
            onClick={() => setStart(addDays(start, 7))}
            aria-label={t('nextWeek')}
          >
            <ChevronRight aria-hidden="true" size={20} />
          </button>
        </div>
        <button className="button secondary" onClick={() => setStart('2026-10-19')}>
          {t('demoWeek')}
        </button>
      </div>
      <div className="week-grid">
        {Array.from({ length: 7 }, (_, index) => addDays(start, index)).map((day) => (
          <section
            key={day}
            className={`day-column ${day === '2026-10-22' ? 'selected-day' : ''}`}
            aria-label={formatDate(day, language, {
              weekday: 'long',
              day: 'numeric',
              month: 'long',
            })}
          >
            <div className="day-heading">
              <span>{formatDate(day, language, { weekday: 'short' })}</span>
              <strong>{formatDate(day, language, { day: 'numeric' })}</strong>
            </div>
            <div className="day-events">
              {events
                .filter((event) => event.date === day)
                .sort((a, b) => a.time.localeCompare(b.time))
                .map((event) => (
                  <article key={event.id} className={`calendar-event ${event.module}`}>
                    <span className="small-label">{t(event.kind)}</span>
                    <strong>{event.time}</strong>
                    <h3>{event.translated ? t(event.title) : event.title}</h3>
                    <small>{t(event.module)}</small>
                    {event.local && <small>{t('localSession')}</small>}
                  </article>
                ))}
            </div>
          </section>
        ))}
      </div>
      {!events.some((event) => event.date >= start && event.date <= addDays(start, 6)) && (
        <p role="status" className="empty-inline">
          {t('noEvents')}
        </p>
      )}
      <div className="calendar-legend">
        <Badge tone="mint">{t('session')}</Badge>
        <Badge tone="lavender">{t('event')}</Badge>
      </div>
      <p className="notice">{t('calendarNotice')}</p>
    </>
  );
}
