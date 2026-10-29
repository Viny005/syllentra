import { useTranslation } from 'react-i18next';
import { ArrowUpRight, Sprout } from 'lucide-react';
import { modules } from '../data/demo';
import { Badge, Icon, PageHeading } from '../ui/primitives';
export function Progress({ onEvidence }: { onEvidence: () => void }) {
  const { t } = useTranslation();
  return (
    <>
      <PageHeading title={t('progress')} description={t('progressIntro')} />
      <p className="notice">
        <Sprout size={20} aria-hidden="true" />
        {t('progressNotice')}
      </p>
      <h2 className="section-title">{t('goals')}</h2>
      <div className="goal-list">
        {modules.map((module, index) => (
          <section className="goal-card" key={module.id}>
            <div className="goal-top">
              <span className={`course-icon ${module.color}`}>
                <Icon module={module.id} />
              </span>
              <div>
                <p className="eyebrow">{t(module.id)}</p>
                <h2>{t(`${module.id}Topic`)}</h2>
              </div>
              <Badge tone={index === 2 ? 'mint' : ''}>
                {t(index === 2 ? 'validated' : 'estimated')}
              </Badge>
            </div>
            <p>{t(`${module.id}Goal`)}</p>
            <div className="goal-bottom">
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
              <button className="text-link" onClick={onEvidence}>
                {t('sourceEvidence')}
                <ArrowUpRight size={16} aria-hidden="true" />
              </button>
            </div>
            {index === 2 && <p className="muted">{t('validatedBody')}</p>}
          </section>
        ))}
      </div>
    </>
  );
}
