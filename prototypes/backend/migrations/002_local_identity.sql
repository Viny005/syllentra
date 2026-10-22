-- Neue Identitätsprobe übernimmt kein altes Gerätevertrauen und keine alten Sitzungen.
ALTER TABLE accounts ALTER COLUMN kind SET DEFAULT 'user';
ALTER TABLE accounts ADD COLUMN security_epoch integer NOT NULL DEFAULT 0 CHECK (security_epoch >= 0);
ALTER TABLE accounts ADD COLUMN mfa_required boolean NOT NULL DEFAULT false;
ALTER TABLE devices ADD COLUMN expires_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE devices ADD COLUMN security_epoch integer NOT NULL DEFAULT 0;
ALTER TABLE sessions ADD COLUMN id uuid NOT NULL DEFAULT gen_random_uuid() UNIQUE;
ALTER TABLE sessions ADD COLUMN security_epoch integer NOT NULL DEFAULT 0;
UPDATE devices SET authorized = false;
UPDATE sessions SET revoked = true;
CREATE TABLE identity_challenges (
 id uuid PRIMARY KEY,
 account_id uuid NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
 purpose text NOT NULL CHECK (purpose IN ('email', 'device', 'recovery')),
 verifier text,
 binding_hash text NOT NULL CHECK (char_length(binding_hash) = 64),
 expires_at timestamptz NOT NULL,
 created_at timestamptz NOT NULL,
 last_sent_at timestamptz NOT NULL,
 attempts integer NOT NULL DEFAULT 0 CHECK (attempts BETWEEN 0 AND 5),
 sends integer NOT NULL DEFAULT 1 CHECK (sends BETWEEN 1 AND 3),
 consumed boolean NOT NULL DEFAULT false,
 approved boolean NOT NULL DEFAULT false,
 approved_by_device uuid,
 security_epoch integer NOT NULL,
 FOREIGN KEY (approved_by_device, account_id) REFERENCES devices(id, account_id) ON DELETE CASCADE
);
CREATE INDEX challenges_account ON identity_challenges(account_id, purpose);
CREATE TABLE recovery_codes (
 account_id uuid PRIMARY KEY REFERENCES accounts(id) ON DELETE CASCADE,
 verifier text NOT NULL,
 used boolean NOT NULL DEFAULT false
);
CREATE TABLE identity_budgets (
 scope_hash text PRIMARY KEY,
 expires_at timestamptz NOT NULL,
 attempts integer NOT NULL CHECK (attempts > 0)
);
CREATE TABLE security_events (
 id uuid PRIMARY KEY,
 account_id uuid REFERENCES accounts(id) ON DELETE CASCADE,
 event text NOT NULL CHECK (event IN ('register', 'email_verified', 'login_ok', 'login_denied',
 'otp_denied', 'otp_resent', 'device_requested', 'device_approved', 'device_revoked',
 'session_revoked', 'recovery_requested', 'recovery_denied', 'recovered')),
 occurred_at timestamptz NOT NULL
);
CREATE INDEX security_events_account ON security_events(account_id, occurred_at);
