import helper.resume_loader.res_loader as rl
import helper.projects.project_loader as pl
from helper.projects.project_blueprint import project

from flask import Flask, render_template, request
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

app.register_blueprint(project)

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

@app.route('/projects/', methods=['GET'])
def projects_page():
    return render_template(
        'project-page.html',
        projects=pl.get_projects()[::-1],
        params=request.args.to_dict()
    )

@app.route('/contact/')
def contact_page():
    return render_template('contact-page.html')
