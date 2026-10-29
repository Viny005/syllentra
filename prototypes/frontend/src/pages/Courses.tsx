import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { modules, documents } from '../data/demo';
import { ModuleCard } from '../features/ModuleCard';
import { Badge, EmptyState, Icon, PageHeading, TextLink } from '../ui/primitives';
export function Courses({ selected }: { selected?: string }) {
  const { t } = useTranslation();
  const [filter, setFilter] = useState('active');
  const module = modules.find((item) => item.id === selected);
  if (selected && !module)
    return (
      <EmptyState title={t('notFound')}>
        <a className="button primary" href="#/courses">
          {t('backCourses')}
        </a>
      </EmptyState>
    );
  if (module)
    return (
      <>
        <TextLink href="#/courses">{t('backCourses')}</TextLink>
        <PageHeading title={t(module.id)} description={t(`${module.id}Desc`)}>
          <span className={`course-icon large ${module.color}`}>
            <Icon module={module.id} size={32} />
          </span>
        </PageHeading>
        <div className="detail-grid">
          <section className="panel">
            <Badge>{module.code}</Badge>
            <h2>{t('learningGoals')}</h2>
            <p className="reading-copy">{t(`${module.id}Goal`)}</p>
            <h3>{t('chapters')}</h3>
            <div className="topic-row">
              <span className={`course-icon ${module.color}`}>
                <Icon module={module.id} />
              </span>
              <span>{t(`${module.id}Topic`)}</span>
            </div>
            <a className="button primary" href="#/assistant">
              {t('discuss')}
            </a>
          </section>
          <section className="panel">
            <h2>{t('resources')}</h2>
            {documents
              .filter((document) => document.module === module.id)
              .map((document) => (
                <a className="resource-row" key={document.id} href="#/library">
                  <strong>{t(document.title)}</strong>
                  <Badge>{t(document.type)}</Badge>
                </a>
              ))}
            <p className="muted">{t('credits', { count: module.credits })}</p>
            <p className="notice">{t('courseData')}</p>
          </section>
        </div>
      </>
    );
  return (
    <>
      <PageHeading title={t('courses')} description={t('courseIntro')} />
      <div className="toolbar">
        <div className="segmented" aria-label={t('filterCourse')}>
          {['active', 'archived'].map((value) => (
            <button aria-pressed={filter === value} key={value} onClick={() => setFilter(value)}>
              {t(value)}
            </button>
          ))}
        </div>
        <Badge>{t('semester')}</Badge>
      </div>
      {filter === 'archived' ? (
        <EmptyState title={t('emptyCourses')} description={t('emptyCoursesText')}>
          <button className="button secondary" onClick={() => setFilter('active')}>
            {t('active')}
          </button>
        </EmptyState>
      ) : (
        <div className="module-grid courses-grid">
          {modules.map((module) => (
            <ModuleCard key={module.id} module={module} />
          ))}
        </div>
      )}
      <p className="demo-footnote">{t('courseData')}</p>
    </>
  );
}
