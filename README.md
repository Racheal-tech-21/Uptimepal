# UptimePal 🔍

A **powerful**, Python-based website uptime monitoring tool built from scratch — featuring **real-time logging, email alerts, scheduling via cron, Docker deployment,** and **full Prometheus & Grafana integration** for professional-grade monitoring and visualization.

## 🚀 Features
- ✅ Real-time website uptime and response speed monitoring  
- 📧 Instant email alerts for downtime to keep you proactive  
- 📓 Detailed logging of every check in `monitor_log.txt`  
- 🕒 Automated checks every 5 minutes via cron scheduling  
- 🐳 Fully Dockerized for smooth, consistent deployment anywhere  
- 📊 **Seamless Prometheus metrics exposure and Grafana dashboards** for visual insight and trend analysis — **production-ready!**

## 🛠️ How It Works
`monitor.py` continuously monitors your list of websites, logs their status and response times, exposes Prometheus-compatible metrics, and triggers email alerts for any downtime—**empowering you with actionable data** and **professional observability tools** like Grafana.

## 📁 Project Structure
uptimepal/
├── monitor.py # Core monitoring and metrics export
├── email_alert.py # Email alert module
├── monitor_log.txt # Persistent uptime logs
├── Dockerfile # Container configuration for deployment
├── requirements.txt # Dependencies
└── scripts/
└── cron.sh # Cron job setup script

## 🧰 Tech Stack & Tools
- Python 3  
- Requests, smtplib, email libraries  
- Gmail SMTP for secure alerting  
- Cron for scheduling  
- Docker for containerization  
- **Prometheus for metrics scraping**  
- **Grafana for live dashboard visualization**

## 📊 Grafana Integration (Job-Winning Highlight)
- Exposes `/metrics` endpoint with Prometheus-formatted data  
- Built custom Grafana dashboards to visualize uptime trends, response times, and real-time statuses  
- Enables quick identification of failures and performance issues through actionable charts and alerts  
- Ready for **production deployment on cloud platforms** (AWS, Render, etc.)

## 🐳 Docker Deployment
Build:
```bash
docker build -t uptimepal .
docker run --name uptimepal-container uptimepal
 Cron Setup
Automate monitoring every 5 minutes with:
*/5 * * * * /usr/bin/python3 /home/rachealsililo@rachealsililo/uptimepal/monitor.py >> /home/rachealsililo@rachealsililo/uptimepal/cron.log 2>&1

 Gmail App Password Setup
Enable 2-Step Verification on Gmail

Create a 16-character App Password

Configure email_alert.py with this password for secure email notifications

 Next-Level Plans
Add Slack/Telegram real-time alerts

Expand frontend UI for better UX

Deploy fully to cloud with automated scaling and failover
 About Me
Racheal Sililo  Ambitious Beginner DevOps Engineer, building real, production-grade projects with a relentless passion for success.
I don’t just learn I build, deploy, and monitor end-to-end systems ready for the real world.

⭐ Star this repo, check out the code, and see how I deliver value you can count on.



