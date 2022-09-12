from flask import Blueprint, render_template, abort
from data.layer_one.io.cache import LayerOneCaches
from flask import request

project = Blueprint('project', __name__,
                    template_folder='templates')


@project.route('/projects/')
def main():
    project_items = LayerOneCaches.get_projects(
        query=request.args.to_dict().get("filter")
    )
    return render_template(
        'project.html',
        project='index',
        project_items=project_items
    )


@project.route('/projects/<page>')
def show(page):
    return render_template(
        'project.html',
        project=page
    )