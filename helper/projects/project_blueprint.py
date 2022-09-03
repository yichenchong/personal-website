from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import helper.projects.project_loader as pl
from flask import request

project = Blueprint('project', __name__,
                        template_folder='templates')

@project.route('/projects/')
def main():
    return render_template(
        'project.html',
        project='index',
        projects=pl.get_projects()[::-1],
        params=request.args.to_dict()
    )

@project.route('/projects/<page>')
def show(page):
    return render_template(
        'project.html',
        project=page
    )