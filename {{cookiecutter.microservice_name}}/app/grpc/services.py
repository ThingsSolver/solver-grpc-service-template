# Business logic, please delete example
from app.database.daos import ExampleQuery


class Basic:
    def __init__(self):
        self.c = ExampleQuery()

    def get_data(self, uid):
        return self.c.get_record(id='id')

