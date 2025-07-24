#!/bin/bash
# Start Prometheus in background
./prometheus/prometheus --config.file=prometheus/prometheus.yml --storage.tsdb.path=prometheus-data &

# Start your Flask app
python3 scripts/monitor.py
