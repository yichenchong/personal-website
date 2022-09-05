from flask_apscheduler import APScheduler
from flask_mail import Mail, Message, email_dispatched
import ssl, smtplib, secret_config

class TaskManager:

    def __init__(self, app):
        self.scheduler = APScheduler()
        self.app = app
        self.mail = Mail(app)
        self.contact_form_tasks = 0

    def contact_form_email(self, name, email, subject, body):
        print("activate contact_form_email job...")
        recipients = ["yichenchong@yahoo.com", "noreply@yichenchong.com"]
        if body == "":
            recipients = ["noreply@yichenchong.com"]
        body = f"""{body}\n\nSent by {name}, {email}"""

        print("Sending email:", subject, body)
        with self.app.app_context():
            self.mail.send_message(
                body=body,
                subject=f"Webform email: {subject}",
                sender=("Portfolio Website", "noreply@yichenchong.com"),
                recipients=recipients
            )
        self.contact_form_tasks -= 1
        print("Sent email:", subject)