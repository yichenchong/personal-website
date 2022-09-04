import helper.resume_loader.res_loader as rl
import helper.projects.project_loader as pl
from helper.projects.project_blueprint import project as projects
from scheduled_tasks import scheduler, contact_form_email
import secret_config

from flask import Flask, render_template, request
import flask_cors

import smtplib, ssl

# application stuff
app = Flask(__name__)
application = app

# CORS stuff
flask_cors.CORS(app)

# scheduler
class SchedConfig:
    SCHEDULER_API_ENABLED = True
app.config.from_object(SchedConfig())
scheduler.init_app(app)
scheduler.start()

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
    job = scheduler.add_job(
        func=contact_form_email,
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
    
    # Create a secure SSL context
#     context = ssl.create_default_context()
    
#     from_addr = 'noreply@yichenchong.com'
#     to_addrs = ['yichenchong@yahoo.com', 'noreply@yichenchong.com']
#     msg = f"""\
# From: {from_addr}
# To: {to_addrs[0]}
# Subject: Webform email: {request.form['contact-subject-field']}
# {request.form['contact-msg-field']}

# Sent by {request.form['contact-name-field']}, {request.form['contact-email-field']}"""
    
#     with smtplib.SMTP_SSL(
#         secret_config.current_mail_config["server"],
#         port=secret_config.current_mail_config["port"],
#         context=context
#     ) as server:
#         server.login(secret_config.current_mail_config["username"], secret_config.current_mail_config["password"])
#         server.sendmail(from_addr, to_addrs, msg)
#         server.quit()
    # print("mail sent..")
    return render_template('contact-page.html', posted=True)
