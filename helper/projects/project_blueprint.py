from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

project = Blueprint('project', __name__,
                        template_folder='templates')

@project.route('/projects/', defaults={'page': 'index'})
@project.route('/projects/<page>')
def show(page):
    return render_template(
        'project.html',
        project=page
    )