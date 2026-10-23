CREATE TABLE accounts (
 id uuid PRIMARY KEY,
 login text UNIQUE NOT NULL CHECK (char_length(login) BETWEEN 1 AND 80),
 password_hash text NOT NULL,
 kind text NOT NULL CHECK (kind IN ('user', 'administrator')),
 verification text NOT NULL CHECK (verification IN ('pending', 'verified')),
 status text NOT NULL CHECK (status IN ('active', 'suspended', 'deleted'))
);
-- Keine Super-Admin-Erstbesetzung oder privilegierte Standardsitzung.
CREATE TABLE devices (
 id uuid PRIMARY KEY,
 account_id uuid NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
 proof_hash text UNIQUE NOT NULL CHECK (char_length(proof_hash) = 64),
 authorized boolean NOT NULL DEFAULT false,
 UNIQUE (id, account_id)
);
CREATE TABLE sessions (
 token_hash text PRIMARY KEY CHECK (char_length(token_hash) = 64),
 account_id uuid NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
 device_id uuid NOT NULL,
 expires_at timestamptz NOT NULL,
 revoked boolean NOT NULL DEFAULT false,
 FOREIGN KEY (device_id, account_id) REFERENCES devices(id, account_id) ON DELETE CASCADE
);
CREATE INDEX sessions_account ON sessions(account_id);
CREATE TABLE notes (
 id uuid PRIMARY KEY,
 account_id uuid NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
 title text NOT NULL CHECK (char_length(title) BETWEEN 1 AND 120),
 body text NOT NULL CHECK (char_length(body) <= 4000),
 deleted_at timestamptz
);
CREATE INDEX notes_account ON notes(account_id, id) WHERE deleted_at IS NULL;
CREATE TABLE capabilities (
 name text PRIMARY KEY,
 mode text NOT NULL CHECK (mode IN ('hidden', 'unavailable', 'available')),
 allowed_kind text NOT NULL CHECK (allowed_kind IN ('user', 'administrator'))
);
INSERT INTO capabilities VALUES ('notes', 'available', 'user'),
 ('assistant', 'unavailable', 'user'), ('administration', 'hidden', 'administrator');
