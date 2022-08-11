import sqlite3
import os
import uuid

cwd = os.path.dirname(os.path.realpath(__file__))
res_loader_dir = os.path.split(cwd)[0]
db_path = os.path.join(res_loader_dir, 'resume.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()

def load(name, logo):
    cur.execute(f"INSERT INTO skills ( skill_name, skill_logo ) VALUES ('{name}', '{logo}');")
    con.commit()

def clear():
    cur.execute(f"DROP TABLE skills;")
    con.commit()

def loadall():
    load("Computer Science", "https://cdn.jsdelivr.net/gh/yichenchong/elegant-circles/svg/dev.svg")
    load("Mathematics", "https://cdn.jsdelivr.net/gh/yichenchong/elegant-circles/svg/circlecompass.svg")
    load("Data", "https://cdn.jsdelivr.net/gh/yichenchong/elegant-circles/svg/trends.svg")
    load("Robotics", "https://cdn.jsdelivr.net/gh/yichenchong/personal-website/static/img/robot.svg")
    load("Python", "https://cdn.cdnlogo.com/logos/p/3/python.svg")
    load("Java", "https://cdn.cdnlogo.com/logos/j/2/java.svg")
    load("C", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg")
    load("Kotlin", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg")
    load("Haskell", "https://cdn.cdnlogo.com/logos/h/95/haskell.svg")
    load("Golang", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg")
    load("R", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg")
    load("Shell Scripting", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg")
    load("HTML", "https://cdn.cdnlogo.com/logos/h/84/html.svg")
    load("JavaScript", "https://cdn.cdnlogo.com/logos/j/44/javascript.svg")
    load("Bootstrap", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg")
    load("CSS", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg")
    load("SQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg")
    load("Git", "https://cdn.cdnlogo.com/logos/g/15/git-icon.svg")
    load("Flask", "https://cdn.jsdelivr.net/gh/yichenchong/personal-website/static/img/flask-original.png")
    load("Pytest", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg")
    load("Swagger", "https://cdn.jsdelivr.net/gh/yichenchong/personal-website/static/img/swagger_logo.svg")
    load("Postman", "https://cdn.jsdelivr.net/gh/yichenchong/personal-website/static/img/postman_logo.png")
    load("Jira", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jira/jira-original.svg")
    load("Arduino", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg")
    load("JetBrains", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jetbrains/jetbrains-original.svg")
    load("Adobe Photoshop", "https://cdn.cdnlogo.com/logos/p/8/photoshop.svg")
    load("Adobe Illustrator", "https://cdn.cdnlogo.com/logos/i/1/illustrator.svg")
    load("Adobe Premiere Pro", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/premierepro/premierepro-original.svg")
    load("Microsoft Office", "https://cdn.cdnlogo.com/logos/o/89/office.svg")

clear()
cur.execute('''CREATE TABLE IF NOT EXISTS skills ( id INTEGER PRIMARY KEY AUTOINCREMENT, skill_name text, skill_logo text );''')
con.commit()
loadall()