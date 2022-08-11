import sqlite3
import os
import uuid

cwd = os.path.dirname(os.path.realpath(__file__))
res_loader_dir = os.path.split(cwd)[0]
db_path = os.path.join(res_loader_dir, 'resume.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS experience ( id INTEGER PRIMARY KEY AUTOINCREMENT, place text, title text, dates text, content text, imagelink text );''')
con.commit()

def load():
    WORK_TITLE = "ByteDance (Bytehouse, Data Platform)"
    WORK_PLACE = "Software Test Engineer Intern (Internship)"
    WORK_DATES = "Jul 2022 - Present"
    WORK_CONTENT = """"""
    WORK_LOGO = """https://media-exp1.licdn.com/dms/image/C560BAQGA-1ynUGnhlA/company-logo_100_100/0/1600334313022?e=1668038400&v=beta&t=WHFyINQGchz6yk8mom2wNWBNVk-GIWbEJmxGlkjORdw"""

    WORK_CONTENT_FILE = uuid.uuid4().hex
    f = open(os.path.join(cwd, f"{WORK_CONTENT_FILE}.html"), "x")
    f.write(WORK_CONTENT)
    f.close()
    cur.execute(f"INSERT INTO experience (place, title, dates, content, imagelink) VALUES ('{WORK_PLACE}', '{WORK_TITLE}', '{WORK_DATES}', '{WORK_CONTENT_FILE}', '{WORK_LOGO}');")
    con.commit()

def change_name(id, name):
    cur.execute(f"UPDATE experience SET place = '{name}' WHERE id = '{id}'")
    con.commit()

def change_date(id, date):
    cur.execute(f"UPDATE experience SET dates = '{date}' WHERE id = '{id}'")
    con.commit()

def change_order(old_id, new_id):
    cur.execute(f"UPDATE experience SET id = '{new_id}' WHERE id = '{old_id}'")
    con.commit()

change_name(2, "Software Test Engineer Intern")