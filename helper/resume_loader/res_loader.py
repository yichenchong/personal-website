import os
import sqlite3
from helper.resume_loader.res_format import ResFormat

cwd = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(cwd, 'resume.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()

def get_education():
    res = cur.execute("SELECT * FROM education ORDER BY id;")
    formatted_res = list(map(lambda x : ResFormat('education', x), res))
    return formatted_res

def get_experience():
    res = cur.execute("SELECT * FROM experience ORDER BY id;")
    formatted_res = list(map(lambda x : ResFormat('experience', x), res))
    return formatted_res

def get_certification():
    res = cur.execute("SELECT * FROM certification ORDER BY id;")
    formatted_res = list(map(lambda x : ResFormat('certification', x), res))
    return formatted_res

def get_skills():
    res = cur.execute("SELECT * FROM skills ORDER BY id;")
    return res