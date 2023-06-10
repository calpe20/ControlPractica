from app import app
from app.gestor import *
from flask import request, jsonify


@app.route('/api/listalum>', methods = ['GET'])
def api_alumno_get():
    if request.method == 'GET':
        status, data = db.get_Alumnos()
        return jsonify({'status': status, 'message': 'RELACION DE ALUMNOS', 'data': data})
    #return jsonify({'message': 'Lista de alumnos'})


@app.route('/api/alumno', methods=['POST'])
def api_alumno_post():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Alumno(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Metodo no permitido'})


@app.route('/api/editalum', methods = ['PUT'])
def api_alumno_put():
    if request.method == 'PUT':
        data = request.json
        id = data['id']
        status, data = db.edit_Alumno(id, data)
        return jsonify({'status': status, 'data': data})

