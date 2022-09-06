from urllib.parse import quote

class ProjectFormat:
    def __init__(self, sql_data):
        self.name = sql_data[1]
        self.subtitle = sql_data[2]
        self.dates = sql_data[3]
        self.logo = sql_data[4]
        self.page = sql_data[5]
        self.blurb = sql_data[6]
        self.tags = self.get_tags(sql_data[7])
        self.tags.sort()
        self.sanitized_tags = self.sanitize(self.tags)
        self.featured = bool(sql_data[8])
    
    def get_tags(self, tag_string):
        if tag_string == "":
            return set()
        return list(set([i for i in tag_string.split(",")]))
    
    def sanitize(self, arr):
        return [quote(i) for i in arr];