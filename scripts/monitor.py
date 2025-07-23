#!/usr/bin/env python3

import requests
import time
from datetime import datetime

# List of URLs to monitor
URLS = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://thiswebsitedoesnotexist.zx",  # for testing failure
]

def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        response_time = round(time.time() - start_time, 3)

        status = response.status_code
        status_text = "UP" if status == 200 else f"ERROR {status}"
    except requests.RequestException as e:
        response_time = 0
        status_text = f"DOWN - {str(e)}"
    
    log_status(url, status_text, response_time)

def log_status(url, status, response_time):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {url} - {status} - {response_time}s"
    print(log_line)
    
    with open("monitor_log.txt", "a") as log_file:
        log_file.write(log_line + "\n")

if __name__ == "__main__":
    for url in URLS:
        check_url(url)
