from app.dbase import *
# from app.libs.jsonapi import JSONAPI
from pony.orm.serialization import to_dict
from datetime import datetime, date
from flask import request, jsonify, session
import json


class DBAdmin:
    def __init__(self):
        db.bind(provider='mysql', user='root', password='', host='localhost', database='senati', port=3306)
        db.generate_mapping(create_tables=True)
    
    @db_session
    def get_Alumnos(self):
        data = Alumno()

    @db_session
    def new_Alumno(self, data):
        try:
            Alumno(**data)
            commit()
            return True, 'Creation Successful!'
        except Exception as e:
            return False, '{0}'. format(e)


db = DBAdmin()
