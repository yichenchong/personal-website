import os
import sqlite3
from helper.resume_loader.res_format import ResFormat

cwd = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(cwd, 'resume.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()

def get_education():
    res = cur.execute("SELECT * FROM education ORDER BY id;")
    formatted_res = list(map(lambda x : ResFormat(x), res))
    return formatted_res