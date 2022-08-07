import helper.resume_loader.res_loader as rl

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('title-slide.html')


@app.route('/about/')
def about_page():
    return render_template('about-page.html', education=rl.get_education()[::-1])


@app.route('/projects/')
def contact_page():
    return render_template('project-page.html')


@app.route('/contact/')
def project_page():
    return render_template('contact-page.html')
