#!/bin/bash

# Gracefully kill any running Prometheus
pkill -15 prometheus 2>/dev/null

# Start Prometheus in background safely
~/uptimepal/prometheus/prometheus \
  --config.file=$HOME/uptimepal/prometheus/prometheus.yml \
  --storage.tsdb.path=$HOME/uptimepal/prometheus/data \
  --web.listen-address=":8000" > ~/uptimepal/prometheus/prometheus.log 2>&1 &
