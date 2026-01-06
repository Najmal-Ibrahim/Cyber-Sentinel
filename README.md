# 🛡️ Cyber-Sentinel: AI Powered Static Analysis Tool (SAST)

**Cyber-Sentinel** is an autonomous security auditor that scans Python codebases for OWASP Top 10 vulnerabilities. It uses Large Language Models (Llama-3-70b) to not only detect flaws but provide production-ready patches.

## 🚀 Features
- **Deep Logic Analysis:** Detects vulnerabilities that regex scanners miss (e.g., Logic flaws).
- **Auto-Patching:** Generates secure code snippets (e.g., converting f-strings to Parameterized Queries).
- **Vulnerabilities Covered:** SQL Injection, Hardcoded Secrets, Command Injection, Insecure Deserialization.

## 🛠️ Tech Stack
- **Engine:** Python 3.11
- **Brain:** Llama-3-70b via Groq API
- **Framework:** LangChain

## 📸 Demo
![Cyber Sentinel Scan Output](cyber_sentinel_output.png)