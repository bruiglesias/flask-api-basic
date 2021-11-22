# -*- coding: utf-8 -*-
from database.db import connect_database

dbConnection = connect_database()

class OneModel:
    def __init__(self):
        pass

    def one_method(self, description_dict):
        pass