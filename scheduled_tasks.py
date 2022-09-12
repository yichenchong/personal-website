from flask_apscheduler import APScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask_mail import Mail
from secret_config import postgres_user, postgres_pw

import urllib.parse


class TmPersist:
    persist_store = None

    def __init__(self, app):
        self.app = app
        self.scheduler = APScheduler()
        postgres_auth = f"{urllib.parse.quote_plus(postgres_user)}:{urllib.parse.quote_plus(postgres_pw)}"
        self.jobstores = {
            'default': SQLAlchemyJobStore(
                url=f"postgresql+psycopg2://{postgres_auth}@127.0.0.1:5432/yichench_jobstore"
            )
        }
        self.executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(3)
        }


class TaskManager:

    def __init__(self):
        # configs
        self.mail = Mail(TmPersist.persist_store.app)
        self.contact_form_tasks = 0
    
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['mail']
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.mail = Mail(TmPersist.persist_store.app)
        self.jobstores = TmPersist.persist_store.jobstores

    def contact_form_email(self, name, email, subject, body):
        print("activate contact_form_email job...")
        recipients = ["yichenchong@yahoo.com", "noreply@yichenchong.com"]
        if body == "":
            recipients = ["noreply@yichenchong.com"]
        body = f"""{body}\n\nSent by {name}, {email}"""

        print("Sending email:", subject, body)
        with TmPersist.persist_store.app.app_context():
            self.mail.send_message(
                body=body,
                subject=f"Webform email: {subject}",
                sender=("Portfolio Website", "noreply@yichenchong.com"),
                recipients=recipients
            )
        self.contact_form_tasks -= 1
        print("Sent email:", subject)