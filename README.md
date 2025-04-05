
# IoT and Satellite-Enabled Environmental Monitoring System 🌍🛰️

A cross-platform, field-ready system for collecting, analyzing, and visualizing environmental data using a hybrid of IoT sensors and satellite telemetry. Built for researchers, security ops, and environmental intelligence.

---

## 🚀 Features

- 🌐 Satellite + IoT Sensor Data Integration
- 📊 Real-Time Dashboard Interface
- 📦 Multi-Platform Support (.deb, .exe, .AppImage)
- 🔐 Secure GPG/Cloudflare Integration
- ⚙️ Offline & Airgap Support
- 🧪 Full CI/CD Pipeline with Pytest + GitHub Actions
- 🧠 Built-in AI Recon Tools (Pluggable)

---

## 📁 File Structure

```
.
├── dashboard/              # Dashboard UI (HTML/CSS/JS)
├── src/                    # Core Python backend
├── tests/                  # Full unit tests (pytest)
├── Dockerfile              # Production Docker build
├── docker-compose.yml      # Multi-container setup
├── requirements.txt        # Python dependencies
├── example.proto           # Protocol Buffers format
├── .github/                # CI/CD workflows
```

---

## 💻 Installation

### 🐳 Docker (Recommended)

```bash
docker-compose up --build
```

### 🐧 Linux (.deb / .AppImage)

```bash
./build.sh
sudo dpkg -i dist/env-monitoring.deb
```

### 🪟 Windows (.exe)

Download the `.exe` from [Releases](https://github.com/rfc391/IoT-and-Satellite-Enabled-Environmental-Monitoring-System/releases)

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📊 Dashboard

Access via: `http://localhost:8080`

- Realtime metrics
- Device health
- Satellite overlays (coming soon)
- Alert system

---

## 🤝 Contributing

1. Fork this repo
2. Create a new branch (`feature/new-feature`)
3. Commit your changes
4. Push and open a PR

---

## 📜 License

MIT © [rfc391](https://github.com/rfc391)

---

## 🛡️ Security Policy

See [SECURITY.md](SECURITY.md)

---

## 📷 Demo

![Demo Dashboard](docs/demo.gif)

