import helper.resume_loader.res_loader as rl
import helper.projects.project_loader as pl
from helper.projects.project_blueprint import project as projects
import secret_config

from flask import Flask, render_template, request
import flask_cors

import sys
import smtplib, ssl

app = Flask(__name__)
application = app
flask_cors.CORS(app)
app.register_blueprint(projects)

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

def log_message(message, app):
    print(message.subject)

email_dispatched.connect(log_message)

@app.route('/contact/', methods=['POST'])
def contact_page_form():
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    from_addr = 'noreply@yichenchong.com'
    to_addrs = ['yichenchong@yahoo.com', 'noreply@yichenchong.com']
    msg = f"""\
From: {from_addr}
To: {to_addrs[0]}
Subject: Webform email: {request.form['contact-subject-field']}
{request.form['contact-msg-field']}

Sent by {request.form['contact-name-field']}, {request.form['contact-email-field']}"""
    
    with smtplib.SMTP_SSL(
        secret_config.current_mail_config["server"],
        port=secret_config.current_mail_config["port"],
        context=context
    ) as server:
        server.login(secret_config.current_mail_config["username"], secret_config.current_mail_config["password"])
        server.sendmail(from_addr, to_addrs, msg)
        server.quit()
    print("mail sent..")
    return render_template('contact-page.html', posted=True)
