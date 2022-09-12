import helper.resume_loader.res_loader as rl
from blueprints.projects.project_blueprint import project as projects
from data.layer_one.io.cache import LayerOneCaches
from scheduled_tasks import TaskManager, TmPersist
import secret_config

from flask import Flask, render_template, request
import flask_cors

import re
import datetime

print(f"===starting web server at {datetime.datetime.now()}===")

# application stuff
app = Flask(__name__)
application = app
TmPersist.persist_store = TmPersist(app)
task_manager = TaskManager(app)

# application config
class SchedConfig:
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = TmPersist.persist_store.jobstores
    SCHEDULER_EXECUTORS = TmPersist.persist_store.executors
    MAIL_SERVER = secret_config.current_mail_config['server']
    MAIL_PORT = secret_config.current_mail_config['port']
    MAIL_USERNAME = secret_config.current_mail_config['username']
    MAIL_PASSWORD = secret_config.current_mail_config['password']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
app.config.from_object(SchedConfig())

# CORS stuff
flask_cors.CORS(app)

# scheduler
TmPersist.persist_store.scheduler.init_app(app)
TmPersist.persist_store.scheduler.start()
print("application and task manager initialized..")

# cache
LayerOneCaches.init_caches()
print("caches initialized..")

# blueprints
app.register_blueprint(projects)
print("blueprints registered..")


# app pages
@app.route('/')
def landing_page():
    return render_template('title-slide.html')


@app.route('/about/')
def about_page():
    print(LayerOneCaches.skills_cache)
    return render_template(
        'about-page.html',
        resume_doc=LayerOneCaches.resume_doc,
        skills=LayerOneCaches.skills_cache
    )


@app.route('/contact/', methods=['GET'])
def contact_page():
    return render_template('contact-page.html')


@app.route('/contact/', methods=['POST'])
def contact_page_form():
    mail_pattern = r"^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$"
    if task_manager.contact_form_tasks >= 50:
        return "Sorry, server busy, please try again"
    if not request.form.get('contact-robot-field'):
        return render_template(
            'contact-page.html',
            posted_message="""Please select the "I am a human" checkbox"""
        )
    if re.search(mail_pattern, request.form['contact-email-field']) is None:
        return render_template(
            'contact-page.html',
            posted_message="Sorry, invalid email. Please try again."
        )
    if request.form['contact-fish-field'] == "" and not request.form.get('contact-human-field'):
        task_manager.contact_form_tasks += 1
        job = TmPersist.persist_store.scheduler.add_job(
            func=task_manager.contact_form_email,
            id="contact page form",
            name="contact page form",
            replace_existing=False,
            kwargs={
                "name": request.form['contact-name-field'],
                "email": request.form['contact-email-field'],
                "subject": request.form['contact-subject-field'],
                "body": request.form['contact-msg-field']
            }
        )
        print(f"{job.name} job added")
        return render_template(
            'contact-page.html',
            posted_message="Thank you, I should be in contact with you shortly."
        )
    print("fish detected")
    return render_template(
        'contact-page.html',
        posted_message="Thank you, I should be in contact with you shortly."
    )


print(f"===flask application initialized at {datetime.datetime.now()}===")
