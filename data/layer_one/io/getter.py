import os
import sqlite3
from data.layer_one.io.project_structure import cwd, db_dir, html_dir, project_dir


class ProjectGetter:
    con = None
    cur = None

    @classmethod
    def connect(cls):
        project_db_path = os.path.join(db_dir, 'projects.db')
        cls.con = sqlite3.connect(project_db_path, check_same_thread=False)
        cls.cur = cls.con.cursor()

    @classmethod
    def disconnect(cls):
        cls.con.close()

    @classmethod
    def get_all_projects(cls):
        cls.connect()
        cls.cur.execute("SELECT * FROM projects ORDER BY seq;")
        projects = list(cls.cur.fetchall())
        cls.disconnect()
        return projects

    @classmethod
    def get_featured_skills(cls):
        cls.connect()
        cls.cur.execute("SELECT * FROM skills WHERE featured = 1 ORDER BY seq;")
        projects = list(cls.cur.fetchall())
        cls.disconnect()
        return projects

    @classmethod
    def get_skill_names_by_project_uuid(cls, project_uuid):
        cls.connect()
        cls.cur.execute(f"SELECT skill_uuid FROM project_skills WHERE project_uuid = '{project_uuid}';")
        skill_uuids = cls.cur.fetchall()
        skill_uuids = tuple([item[0] for item in skill_uuids])
        cls.cur.execute(f"SELECT skill_name FROM skills WHERE uuid IN {skill_uuids};")
        skills = cls.cur.fetchall()
        skills = [item[0] for item in skills]
        cls.disconnect()
        return skills

    @classmethod
    def get_project_uuids_by_skill_name(cls, skill_name):
        cls.connect()
        cls.cur.execute(f"SELECT uuid FROM skills WHERE skill_name = '{skill_name}';")
        uuid = cls.cur.fetchone()[0]
        cls.cur.execute(f"SELECT project_uuid FROM project_skills WHERE skill_uuid = '{uuid}';")
        project_uuids = cls.cur.fetchall()
        project_uuids = [item[0] for item in project_uuids]
        return project_uuids


class ResumeGetter:
    con = None
    cur = None

    @classmethod
    def connect(cls):
        project_db_path = os.path.join(db_dir, 'resume.db')
        cls.con = sqlite3.connect(project_db_path, check_same_thread=False)
        cls.cur = cls.con.cursor()

    @classmethod
    def disconnect(cls):
        cls.con.close()

    @classmethod
    def get_resume_data(cls):
        cls.connect()
        cls.cur.execute("SELECT * FROM categories;")
        categories = cls.cur.fetchall()
        category_items = dict()
        for cat in categories:
            cat_id = cat[0]
            name = cat[1]
            cls.cur.execute(f"SELECT item_uuid FROM category_items WHERE category_index = {cat_id};")
            item_ids = cls.cur.fetchall()
            item_ids = tuple([i[0] for i in item_ids])
            cls.cur.execute(f"SELECT * FROM items WHERE uuid IN {item_ids} ORDER BY seq;")
            data = list(cls.cur.fetchall())[::-1]
            item_list = []
            for i in data:
                item_content_file = os.path.join(html_dir, f"{i[0]}.html")
                with open(item_content_file, 'r') as read_file:
                    arr = list(i)
                    arr.append(read_file.read())
                item_list.append(tuple(arr))
            category_items[name] = item_list
        cls.disconnect()
        return category_items


ResumeGetter.get_resume_data()