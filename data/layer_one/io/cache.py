import os

from data.layer_one.io.getter import ResumeGetter, ProjectGetter
from data.layer_one.io.project_structure import templates_dir, db_dir, html_dir, project_dir

from jinja2 import Template


class LayerOneCaches:
    resume_doc = ""  # document-based refresh-ahead cache
    project_bar_cache = dict()  # key-value refresh-ahead cache
    skills_cache = []
    skill_search_cache = dict()  # TODO: LRU cache to store query results

    @classmethod
    def init_caches(cls):
        res_data = ResumeGetter.get_resume_data()
        with open(os.path.join(templates_dir, 'res_section.html')) as tfile:
            res_template = Template(tfile.read())
        cls.resume_doc = res_template.render(res_data=res_data)
        project_data_raw = ProjectGetter.get_all_projects()
        with open(os.path.join(templates_dir, 'project_fragment.html'), 'r') as tfile:
            project_template = Template(tfile.read())
        for proj in project_data_raw:
            puuid = proj[0]
            skills = ProjectGetter.get_skill_names_by_project_uuid(puuid)
            skills.sort()
            templated_string = project_template.render(
                title=proj[2],
                subtitle=proj[3],
                dates=proj[4],
                page=proj[5],
                skills=skills
            )
            cls.project_bar_cache[puuid] = (proj[1], templated_string)
        cls.skills_cache = ProjectGetter.get_featured_skills()


    @classmethod
    def get_projects(cls, query=None):
        l1c = LayerOneCaches.project_bar_cache
        if query is None:
            cached_projects = [l1c[i] for i in l1c]
        else:
            project_uuids = ProjectGetter.get_project_uuids_by_skill_name(query)
            cached_projects = [l1c[i] for i in l1c if i in project_uuids]
        cached_projects.sort(key=lambda i: i[0], reverse=True)
        cached_projects = [i[1] for i in cached_projects]
        return "\n".join(cached_projects)
