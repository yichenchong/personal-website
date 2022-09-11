import os
import sqlite3
import uuid

cwd = os.path.dirname(os.path.realpath(__file__))
db_dir = os.path.join(os.path.split(cwd)[0], 'db')
html_dir = os.path.join(os.path.split(cwd)[0], 'static/html')
project_dir = os.path.join(os.path.split(cwd)[0], 'static/project_html')

class ProjectWriter:

    @classmethod
    def connect(cls):
        project_db_path = os.path.join(db_dir, 'projects.db')
        print(project_db_path)
        cls.con = sqlite3.connect(project_db_path, check_same_thread=False)
        cls.cur = cls.con.cursor()


    @classmethod
    def disconnect(cls):
        cls.con.close()
    
    @classmethod
    def setup(cls):
        cls.cur.execute('''CREATE TABLE IF NOT EXISTS projects ( uuid TEXT UNIQUE NOT NULL, seq INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, subtitle TEXT, dates TEXT, content_page TEXT, featured TEXT );''')
        cls.cur.execute('''CREATE TABLE IF NOT EXISTS project_skills ( row_id INTEGER PRIMARY KEY, project_uuid TEXT, skill_uuid TEXT );''')
        cls.cur.execute('''CREATE TABLE IF NOT EXISTS skills ( uuid TEXT UNIQUE NOT NULL, seq INTEGER PRIMARY KEY AUTOINCREMENT, skill_name TEXT, logo TEXT, featured INTEGER );''')
        cls.con.commit()

    @classmethod
    def add_project(cls, title, subtitle, dates, page_name, *skills):
        proj_uuid = uuid.uuid4().hex
        with open(os.path.join(project_dir, f"{page_name}.html"), "x") as content_file:
            content_file.write("")
        cls.cur.execute(f"INSERT INTO projects ( uuid, title, subtitle, dates, content_page, featured ) VALUES ( '{proj_uuid}', '{title}', '{subtitle}', '{dates}', '{page_name}', 0 )")
        for i in skills:
            cls.cur.execute(f"SELECT uuid FROM skills WHERE skill_name = '{ i }';")
            skill_uuid = cls.cur.fetchone()
            if skill_uuid is None:
                skill_uuid = uuid.uuid4().hex
                print(skill_uuid)
                cls.cur.execute(f"INSERT INTO skills ( uuid, skill_name, featured ) VALUES ('{ skill_uuid }', '{i}', 0 );")
            skill_uuid = skill_uuid[0] if isinstance(skill_uuid, tuple) else skill_uuid
            cls.cur.execute(f"INSERT INTO project_skills ( project_uuid, skill_uuid ) VALUES ( '{proj_uuid}', '{skill_uuid}' );")
        cls.con.commit()


class ResumeWriter:
    @classmethod
    def connect(cls):
        resume_db_path = os.path.join(db_dir, 'resume.db')
        print(resume_db_path)
        cls.con = sqlite3.connect(resume_db_path, check_same_thread=False)
        cls.cur = cls.con.cursor()

    @classmethod
    def disconnect(cls):
        cls.con.close()


    @classmethod
    def setup(cls):
        cls.cur.execute('''CREATE TABLE IF NOT EXISTS items ( uuid TEXT NOT NULL UNIQUE, seq INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, subtitle TEXT, dates TEXT, logo TEXT );''')
        cls.cur.execute('''CREATE TABLE IF NOT EXISTS category_items ( category_index INTEGER, item_uuid TEXT PRIMARY KEY );''')
        cls.cur.execute('''CREATE TABLE IF NOT EXISTS categories ( seq INTEGER PRIMARY KEY AUTOINCREMENT, category_name TEXT );''')
        try:
            for i in [(1, "Education"), (2, "Experience"), (3, "Certification")]:
                cls.cur.execute(f'''INSERT INTO categories VALUES ( {i[0]}, '{i[1]}' );''')
        except sqlite3.IntegrityError:
            print("Insertions already occurred")
        cls.con.commit()
    
    @classmethod
    def add_item(cls, category, title, subtitle, dates, logo):
        proj_uuid = uuid.uuid4().hex
        with open(os.path.join(html_dir, f"{proj_uuid}.html"), "x") as content_file:
            content_file.write("")
        cls.cur.execute(f"INSERT INTO items ( uuid, title, subtitle, dates, logo ) VALUES ( '{proj_uuid}', '{title}', '{subtitle}', '{dates}', '{logo}' );")
        cls.cur.execute(f"SELECT seq FROM categories WHERE category_name = '{category}';")
        cat_id = cls.cur.fetchone()[0]
        cls.cur.execute(f"INSERT INTO category_items VALUES ( {cat_id}, '{proj_uuid}' );")
        cls.con.commit()

def connect():
    ResumeWriter.connect()
    ProjectWriter.connect()

def disconnect():
    ResumeWriter.connect()
    ProjectWriter.disconnect()

