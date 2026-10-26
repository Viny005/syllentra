import { useEffect, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import type { FormEvent } from 'react';
import { PageHeading } from '../ui/primitives';
import { createIdentityClient, localEnabled, object } from '../lib/identityClient';

type Stage = 'login' | 'register' | 'verify' | 'recover' | 'recoveryProof' | 'device';
type Item = { id: string; revoked?: boolean; authorized?: boolean };

export function Identity() {
  const { t } = useTranslation();
  const [stage, setStage] = useState<Stage>('login');
  const [active, setActive] = useState(false);
  const [email, setEmail] = useState('');
  const [challenge, setChallenge] = useState('');
  const [message, setMessage] = useState('');
  const [busy, setBusy] = useState(false);
  const [sessions, setSessions] = useState<Item[]>([]);
  const [devices, setDevices] = useState<Item[]>([]);
  const [requests, setRequests] = useState<Item[]>([]);
  const confirmation = useRef<HTMLInputElement>(null);

  function clearAccount() {
    setActive(false);
    setSessions([]);
    setDevices([]);
    setRequests([]);
  }

  const clientRef = useRef<ReturnType<typeof createIdentityClient> | null>(null);
  if (!clientRef.current) {
    clientRef.current = createIdentityClient({
      isLocalEnabled: localEnabled,
      onUnauthorized: clearAccount,
    });
  }
  const call = clientRef.current.call;
  async function refresh() {
    const session = await call('/session');
    if (!object(session) || session.kind !== 'user' || session.assurance !== 'local-synthetic-otp')
      throw new Error('identityFailed');
    setActive(true);
    const readList = async (path: string) => {
      const data = await call(path);
      if (
        !Array.isArray(data) ||
        !data.every((v: unknown) => object(v) && typeof v.id === 'string')
      )
        throw new Error('identityFailed');
      return data as Item[];
    };
    setSessions(await readList('/sessions'));
    setDevices(await readList('/devices'));
    setRequests(await readList('/devices/requests'));
  }
  async function run(action: () => Promise<void>) {
    if (busy) return;
    setBusy(true);
    setMessage('');
    try {
      await action();
    } catch (error) {
      setMessage(
        error instanceof Error &&
          ['identityUnavailable', 'identityLimited', 'identityDisconnected'].includes(error.message)
          ? error.message
          : 'identityFailed',
      );
    } finally {
      setBusy(false);
    }
  }
  useEffect(() => {
    // Ausschließlich der ausdrücklich aufgerufene lokale Identitätsbereich kontaktiert die API.
    if (localEnabled()) void refresh().catch(() => clearAccount());
    // Einmalige Zustandsabfrage; Sprache/Theme dürfen keine neue Anmeldung auslösen.
  }, []);

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = event.currentTarget;
    const values = new FormData(form);
    const value = (name: string) => String(values.get(name) || '');
    const enteredEmail = value('email') || email;
    const password = value('password');
    const code = value('code');
    const recoveryCode = value('recovery_code');
    form.reset();
    void run(async () => {
      if (stage === 'register' || stage === 'recover') {
        const data = await call(
          stage === 'register' ? '/auth/register' : '/auth/recover',
          stage === 'register' ? { email: enteredEmail, password } : { email: enteredEmail },
        );
        if (!object(data) || typeof data.challenge_id !== 'string')
          throw new Error('identityFailed');
        setEmail(enteredEmail);
        setChallenge(data.challenge_id);
        setStage(stage === 'register' ? 'verify' : 'recoveryProof');
        setMessage('identityAccepted');
      } else if (stage === 'verify') {
        await call('/auth/verify', { challenge_id: challenge, code });
        setStage('login');
        setMessage('identityVerified');
      } else if (stage === 'recoveryProof') {
        await call('/auth/recover/complete', {
          challenge_id: challenge,
          code,
          recovery_code: recoveryCode,
          new_password: password,
        });
        clearAccount();
        setStage('login');
        setMessage('identityRecovered');
      } else if (stage === 'login') {
        const data = await call('/auth/login', { login: enteredEmail, password });
        if (
          object(data) &&
          data.status === 'device_verification_required' &&
          typeof data.challenge_id === 'string'
        ) {
          setChallenge(data.challenge_id);
          setEmail(enteredEmail);
          setStage('device');
          setMessage('identityDeviceHelp');
        } else {
          await refresh();
          setMessage('identityConnected');
        }
      }
    });
  }
  const needsEmail = ['login', 'register', 'recover'].includes(stage);
  const needsPassword = ['login', 'register', 'recoveryProof'].includes(stage);
  const needsOtp = ['verify', 'recoveryProof'].includes(stage);
  return (
    <>
      <PageHeading title={t('identityTitle')} description={t('identityBoundary')} />
      <section className="identity-panel" aria-label={t('identityTitle')}>
        <p className="eyebrow">{t(active ? 'identityConnected' : 'identityDisconnected')}</p>
        <p>{t('identitySynthetic')}</p>
        {!localEnabled() && <p role="status">{t('identityUnavailable')}</p>}
        {message && (
          <p role="status" aria-live="polite">
            {t(message)}
          </p>
        )}
        {!active ? (
          <>
            <div className="identity-actions">
              {(['login', 'register', 'recover'] as const).map((item) => (
                <button
                  key={item}
                  className="button secondary"
                  type="button"
                  disabled={busy}
                  onClick={() => {
                    setStage(item);
                    setMessage('');
                    setChallenge('');
                  }}
                >
                  {t(`identity_${item}`)}
                </button>
              ))}
            </div>
            <h2>{t(`identity_${stage}`)}</h2>
            {stage === 'device' ? (
              <>
                <p>{t('identityDeviceHelp')}</p>
                <p className="identity-reference">
                  {t('identityDeviceReference', { reference: challenge })}
                </p>
                <button
                  className="button primary"
                  disabled={busy || !localEnabled()}
                  onClick={() =>
                    void run(async () => {
                      await call('/auth/device/complete', { challenge_id: challenge });
                      setStage('login');
                      setMessage('identityVerified');
                    })
                  }
                >
                  {t('identityCheckDevice')}
                </button>
              </>
            ) : (
              <form onSubmit={submit} className="identity-form">
                {needsEmail && (
                  <label>
                    {t('identityEmail')}
                    <input
                      name="email"
                      type="email"
                      autoComplete="username"
                      defaultValue={email}
                      required
                      maxLength={100}
                      placeholder="student@example.test"
                    />
                  </label>
                )}
                {needsPassword && (
                  <label>
                    {t(stage === 'recoveryProof' ? 'identityNewPassword' : 'identityPassword')}
                    <input
                      name="password"
                      type="password"
                      autoComplete={stage === 'login' ? 'current-password' : 'new-password'}
                      required
                      minLength={12}
                      maxLength={256}
                    />
                  </label>
                )}
                {needsOtp && (
                  <label>
                    {t('identityOtp')}
                    <input
                      name="code"
                      type="password"
                      inputMode="numeric"
                      autoComplete="off"
                      required
                      minLength={8}
                      maxLength={8}
                      pattern="[0-9]{8}"
                    />
                  </label>
                )}
                {stage === 'recoveryProof' && (
                  <label>
                    {t('identityRecoveryCode')}
                    <input
                      name="recovery_code"
                      type="password"
                      autoComplete="off"
                      required
                      minLength={32}
                      maxLength={128}
                    />
                  </label>
                )}
                <button className="button primary" disabled={busy || !localEnabled()}>
                  {t(busy ? 'identityWorking' : 'identitySubmit')}
                </button>
              </form>
            )}
            {needsOtp && (
              <button
                className="button secondary"
                disabled={busy}
                onClick={() =>
                  void run(async () => {
                    await call('/auth/resend', { challenge_id: challenge });
                    setMessage('identityAccepted');
                  })
                }
              >
                {t('identityResend')}
              </button>
            )}
          </>
        ) : (
          <>
            <div className="identity-actions">
              <button className="button primary" disabled={busy} onClick={() => void run(refresh)}>
                {t('identityRefresh')}
              </button>
              <button
                className="button secondary"
                disabled={busy}
                onClick={() =>
                  void run(async () => {
                    await call('/auth/logout', {});
                    clearAccount();
                    setMessage('identityDisconnected');
                  })
                }
              >
                {t('identityLogout')}
              </button>
            </div>
            <label>
              {t('identityConfirmPassword')}
              <input
                ref={confirmation}
                type="password"
                autoComplete="current-password"
                maxLength={256}
              />
            </label>
            <h2>{t('identityRequests')}</h2>
            {!requests.length && <p>{t('identityNoRequests')}</p>}
            {requests.map((item, index) => (
              <div key={item.id}>
                <p className="identity-reference">
                  {t('identityDeviceReference', { reference: item.id })}
                </p>
                <button
                  className="button secondary"
                  disabled={busy}
                  onClick={() => {
                    const password = confirmation.current?.value || '';
                    if (confirmation.current) confirmation.current.value = '';
                    void run(async () => {
                      await call(`/devices/requests/${item.id}/approve`, { password });
                      await refresh();
                    });
                  }}
                >
                  {t('identityApprove', { number: index + 1 })}
                </button>
              </div>
            ))}
            <h2>{t('identitySessions')}</h2>
            {sessions
              .filter((item) => !item.revoked)
              .map((item, index) => (
                <button
                  className="button secondary"
                  key={item.id}
                  disabled={busy}
                  onClick={() =>
                    void run(async () => {
                      await call(`/sessions/${item.id}/revoke`, {});
                      await refresh();
                    })
                  }
                >
                  {t('identityRevokeSession', { number: index + 1 })}
                </button>
              ))}
            <h2>{t('identityDevices')}</h2>
            {devices
              .filter((item) => item.authorized)
              .map((item, index) => (
                <button
                  className="button secondary"
                  key={item.id}
                  disabled={busy}
                  onClick={() => {
                    const password = confirmation.current?.value || '';
                    if (confirmation.current) confirmation.current.value = '';
                    void run(async () => {
                      await call(`/devices/${item.id}/revoke`, { password });
                      await refresh();
                    });
                  }}
                >
                  {t('identityRevokeDevice', { number: index + 1 })}
                </button>
              ))}
          </>
        )}
        <p className="muted">{t('identityMfaBlocked')}</p>
        <a className="button secondary" href="#/">
          {t('identityBackDemo')}
        </a>
      </section>
    </>
  );
}
