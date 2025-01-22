import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
import json

from family_reminders.credit_card_payment_alert import cc_alert
from general_alert import check_general_schedule
from housework_alert import today_task
from mortgage_payment_alert import mortgage_alert
from rent_collection_alert import rent_collection_alert
# Email credentials and settings
with open('email.json', 'r') as f:
    email_data = json.load(f)

smtp_server = email_data["smtp_server"]
smtp_port = email_data["smtp_port"]
sender_email = email_data["sender_email"]
sender_password = email_data["sender_password"]
recipient_email = email_data["recipient_email"]

SUBJECT = "Daily Reminder Alert " + str(datetime.date.today())


def send_email(subject, body):
    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def create_daily_email():
    # Create the body of the email
    print(today_task())
    print(rent_collection_alert())
    tasks = "\n".join([today_task(), rent_collection_alert(), cc_alert(), mortgage_alert(), check_general_schedule()])
    body = f"Hello! Here are your alerts for today:\n\n{tasks}\n\nStay productive!"
    send_email(SUBJECT, body)

if __name__ == "__main__":
    create_daily_email()