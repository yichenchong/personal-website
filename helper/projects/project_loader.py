import os
import sqlite3
from helper.projects.project_format import ProjectFormat

cwd = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(cwd, 'projects.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()

def get_projects():
    res = cur.execute("SELECT * FROM projects ORDER BY id;").fetchall()
    formatted_res = list(map(lambda x : ProjectFormat(x), res))
    return formatted_res
