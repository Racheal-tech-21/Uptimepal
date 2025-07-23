#!/bin/bash

echo "[+] Stopping any existing Prometheus..."
pkill -f "prometheus" || true

echo "[+] Stopping any existing monitor.py..."
pkill -f "monitor.py" || true

# echo "[+] Starting Prometheus in background..."
# ./prometheus/prometheus --config.file=prometheus/prometheus.yml &

echo "[+] Starting monitor.py..."
python3 monitor.py
