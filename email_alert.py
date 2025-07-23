import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(site, error_msg):
    sender = "Rachealsililo11@gmail.com"
    receiver = "Rachealsililo11@gmail.com"
    password = "wahgitkrwhxwqqar"  # 16-character app password

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"ALERT: {site} is DOWN"
    msg["From"] = sender
    msg["To"] = receiver

    body = f"⚠️ The website {site} is DOWN.\n\nError: {error_msg}"
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print(f"Email alert sent for {site}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")
