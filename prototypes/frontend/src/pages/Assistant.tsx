import { useEffect, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { ArrowUp, Plus, MessageSquare, Sparkles, Square, Paperclip } from 'lucide-react';
import type { FormEvent } from 'react';
import { Badge, PageHeading } from '../ui/primitives';
import type { Language } from '../lib/preferences';
type Message = { id: number; role: 'user' | 'assistant'; text: string; language: Language };
export function Assistant({ language }: { language: Language }) {
  const { t, i18n } = useTranslation();
  const [thread, setThread] = useState('new');
  const [messages, setMessages] = useState<Record<string, Message[]>>({
    new: [],
    example: [
      { id: 0, role: 'user', text: 'prompt', language: 'de' },
      { id: 1, role: 'assistant', text: 'demoReply', language: 'de' },
    ],
  });
  const [draft, setDraft] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState(false);
  const [stopped, setStopped] = useState(false);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const counter = useRef(10);
  const input = useRef<HTMLTextAreaElement>(null);
  useEffect(
    () => () => {
      if (timer.current) clearTimeout(timer.current);
    },
    [],
  );
  function send(event: FormEvent) {
    event.preventDefault();
    const text = draft.trim();
    if (!text || text.length > 500) {
      setError(true);
      return;
    }
    setError(false);
    setStopped(false);
    const user: Message = { id: counter.current++, role: 'user', text, language };
    setMessages((previous) => ({ ...previous, [thread]: [...previous[thread], user] }));
    setDraft('');
    setBusy(true);
    // Deterministische lokale Simulation; keine Netzwerk- oder Modellanfrage.
    timer.current = setTimeout(() => {
      const response: Message = {
        id: counter.current++,
        role: 'assistant',
        text: i18n.getFixedT(language)('demoReply'),
        language,
      };
      setMessages((previous) => ({ ...previous, [thread]: [...previous[thread], response] }));
      setBusy(false);
      timer.current = null;
    }, 650);
  }
  function stop() {
    if (timer.current) clearTimeout(timer.current);
    timer.current = null;
    setBusy(false);
    setStopped(true);
    input.current?.focus();
  }
  function choose(id: string) {
    if (busy) stop();
    setThread(id);
    setDraft('');
    setError(false);
    setStopped(false);
  }
  return (
    <>
      <PageHeading title={t('assistant')} description={t('assistantIntro')} />
      <p className="chat-notice">
        <span className="tiny-dot" />
        {t('chatNotice')}
      </p>
      <div className="chat-layout">
        <aside className="conversation-list">
          <button
            className="button secondary"
            onClick={() => {
              choose('new');
              input.current?.focus();
            }}
          >
            <Plus size={18} aria-hidden="true" />
            {t('newChat')}
          </button>
          <p className="eyebrow">{t('conversations')}</p>
          <button
            className={thread === 'example' ? 'current-conversation' : ''}
            onClick={() => choose('example')}
          >
            <MessageSquare size={17} aria-hidden="true" />
            {t('mathTopic')}
          </button>
          <p className="muted">{t('localOnly')}</p>
        </aside>
        <section className="chat-panel" aria-label={t('conversations')}>
          <div className="chat-messages">
            {messages[thread].length === 0 ? (
              <div className="chat-welcome">
                <span className="tutor-symbol">
                  <Sparkles size={28} aria-hidden="true" />
                </span>
                <h2>{t('chatWelcome')}</h2>
                <p>{t('chatWelcomeBody')}</p>
                <div className="prompt-list">
                  {['prompt', 'promptTwo'].map((key) => (
                    <button
                      key={key}
                      onClick={() => {
                        setDraft(t(key));
                        input.current?.focus();
                      }}
                    >
                      {t(key)}
                      <ArrowUp size={16} aria-hidden="true" />
                    </button>
                  ))}
                </div>
              </div>
            ) : (
              messages[thread].map((message) => (
                <article className={`chat-message ${message.role}`} key={message.id}>
                  <p className="message-author">
                    {t(message.role === 'user' ? 'you' : 'companion')}
                  </p>
                  <p
                    className="message-content"
                    lang={thread === 'example' && message.id < 2 ? language : message.language}
                  >
                    {thread === 'example' && message.id < 2 ? t(message.text) : message.text}
                  </p>
                  {message.role === 'assistant' && (
                    <a href="#/library" className="citation">
                      {t('sampleSource')}
                    </a>
                  )}
                </article>
              ))
            )}
            <div role="status" aria-live="polite" className="chat-status">
              {busy ? t('simulating') : stopped ? t('stopped') : ''}
            </div>
          </div>
          <form className="composer" onSubmit={send}>
            <label className="sr-only" htmlFor="chat-message">
              {t('message')}
            </label>
            <textarea
              ref={input}
              id="chat-message"
              maxLength={500}
              rows={2}
              value={draft}
              placeholder={t('messagePlaceholder')}
              aria-invalid={error || undefined}
              aria-describedby={error ? 'message-error' : 'attachment-note'}
              onChange={(event) => {
                setDraft(event.target.value);
                setError(false);
              }}
            />
            <div className="composer-bottom">
              <Badge>{t('demoShort')}</Badge>
              {busy ? (
                <button type="button" className="send-button" aria-label={t('stop')} onClick={stop}>
                  <Square size={18} aria-hidden="true" />
                </button>
              ) : (
                <button type="submit" className="send-button" aria-label={t('send')}>
                  <ArrowUp size={20} aria-hidden="true" />
                </button>
              )}
            </div>
            {error && (
              <p className="error-message" role="alert" id="message-error">
                {t('messageError')}
              </p>
            )}
          </form>
          <p id="attachment-note" className="attachment-note">
            <Paperclip size={14} aria-hidden="true" />
            {t('attachments')}
          </p>
        </section>
      </div>
    </>
  );
}
