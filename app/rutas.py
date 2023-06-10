from app import app
from app.gestor import *
from flask import request, jsonify


@app.route('/api/listalum>', methods = ['GET'])
def api_alumno_get():
    if request.method == 'GET':
        data = db.get_Alumnos()
        return jsonify(data)
    return jsonify({'message': 'Lista de alumnos'})


@app.route('/api/alumno', methods=['POST'])
def api_alumno_post():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Alumno(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Metodo no permitido'})
    '''elif request.method == 'GET':
        #data = db.get_Alumnos()
        message = db.get_Alumnos()
        return jsonify({'message': message})
    return jsonify({'message': 'Lista de alumnos'})'''
    

