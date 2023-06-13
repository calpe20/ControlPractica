from app import app
from app.gestor import *
from flask import request, jsonify


# Rutas Alumno

@app.route('/api/alumno', methods = ['GET'])
def api_alumno_get():
    if request.method == 'GET':
        status, data = db.get_Alumnos()
        return jsonify({'status': status,'message': 'RELACION DE ALUMNOS', 'data': data})
    #return jsonify({'message': 'Lista de alumnos'})


@app.route('/api/alumno', methods=['POST'])
def api_alumno_post():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Alumno(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})


@app.route('/api/alumno<int:id>', methods = ['PUT'])
def api_alumno_put(id):
    if request.method == 'PUT':
        data = request.json
        status, message  = db.edit_Alumno(id, data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})

   
@app.route('/api/alumno<int:id>', methods = ['DELETE'])
def api_alumno_delete(id):
    if request.method == 'DELETE':
        status, message = db.delete_Alumno(id)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})

    
# Rutas CursoEspecialidad   

@app.route('/api/esp', methods = ['GET'])
def api_esp_get():
    if request.method == 'GET':
        status, data = db.get_Esp()
        return jsonify({'status': status, 'data': data, 'message': 'LISTA DE ESPECIALIDADES'})
    

@app.route('/api/esp', methods = ['POST'])
def api_esp_post():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Esp(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})


# Rutas Curso

@app.route('/api/curso', methods = ['GET'])
def api_curso_get():
    if request.method == 'GET':
        status, data = db.get_Cursos()
        return jsonify({'status': status, 'data': data, 'message': 'LISTA DE CURSOS'})
    

@app.route('/api/curso', methods = ['POST'])
def api_curso_post():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Curso(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})

