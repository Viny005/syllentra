import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { FileText, Search, Headphones, ArrowUpRight } from 'lucide-react';
import { documents, modules } from '../data/demo';
import type { DemoDocument } from '../data/demo';
import type { Language } from '../lib/preferences';
import { formatDate } from '../lib/calendar';
import { Badge, EmptyState, PageHeading } from '../ui/primitives';
export function Library({
  language,
  onPreview,
}: {
  language: Language;
  onPreview: (document: DemoDocument) => void;
}) {
  const { t } = useTranslation();
  const [query, setQuery] = useState('');
  const [course, setCourse] = useState('all');
  const [format, setFormat] = useState('all');
  const filtered = documents.filter(
    (document) =>
      (course === 'all' || document.module === course) &&
      (format === 'all' || document.type === format) &&
      `${t(document.title)} ${t(document.module)}`
        .toLocaleLowerCase(language)
        .includes(query.toLocaleLowerCase(language).trim()),
  );
  return (
    <>
      <PageHeading title={t('library')} description={t('libraryIntro')} />
      <div className="library-toolbar">
        <label className="search-field">
          <Search size={19} aria-hidden="true" />
          <span className="sr-only">{t('search')}</span>
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder={t('searchPlaceholder')}
          />
        </label>
        <label>
          <span className="sr-only">{t('filterCourse')}</span>
          <select value={course} onChange={(event) => setCourse(event.target.value)}>
            <option value="all">{t('allCourses')}</option>
            {modules.map((module) => (
              <option value={module.id} key={module.id}>
                {t(module.id)}
              </option>
            ))}
          </select>
        </label>
        <label>
          <span className="sr-only">{t('format')}</span>
          <select value={format} onChange={(event) => setFormat(event.target.value)}>
            <option value="all">{t('allTypes')}</option>
            <option value="pdf">{t('pdf')}</option>
            <option value="audio">{t('audio')}</option>
          </select>
        </label>
      </div>
      <p className="muted" role="status">
        {t('results', { count: filtered.length })} · {t('sample')}
      </p>
      {filtered.length === 0 ? (
        <EmptyState title={t('emptyDocuments')} description={t('emptySearch')}>
          <button
            className="button secondary"
            onClick={() => {
              setQuery('');
              setCourse('all');
              setFormat('all');
            }}
          >
            {t('reset')}
          </button>
        </EmptyState>
      ) : (
        <div className="document-grid">
          {filtered.map((document) => (
            <button
              key={document.id}
              className="document-card"
              onClick={() => onPreview(document)}
              aria-label={`${t('preview')}: ${t(document.title)}`}
            >
              <div
                className={`document-cover ${modules.find((module) => module.id === document.module)?.color}`}
              >
                <span>
                  {document.type === 'audio' ? (
                    <Headphones size={32} aria-hidden="true" />
                  ) : (
                    <FileText size={32} aria-hidden="true" />
                  )}
                </span>
                <div className="paper-lines" aria-hidden="true">
                  <i />
                  <i />
                  <i />
                </div>
                <Badge>{t(document.type)}</Badge>
              </div>
              <div className="document-content">
                <p className="eyebrow">{t(document.module)}</p>
                <h2>{t(document.title)}</h2>
                <p className="muted">
                  {document.pages ? t('pages', { count: document.pages }) : t('audioLength')}
                </p>
                <div className="document-bottom">
                  <small>
                    {formatDate(document.date, language, { day: 'numeric', month: 'short' })}
                  </small>
                  <ArrowUpRight size={18} aria-hidden="true" />
                </div>
              </div>
            </button>
          ))}
        </div>
      )}
    </>
  );
}
