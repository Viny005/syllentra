import { useState } from 'react';
import type { FormEvent } from 'react';
import { useTranslation } from 'react-i18next';
import { modules } from '../data/demo';
import type { ModuleId, StudyEvent } from '../data/demo';
import { validSession } from '../lib/calendar';
export function SessionForm({ onSave }: { onSave: (event: StudyEvent) => void }) {
  const { t } = useTranslation();
  const [error, setError] = useState(false);
  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const title = String(data.get('title') || '').trim();
    const module = String(data.get('module'));
    const date = String(data.get('date'));
    const time = String(data.get('time'));
    if (!validSession(title, module, date, time)) {
      setError(true);
      return;
    }
    onSave({
      id: crypto.randomUUID(),
      title,
      translated: false,
      module: module as ModuleId,
      date,
      time,
      kind: 'session',
      local: true,
    });
  }
  return (
    <form onSubmit={submit} noValidate className="form-stack">
      <p className="muted">{t('fiction')}</p>
      <label>
        {t('sessionTitle')}
        <input
          autoFocus
          name="title"
          maxLength={80}
          placeholder={t('sessionPlaceholder')}
          aria-invalid={error || undefined}
          aria-describedby={error ? 'session-error' : undefined}
        />
      </label>
      <label>
        {t('courses')}
        <select name="module">
          {modules.map((module) => (
            <option value={module.id} key={module.id}>
              {t(module.id)}
            </option>
          ))}
        </select>
      </label>
      <div className="form-row">
        <label>
          {t('date')}
          <input
            name="date"
            type="date"
            defaultValue="2026-10-22"
            min="2020-01-01"
            max="2099-12-31"
          />
        </label>
        <label>
          {t('time')}
          <input name="time" type="time" defaultValue="16:00" />
        </label>
      </div>
      {error && (
        <p id="session-error" className="error-message" role="alert">
          {t('sessionError')}
        </p>
      )}
      <button type="submit" className="button primary">
        {t('saveSession')}
      </button>
    </form>
  );
}
