import os

class ResFormat:
    def __init__(self, sql_data):
        self.place = sql_data[1]
        self.title = sql_data[2]
        self.dates = sql_data[3]
        self.description_file = sql_data[4]
        self.image = sql_data[5]
        self.description_data = self.get_description_data()
    
    def get_description_data(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        print(os.path.join(cwd, f"education/{self.description_file}.html"))
        f = open(os.path.join(cwd, f"education/{self.description_file}.html"), "r")
        contents = f.read()
        return contents