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
        # select * from alumno where nombre = 'julio'
        
        #data = Alumno.select(lambda a: )
        alumno = Alumno.get(id=3)
        # Update alumno set nombre = 'Gin' where id =3;
        alumno.nombre = 'Gin'

        # rollback()
        # commit()
        print(len(data))
        response = []
        if data:
            for a in data:
                row = {
                    'id': a.id,
                    'nombre': a.nombre,
                    'apellidos': a.apellidos,
                    'edad': a.edad,
                    'dni': a.dni,
                    'direccion': a.direccion,
                    'observacion': a.observacion,
                    'estado': a.estado
                }
                response.append(row)
            return True, response
        return False, response
            

    @db_session
    def new_Alumno(self, data):
        try:
            Alumno(**data)
            commit()
            return True, 'Creation Successful!'
        except Exception as e:
            return False, '{0}'. format(e)
        
    
    @db_session
    def edit_Alumno(self, alumno_id, data):
        try:
            alumno = Alumno.get(id=alumno_id)
            if alumno:
<<<<<<< Updated upstream
                alumno.edad = data['edad'] 
                alumno.direccion = data['direccion']
                alumno.observacion = data['observacion'] 
                alumno.estado = data['estado']            
=======
                alumno.nombre = data['nombre']

>>>>>>> Stashed changes
                commit()
                return True, 'Edit successful!'
            else:
                return False, 'Alumno not found'
        except Exception as e:
            return False, str(e)
        
    
    @db_session
    def delete_Alumno(self, alumno_id):
        try:
            alumno = Alumno.get(id=alumno_id)
            if alumno:
                alumno.delete()
                commit()
                return True, 'Delete successful!'
            else:
                return False, 'Alumno not found'
        except Exception as e:
            return False, str(e)


db = DBAdmin()
