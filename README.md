# OWASP Top 10 Web Demos

A collection of small, self-contained web application vulnerability demos focused on the **OWASP Top 10**.  
Each vulnerability lives in its own folder with:

- A vulnerable implementation
- A fixed/secure version
- A walkthrough-style README

## Current Demos

### 1. Reflected XSS (Flask)
Folder: `xss-reflected-flask/`  
Shows how a simple template change (`|safe`) introduces reflected XSS, and how autoescaping fixes it.

## Goals

- Help developers understand the *cause* of common vulnerabilities  
- Provide runnable code that’s easy to experiment with  
- Keep each demo lightweight and Python-first

## Upcoming Demos

- SQL Injection
- CSRF
- Template Injection
- Insecure Direct Object Reference
- Open Redirects
- And more…

---

Each demo is intentionally very small and ideal for reading, modifying, and breaking on purpose.
