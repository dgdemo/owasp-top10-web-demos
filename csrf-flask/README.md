# CSRF Demo (Cross-Site Request Forgery)

This demo shows:

- A vulnerable “transfer funds” endpoint that trusts only a cookie-based session.
- A malicious third-party page that silently triggers a POST using the victim's cookies.
- A fixed implementation that uses an anti-forgery (CSRF) token stored in the session
  and embedded in a hidden form field.

## How to run

Vulnerable app:

```bash
cd csrf
python csrf_vuln_app.py
# visit http://localhost:5002/ in your browser
```

Fixed app:

```bash
cd csrf
python csrf_fixed_app.py
# visit http://localhost:5002/ in your browser
```

## Attack page:

Log into the vulnerable app by visiting http://localhost:5002/.

With that tab still logged in, open csrf_attack_example.html directly
in your browser (e.g., drag-drop the file or use file:///).

Observe that the transfer completes without any interaction on the vulnerable app.

Then repeat the same with the fixed app and note that the forged request fails
because it does not include a valid CSRF token.


<details>
<summary>
Why CSRF Still Matters (Even in 2025/2026)
</summary>
Cross-Site Request Forgery (CSRF) is less visible today than it was a decade ago, but it remains a real-world issue—especially in applications that rely on cookie-based sessions or use server-rendered forms.

Modern browser features like SameSite cookies reduced many classic CSRF attack paths, and SPA architectures often authenticate using Bearer tokens rather than automatic cookies. However, large portions of the web still rely on traditional session cookies, and many internal tools, admin panels, and enterprise applications continue to be vulnerable.

Recent publicly disclosed CSRF vulnerabilities (2023–2025) have affected major platforms such as Atlassian, Jenkins, VMware appliances, various Cisco web interfaces, and numerous WordPress plugins. IoT and network devices (routers, NAS systems, IP cameras) continue to expose CSRF-prone admin panels that automatically trust browser cookies.

In other words: CSRF is less common, but far from obsolete.
Any application that accepts state-changing requests using a session cookie can still be coerced into performing unintended actions unless it implements proper controls—typically anti-forgery tokens, SameSite cookie restrictions, or double-submit cookies.

This demo illustrates how CSRF works, why frameworks still defend against it, and how a simple anti-forgery token fully mitigates the attack.
</detaails>