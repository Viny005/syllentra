import { ArrowUpRight } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { modules } from '../data/demo';
import { Icon } from '../ui/primitives';
export function ModuleCard({ module }: { module: (typeof modules)[number] }) {
  const { t } = useTranslation();
  return (
    <a className="module-card" href={`#/courses/${module.id}`}>
      <div className="card-top">
        <span className={`course-icon ${module.color}`}>
          <Icon module={module.id} />
        </span>
        <ArrowUpRight className="muted" size={20} aria-hidden="true" />
      </div>
      <p className="eyebrow">{module.code}</p>
      <h3>{t(module.id)}</h3>
      <p className="card-description">{t(`${module.id}Desc`)}</p>
      <div className="card-progress">
        <div>
          <span>{t('sampleProgress')}</span>
          <strong>{module.progress}%</strong>
        </div>
        <progress
          max={100}
          value={module.progress}
          aria-label={`${t(module.id)}: ${t('sampleProgress')}`}
        />
      </div>
      <div className="card-meta">
        <span>{t('topicsCount', { count: module.topics })}</span>
        <span>{t('demoShort')}</span>
      </div>
    </a>
  );
}
