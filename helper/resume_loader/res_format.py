import os

class ResFormat:
    def __init__(self, type, sql_data):
        self.place = sql_data[1]
        self.title = sql_data[2]
        self.dates = sql_data[3]
        self.description_file = sql_data[4]
        self.image = sql_data[5]
        self.type = type
        self.description_data = self.get_description_data()
    
    def get_description_data(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        f = open(os.path.join(cwd, f"{self.type}/{self.description_file}.html"), "r")
        contents = f.read()
        return contents