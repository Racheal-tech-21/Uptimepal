import requests

def send_slack_alert(site, error_msg):
    webhook_url = "https://hooks.slack.com/services/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"
    message = {
        "text": f":warning: ALERT: {site} is DOWN.\n\nError: {error_msg}"
    }

    try:
        response = requests.post(webhook_url, json=message)
        if response.status_code != 200:
            print(f"Failed to send Slack alert: {response.text}")
    except Exception as e:
        print(f"Error sending Slack alert: {str(e)}")

