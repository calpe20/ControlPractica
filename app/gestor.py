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
        
        data = Alumno.select()
        # select * from alumno where nombre = 'julio'
        
        #data = Alumno.select(lambda a: )
        alumno = Alumno.get(id=39)
        # Update alumno set nombre = 'Gin' where id =3;
        alumno.nombre = 'FEmilio'

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
            alumno = Alumno[alumno_id]
            if alumno:
                alumno.edad = data['edad'] 
                alumno.direccion = data['direccion']
                alumno.observacion = data['observacion'] 
                alumno.estado = data['estado']            
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


# Tabla maestra Especialidad

    @db_session
    def get_Esp(self):
        
        data = Especialidad.select()
            
        print(len(data))
        response = []
        if data:
            for a in data:
                row = {
                    'id': a.id,
                    'nombre': a.nombre,
                    'estado': a.estado
                }
                response.append(row)
            return True, response
        return False, response


    @db_session
    def new_Esp(self, data):
        try:
            Especialidad(**data)
            commit()
            return True, 'Creation Successful!'
        except Exception as e:
            return False, '{0}'. format(e)
        
    
    @db_session
    def edit_Esp(self, esp_id, data):
        try:
            especialidad = Especialidad[esp_id]
            if especialidad:
                especialidad.nombre = data['nombre']
                especialidad.estado = data['estado']
                commit()
                return True, 'Edit sucessful!'
            else:
                return False, 'Specialty not found'
        except Exception as e:
            return False, str(e)


    @db_session
    def delete_Esp(self, esp_id):
        try:
            especialidad = Especialidad.get(id=esp_id)
            if especialidad:
                especialidad.delete()
                commit()
                return True, 'Delete sucessful!'
            else:
                return False, 'Specialty not found'
        except Exception as e:
            return False, str(e)
    
                
# Tabla maestra Curso

    @db_session
    def get_Curso(self):
        
        data = Curso.select()
        
        print(len(data))
        response = []
        if data:
            for a in data:
                row = {
                    'id': a.id,
                    'nombre': a.nombre,
                    'credito': a.credito,
                    'estado': a.estado
                }
                response.append(row)
            return True, response
        return False, response
    
    @db_session
    def new_Curso(self, data):
        try:
            Curso(**data)
            commit()
            return True, 'Creation Successful!'
        except Exception as e:
            return False, '{0}'. format(e)
        
    @db_session
    def edit_Curso(self, curso_id, data):
        try:
            curso = Curso[curso_id]
            if curso:
                curso.nombre = data['nombre']
                curso.credito = data['credito']
                curso.estadoq = data['estado']
                return True, 'Edit succesful!'
            else:
                return False, 'Curso not found'
        except Exception as e:
            return False, str(e) 
        
    @db_session
    def delete_Curso(self, curso_id):
        try:
            curso = Curso.get(id=curso_id)
            if curso:
                curso.delete()
                commit()
                return True, 'Delete sucessful!'
            else:
                return False, 'Curso not found'
        except Exception as e:
            return False, str(e)
            
    
db = DBAdmin()
