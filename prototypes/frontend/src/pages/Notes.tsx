import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { StickyNote, ArrowUpRight } from 'lucide-react';
import { noteData } from '../data/demo';
import { Badge, PageHeading } from '../ui/primitives';
export function Notes() {
  const { t } = useTranslation();
  const [selected, setSelected] = useState('math');
  const note = noteData.find((note) => note.id === selected)!;
  return (
    <>
      <PageHeading title={t('notes')} description={t('notesIntro')} />
      <div className="notes-layout">
        <nav className="notes-list" aria-label={t('notes')}>
          {noteData.map((note) => (
            <button
              key={note.id}
              onClick={() => setSelected(note.id)}
              aria-current={selected === note.id ? 'true' : undefined}
            >
              <StickyNote size={18} aria-hidden="true" />
              <span>
                <strong>{t(note.title)}</strong>
                <small>{t(note.id)}</small>
              </span>
            </button>
          ))}
        </nav>
        <article className="note-paper">
          <div className="note-meta">
            <Badge>{t(selected)}</Badge>
            <span className="small-label">{t('sample')}</span>
          </div>
          <h2>{t(note.title)}</h2>
          <p className="note-lead">{t('noteLead')}</p>
          <hr />
          <h3>{t('coreIdea')}</h3>
          <p>{t(note.body)}</p>
          <h3>{t('ownExample')}</h3>
          <blockquote>{t(note.example)}</blockquote>
          <h3>{t('nextQuestion')}</h3>
          <a className="text-link" href="#/assistant">
            {t(selected === 'math' ? 'prompt' : 'promptTwo')}
            <ArrowUpRight size={16} aria-hidden="true" />
          </a>
          <p className="notice">{t('editorFuture')}</p>
        </article>
      </div>
    </>
  );
}
