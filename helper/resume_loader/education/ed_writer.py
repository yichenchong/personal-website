import sqlite3
import os
import uuid

cwd = os.path.dirname(os.path.realpath(__file__))
res_loader_dir = os.path.split(cwd)[0]
db_path = os.path.join(res_loader_dir, 'resume.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS education ( id INTEGER PRIMARY KEY AUTOINCREMENT, place text, title text, dates text, content text, imagelink text );''')
con.commit()

def load():
    EDUCATION_SCHOOL = "Shanghai American School"
    EDUCATION_TITLE = "US High School Diploma"
    EDUCATION_DATES = "2015 - 2019"
    EDUCATION_CONTENT = """"""
    EDUCATION_LOGO = """https://media-exp1.licdn.com/dms/image/C4E0BAQG_5-f5FcsRSA/company-logo_100_100/0/1536305974552?e=1668038400&v=beta&t=sFQWWtWQB4KwjJHCfk9wD51jF-c6cEQixTAcmOVPruE"""

    EDUCATION_CONTENT_FILE = uuid.uuid4().hex
    f = open(os.path.join(cwd, f"{EDUCATION_CONTENT_FILE}.html"), "x")
    f.write(EDUCATION_CONTENT)
    f.close()
    res = cur.execute(f"INSERT INTO education (place, title, dates, content, imagelink) VALUES ('{EDUCATION_SCHOOL}', '{EDUCATION_TITLE}', '{EDUCATION_DATES}', '{EDUCATION_CONTENT_FILE}', '{EDUCATION_LOGO}');")
    print(res)
    con.commit()

def change_order(old_id, new_id):
    res = cur.execute(f"UPDATE education SET id = '{new_id}' WHERE id = '{old_id}'")
    con.commit()

load()
change_order(2, 3)
change_order(1, 2)
change_order(3, 1)