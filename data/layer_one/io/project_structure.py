import os

cwd = os.path.dirname(os.path.realpath(__file__))
db_dir = os.path.join(os.path.split(cwd)[0], 'db')
html_dir = os.path.join(os.path.split(cwd)[0], 'static/html')
project_dir = os.path.join(os.path.split(cwd)[0], '../../blueprints/projects/templates')
templates_dir = os.path.join(os.path.split(cwd)[0], 'static/templates')