connect()
ProjectWriter.setup()
ProjectWriter.add_project(
    "Innovation Institute Projects",
    "Student/Participant",
    "2015 - 2017",
    "innovation_institute",
    "Adobe Illustrator",
    "Adobe Photoshop",
    "Adobe Premiere",
    "Arduino",
    "C++",
    "Design",
    "Engineering",
    "Robotics",
    "Teamwork"
)
ProjectWriter.add_project(
    "SASPX FRC Initiative",
    "Founder",
    "2016 - 2018",
    "frc",
    "Business",
    "Engineering",
    "Robotics"
)
ProjectWriter.add_project(
    "DNA Digital Data Storage",
    "Intel Science and Engineering Fair and AP Research Researcher",
    "2017 - 2018",
    "dna_digital_data_storage",
    "Computer science",
    "Python",
    "Statistics"
)
ProjectWriter.add_project(
    "AP Statistics Project",
    "Student Research",
    "2018",
    "ap_stats_survey",
    "CSS",
    "Flask",
    "HTML",
    "Mathematics",
    "Programming",
    "Python",
    "REST",
    "SQL",
    "Statistics",
    "Teamwork",
    "Web development"
)
ProjectWriter.add_project(
    "Almanac",
    "Co-Developer",
    "2018 - 2019",
    "almanac",
    "Data",
    "Flask",
    "Python",
    "SQL",
    "Web scraping",
    "Web development"
)
ProjectWriter.add_project(
    "Vending Machine Committee",
    "Lead Engineer",
    "2018 - 2019",
    "vending_machine",
    "Adobe Photoshop",
    "Business",
    "C",
    "C++",
    "Computer science",
    "Engineering",
    "Mathematics",
    "Physics",
    "Robotics",
    "Teamwork"
)
ProjectWriter.add_project(
    "Projectile Rocket Simulation",
    "Programmer",
    "2020",
    "projectile_rockets",
    "C++",
    "Computer science",
    "Mathematics",
    "Physics",
    "Python"
)
ProjectWriter.add_project(
    "Dynamic-R",
    "Researcher/Author",
    "2020",
    "dynamic_r",
    "Biology",
    "Data",
    "Mathematics",
    "Statistics"
)
ProjectWriter.add_project(
    "Mortality Predictions",
    "Hobby project",
    "2021",
    "mortality_models",
    "AI/ML",
    "Data",
    "Mathematics",
    "Python",
    "R"
)
ProjectWriter.add_project(
    "Word Game Solvers",
    "Hobby project",
    "2021",
    "word_games",
    "C++",
    "Java",
    "Programming",
    "Python"
)
ProjectWriter.add_project(
    "Computing Practical 1 Labs",
    "First-year curricular projects",
    "2021 - 2022",
    "comp40009",
    "C",
    "Computer science",
    "Git",
    "Haskell",
    "Java",
    "Kotlin",
    "Programming"
)
ProjectWriter.add_project(
    "Computing Practical 1 C Group Project",
    "Building an ARM emulator and assembler",
    "2021",
    "c_group_project",
    "Assembly",
    "C",
    "Computer science",
    "Git",
    "Programming",
    "Teamwork"
)
ProjectWriter.add_project(
    "Personal Website v1",
    "Personal Portfolio Project (Work in Progress)",
    "2022 - Present",
    "personal_website_v1",
    "CSS",
    "Computer science",
    "Flask",
    "HTML",
    "Programming",
    "Python",
    "SQL",
    "Web development"
)

# ResumeWriter.add_item(
#     category="Education",
#     title="Shanghai American School",
#     subtitle="US High School Diploma",
#     dates="2015 - 2019",
#     logo="https://media-exp1.licdn.com/dms/image/C4D0BAQGqHutcTiqC_Q/company-logo_100_100/0/1648805896641?e=1668038400&v=beta&t=OcK287yu2VPBH_TSKwBZUMRjNuuZZI9qy1SBdb_YHns"
# )
# ResumeWriter.add_item(
#     category="Experience",
#     title="Sergeant (3SG), Combat Engineer",
#     subtitle="Singapore Armed Forces",
#     dates="2019 - 2021",
#     logo="https://media-exp1.licdn.com/dms/image/C4D0BAQFfFC1-GyqZJg/company-logo_100_100/0/1519866192442?e=1668038400&v=beta&t=qw0D2XY7RYlJvsSr9dB_NYv7dujKpr7ZdioRl7MKONI"
# )
# ResumeWriter.add_item(
#     category="Certification",
#     title="MicroBachelors Program in Computer Science Fundamentals",
#     subtitle="NYU via edX",
#     dates="Dec 2020",
#     logo="https://media-exp1.licdn.com/dms/image/C560BAQH_xbnvm8hevg/company-logo_100_100/0/1608046236488?e=1668038400&v=beta&t=C1rX69UzUmk3c3xjuVYmKsltaehg5h0gZKhvax7_sXg"
# )
# ResumeWriter.add_item(
#     category="Education",
#     title="Imperial College London",
#     subtitle="BEng Mathematics and Computer Science",
#     dates="2021 - Present",
#     logo="https://media-exp1.licdn.com/dms/image/C4D0BAQGqHutcTiqC_Q/company-logo_100_100/0/1648805896641?e=1668038400&v=beta&t=OcK287yu2VPBH_TSKwBZUMRjNuuZZI9qy1SBdb_YHns"
# )
# ResumeWriter.add_item(
#     category="Certification",
#     title="Securities Education Certificate",
#     subtitle="Imperial College Investment Society",
#     dates="Jan 2022",
#     logo="https://media-exp1.licdn.com/dms/image/C4E0BAQFYd3UKw6Pw7Q/company-logo_100_100/0/1599601428810?e=1668038400&v=beta&t=JjIx833VtAMVKG2lGBTKrTBn_Y54__pdsHYLMzW1T9c"
# )
# ResumeWriter.add_item(
#     category="Experience",
#     title="Software Test Engineer Intern",
#     subtitle="ByteDance (Bytehouse Data Platform)",
#     dates="Jul - Sep 2022",
#     logo="https://media-exp1.licdn.com/dms/image/C560BAQGA-1ynUGnhlA/company-logo_100_100/0/1600334313022?e=1668038400&v=beta&t=WHFyINQGchz6yk8mom2wNWBNVk-GIWbEJmxGlkjORdw"
# )
disconnect()