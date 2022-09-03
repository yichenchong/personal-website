from inspect import CO_VARKEYWORDS
import sqlite3
import os

cwd = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(cwd, 'projects.db')
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS projects ( id INTEGER PRIMARY KEY AUTOINCREMENT, p_name TEXT, subtitle TEXT, dates TEXT, logo TEXT, c_file TEXT, blurb TEXT, tags TEXT, featured INTEGER );''')
con.commit()

def load(name, page_name, subtitle, dates, logo, blurb="", featured = "FALSE"):
    file = page_name
    try:
        f = open(os.path.join(cwd, f"templates/{file}.html"), "x")
        f.write(
                """<div class="page-title">{name}</div>
<div class="slide"><div class="slide-container center-justify">404 page yet to be created</div></div>"""
        )
        f.close()
    except FileExistsError:
        print(f"File {page_name}.html exists")
    res = cur.execute(f"""INSERT INTO projects (p_name, subtitle, dates, logo, c_file, blurb, tags, featured) VALUES ('{name}', '{subtitle}', '{dates}', '{logo}', '{page_name}', "{blurb}", '', {featured});""")
    con.commit()

def change_order(old_id, new_id):
    res = cur.execute(f"UPDATE projects SET id = '{new_id}' WHERE id = '{old_id}'")
    con.commit()

def feature(name):
    res = cur.execute(f"UPDATE projects SET featured = TRUE WHERE p_name = '{name}'")
    con.commit()

def unfeature(name):
    res = cur.execute(f"UPDATE projects SET featured = FALSE WHERE p_name = '{name}'")
    con.commit()

def change_date(name, new_dates):
    res = cur.execute(f"UPDATE projects SET dates = '{new_dates}' WHERE p_name = '{name}'")
    con.commit()

def change_subtitle(name, subtitle):
    res = cur.execute(f"UPDATE projects SET subtitle = '{subtitle}' WHERE p_name = '{name}'")
    con.commit()

def change_logo(name, img_url):
    res = cur.execute(f"UPDATE projects SET logo = '{img_url}' WHERE p_name = '{name}'")
    con.commit()

def add_tag(name, new_tag):
    res = cur.execute(f"SELECT tags FROM projects WHERE p_name = '{name}'")
    tags = set(res.fetchone()[0].split(","))
    if tags == {""}:
        tags = set()
    tags.add(new_tag)
    tags = ",".join(tags)
    res = cur.execute(f"""UPDATE projects SET tags = "{ tags }" WHERE p_name = '{name}'""")
    con.commit()

def rm_tag(name, tag):
    res = cur.execute(f"SELECT tags FROM projects WHERE p_name = '{name}'")
    tags = set(res.fetchone()[0].split(","))
    tags.remove(tag)
    tags = ",".join(tags)
    res = cur.execute(f"""UPDATE projects SET tags = "{ tags }" WHERE p_name = '{name}'""")
    con.commit()

change_subtitle("Personal Website v1", "Personal Portfolio Project (Work in Progress)")
add_tag("Microsoft Office")