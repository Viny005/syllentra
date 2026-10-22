ALTER TABLE recovery_codes ADD COLUMN expires_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE identity_challenges ADD COLUMN prior_verifiers text[] NOT NULL DEFAULT '{}';
