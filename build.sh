
#!/bin/bash
set -e

echo "[+] Creating virtual environment..."
python3 -m venv build_env
source build_env/bin/activate
pip install --upgrade pip setuptools wheel pyinstaller

echo "[+] Installing dependencies..."
pip install -r requirements.txt

echo "[+] Building .deb package..."
fpm -s python -t deb -n iot-env-monitoring -v 1.0.0 .

echo "[+] Building .AppImage (stub - configure further)..."
# Placeholder for AppImage creation using appimagetool

echo "[+] Building Windows .exe..."
pyinstaller --onefile cli.py --name iot_env_monitoring.exe

echo "[✓] All builds complete."
