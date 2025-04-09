
# 🔐 Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅                 |
| < 1.0   | ❌                 |

## 📢 Reporting a Vulnerability

If you discover a security vulnerability, please contact us via:

- Email: robshubert96@gmail.com
- GPG Key: Available upon request

We will respond within **24 hours** and coordinate a private fix.

## 🛡️ Hardening Tips

- Always run behind a Cloudflare Zero Trust Tunnel
- Use GPG to encrypt sensitive logs and sensor data
- Regularly update dependencies via `pip install --upgrade -r requirements.txt`
- Enable container security scanning via Trivy
