import time
import os
import threading
import requests
import datetime
import smtplib
from email.mime.text import MIMEText
from flask import Flask, jsonify, render_template
from prometheus_client import start_http_server, Gauge

# List of websites to monitor
WEBSITES = [
    "https://google.com",
    "https://github.com",
    "https://thiswebsitedoesnotexist.zx"
]

# Email alert config
ALERT_EMAIL = "Rachealsililo11@gmail.com"  # recipient
SENDER_EMAIL = "Rachealsililo11@gmail.com"  # sender
SENDER_PASSWORD = "wahgitkrwhxwqqar"  # app-specific password

# Dictionary to store status
website_status = {}
previous_status = {}

# Prometheus metric
UPTIME_GAUGE = Gauge("website_up", "Website availability (1 = UP, 0 = DOWN)", ["url"])

# Flask app
app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", website_data=website_status)

@app.route("/data")
def api_status():
    data = []
    for url, info in website_status.items():
        data.append({
            "url": url,
            "status": info["status"],
            "response_time": info["response_time"],
            "last_checked": info["last_checked"]
        })
    return jsonify(data)

# Email alert function
def send_email_alert(url):
    subject = f"🚨 UptimePal Alert: {url} is DOWN!"
    body = f"The website {url} is DOWN as of {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ALERT_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, ALERT_EMAIL, msg.as_string())
        print(f"[EMAIL SENT] Alert for {url}")
    except Exception as e:
        print(f"[EMAIL FAILED] Could not send alert for {url}: {e}")

# Monitoring function
def monitor_websites():
    while True:
        for url in WEBSITES:
            try:
                start = time.time()
                response = requests.get(url, timeout=5)
                status = "UP" if response.status_code == 200 else "DOWN"
                response_time = round(time.time() - start, 2)
            except requests.RequestException:
                status = "DOWN"
                response_time = "N/A"

            # Send alert only if status changed to DOWN
            if previous_status.get(url) != status:
                if status == "DOWN":
                    send_email_alert(url)
                previous_status[url] = status

            website_status[url] = {
                "status": status,
                "response_time": response_time,
                "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Update Prometheus metric
            UPTIME_GAUGE.labels(url=url).set(1 if status == "UP" else 0)

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    # Start Prometheus metrics on port 9100 (change if needed)
    start_http_server(9100)

    # Start monitoring in background
    threading.Thread(target=monitor_websites, daemon=True).start()

    # Start Flask server    
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=False)

