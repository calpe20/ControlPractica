from pony.orm import *

db = Database()


class Alumno(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str, 50)
    apellidos = Required(str, 100)
    edad = Required(int)
    dni = Required(str, 8, unique=True)
    direccion = Optional(str, 200)
    observacion = Optional(LongStr)
    estado = Required(int)
    matricula = Set('Matricula')


class Especialidad(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str, 100)
    estado = Required(int)
    cursoespecialidad = Set('Cursoespecialidad')


class Curso(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str, 20)
    credito = Required(int)
    estado = Required(int)
    cursoespecialidad = Set('Cursoespecialidad')


class Cursoespecialidad(db.Entity):
    id = PrimaryKey(int, auto=True)
    idespecialidad = Required(Especialidad)
    idcurso = Required(Curso)


class Matricula(db.Entity):
    id = PrimaryKey(int, auto=True)
    idalumno = Required(Alumno)
    idespecialidad = Required(Especialidad)
