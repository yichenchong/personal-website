import sqlite3
import os
import uuid

cwd = os.path.dirname(os.path.realpath(__file__))
res_loader_dir = os.path.split(cwd)[0]
db_path = os.path.join(res_loader_dir, 'resume.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS certification ( id INTEGER PRIMARY KEY AUTOINCREMENT, place text, title text, dates text, content text, imagelink text );''')
con.commit()

def load():
    EDUCATION_SCHOOL = "Imperial College Investment Society"
    EDUCATION_TITLE = "Securities Education Certificate"
    EDUCATION_DATES = ""
    EDUCATION_CONTENT = """Jan 2022"""
    EDUCATION_LOGO = """https://media-exp1.licdn.com/dms/image/C4E0BAQFYd3UKw6Pw7Q/company-logo_100_100/0/1599601428810?e=1668038400&v=beta&t=JjIx833VtAMVKG2lGBTKrTBn_Y54__pdsHYLMzW1T9c"""

    EDUCATION_CONTENT_FILE = uuid.uuid4().hex
    f = open(os.path.join(cwd, f"{EDUCATION_CONTENT_FILE}.html"), "x")
    f.write(EDUCATION_CONTENT)
    f.close()
    res = cur.execute(f"INSERT INTO certification (place, title, dates, content, imagelink) VALUES ('{EDUCATION_SCHOOL}', '{EDUCATION_TITLE}', '{EDUCATION_DATES}', '{EDUCATION_CONTENT_FILE}', '{EDUCATION_LOGO}');")
    print(res)
    con.commit()

def change_order(old_id, new_id):
    res = cur.execute(f"UPDATE certification SET id = '{new_id}' WHERE id = '{old_id}'")
    con.commit()

def change_date(id, date):
    cur.execute(f"UPDATE certification SET dates = '{date}' WHERE id = '{id}'")
    con.commit()

change_date(2, "Jan 2022")
change_date(1, "Dec 2020")