import helper.resume_loader.res_loader as rl
import helper.projects.project_loader as pl
from helper.projects.project_blueprint import project as projects
from scheduled_tasks import TaskManager
import secret_config

from flask import Flask, render_template, request
import flask_cors

import smtplib, ssl

# application stuff
app = Flask(__name__)
application = app

# application config
class SchedConfig:
    SCHEDULER_API_ENABLED = True
    MAIL_SERVER = secret_config.current_mail_config['server']
    MAIL_PORT = secret_config.current_mail_config['port']
    MAIL_USERNAME = secret_config.current_mail_config['username']
    MAIL_PASSWORD = secret_config.current_mail_config['password']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
app.config.from_object(SchedConfig())

#scheduler
task_manager = TaskManager(app)

# CORS stuff
flask_cors.CORS(app)

# scheduler
task_manager.scheduler.init_app(app)
task_manager.scheduler.start()

# blueprints
app.register_blueprint(projects)

# app pages
@app.route('/')
def landing_page():
    return render_template('title-slide.html')


@app.route('/about/')
def about_page():
    return render_template(
        'about-page.html',
        education=rl.get_education()[::-1],
        experience=rl.get_experience()[::-1],
        certification=rl.get_certification()[::-1],
        skills=rl.get_skills()
    )

@app.route('/projects/', methods=['GET', 'POST'])
def projects_page():
    return render_template(
        'project-page.html',
        projects=pl.get_projects()[::-1],
        params=request.args.to_dict()
    )

@app.route('/contact/', methods=['GET'])
def contact_page():
    return render_template('contact-page.html')

@app.route('/contact/', methods=['POST'])
def contact_page_form():
    # sanitization/verification

    job = task_manager.scheduler.add_job(
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
    print (f"{job.name} job added")
    
    return render_template('contact-page.html', posted=True)
