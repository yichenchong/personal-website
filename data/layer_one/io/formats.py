import os
import sqlite3

class SkillFormat:
    def __init__(self, sql_data):
        """Converts single SQL skill entry into data"""
        self.uuid = sql_data[0]
        self.index = sql_data[1]
        self.name = sql_data[2]
        self.featured = sql_data[3]          

class ProjectFormat:
    def __init__(self, sql_data):
        assert len(sql_data) == 7
        self.uuid = sql_data[0]
        self.index = sql_data[1]
        self.title = sql_data[2]
        self.subtitle = sql_data[3]
        self.dates = sql_data[4]
        self.content_page = sql_data[5]
        self.featured = sql_data[6]
        self.skills = self.get_skills()

    def get_skills(self):
        # TODO
        return 


