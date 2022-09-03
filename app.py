import helper.resume_loader.res_loader as rl
import helper.projects.project_loader as pl
from helper.projects.project_blueprint import project as projects
import secret_config

from flask import Flask, render_template, request
import flask_cors
from flask_mail import Mail, Message

app = Flask(__name__)
flask_cors.CORS(app)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = secret_config.gmail_username
app.config['MAIL_PASSWORD'] = secret_config.gmail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

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

@app.route('/contact/', methods=['POST'])
def contact_page_form():
    msg = Message(
        subject=f"Webform email: {request.form['contact-subject-field']}",
        recipients=[("Master", "yichenchong@yahoo.com")],
        body=f"{request.form['contact-msg-field']}\n\n\n From: {request.form['contact-name-field']}, {request.form['contact-email-field']}",
        sender='chongyichen03@gmail.com'
    )
    mail.send(msg)
    return render_template('contact-page.html', posted=True)
