-- R1: Persönlicher Offline-Recoverycode läuft nicht mehr automatisch nach 7 Tagen ab;
-- bereits abgelaufene Altcodes werden widerrufen statt still reaktiviert.
ALTER TABLE recovery_codes ADD COLUMN revoked boolean NOT NULL DEFAULT false;
ALTER TABLE recovery_codes ADD COLUMN issued_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE recovery_codes ALTER COLUMN expires_at DROP NOT NULL;
ALTER TABLE recovery_codes ALTER COLUMN expires_at DROP DEFAULT;
UPDATE recovery_codes SET revoked = true WHERE expires_at IS NOT NULL AND expires_at <= CURRENT_TIMESTAMP;
UPDATE recovery_codes SET expires_at = NULL WHERE NOT revoked AND NOT used;

-- R4: Serverseitiger Startzeitpunkt für unverifizierte pending-Konten (24h-Frist).
ALTER TABLE accounts ADD COLUMN pending_since timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Erweiterte Sicherheitsereignisse für R1-Widerruf und R4-Pending-Reset.
ALTER TABLE security_events DROP CONSTRAINT security_events_event_check;
ALTER TABLE security_events ADD CONSTRAINT security_events_event_check CHECK (
 event IN (
  'register', 'pending_reset', 'pending_reset_blocked', 'email_verified',
  'login_ok', 'login_denied', 'otp_denied', 'otp_resent',
  'device_requested', 'device_approved', 'device_revoked', 'session_revoked',
  'recovery_requested', 'recovery_denied', 'recovered', 'recovery_code_revoked'
 )
);
