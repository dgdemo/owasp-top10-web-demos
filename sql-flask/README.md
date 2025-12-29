# SQL Injection Demo (Flask)

This demo shows:
- How SQL Injection (SQLi) works in a simple Flask application and how to fix it using parameterized queries.

- It is intentionally minimal and educational, designed to clearly demonstrate the vulnerability, exploitation, and remediation.

- A vulnerable login endpoint that builds SQL queries using string concatenation.

- How an attacker can bypass authentication using a classic SQL injection payload.

- A fixed implementation that uses parameterized (prepared) SQL queries.


## Vulnerable Version

- User input is directly concatenated into an SQL query.

- The database treats attacker input as executable SQL.

- Authentication can be bypassed with a crafted payload.

### Example vulnerable query:

`
SELECT * FROM users
WHERE username = 'admin' AND password = '' OR 1=1--'
`

### Fixed Version

- Uses parameterized queries (? placeholders).

- User input is treated strictly as data, not SQL.

- Injection payloads are rendered harmless.

**Example fixed query:**

`
SELECT * FROM users WHERE username = ? AND password = ?
`

## How to run

From the sqli-flask directory:

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then visit:

- **Vulnerable login:**

http://localhost:5000/login-vuln

- **Fixed login:**

http://localhost:5000/login-fixed

---

## Example attack payload

Use this payload on the **vulnerable login form**:

- **Username**: admin

- **Password**:
' OR 1=1--


**Result**:

- Authentication succeeds without knowing the password.

- Multiple user rows may be returned.

- The executed SQL query is displayed in the UI.

The same payload **fails** on the fixed version.


# Why SQL injection remains a critical issue (OWASP A03: Injection).

- SQL injection remains one of the most common and severe web vulnerabilities.

- Modern frameworks do not automatically prevent SQLi if developers misuse database APIs.

- Injection flaws frequently lead to:

    - Authentication bypass

    - Data exfiltration

    - Privilege escalation

    - Full database compromise

## Notes

- This demo uses SQLite for simplicity.

- The database is recreated on app startup to keep behavior predictable.

- This project is for **educational purposes** only.
