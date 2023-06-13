from app import app
from app.gestor import *
from flask import request, jsonify


# Rutas Alumno

@app.route('/api/alumno', methods = ['GET'])
def api_alumno_get():
    if request.method == 'GET':
        status, data = db.get_Alumnos()
        return jsonify({'status': status,'data': data, 'message': 'RELACION DE ALUMNOS'})
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

    
# Rutas Especialidad   

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


@app.route('/api/esp<int:id>', methods = ['PUT'])
def api_esp_put(id):
    if request.method == 'PUT':
        data = request.json
        status, message = db.edit_Esp(id, data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed'})



@app.route('/api/esp<int:id>', methods = ['DELETE'])
def api_esp_delete(id):
    if request.method == 'DELETE':
        status, message = db.delete_Esp(id)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})
                       

# Rutas Curso

@app.route('/api/curso', methods = ['GET'])
def api_curso_get():
    if request.method == 'GET':
        status, data = db.get_Curso()
        return jsonify({'status': status, 'data': data, 'message': 'LISTA DE CURSOS'})
    

@app.route('/api/curso', methods = ['POST'])
def api_curso_post():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Curso(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})


@app.route('/api/curso<int:id>', methods = ['PUT'])
def api_curso_put(id):
    if request.method == 'PUT':
        data = request.json
        status, message = db.edit_Curso(id, data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Method not allowed!'})


@app.route('/api/curso<int:id>', methods= ['DELETE'])
def api_curso_delete(id):
    if request.method == 'DELETE':
        status, message = db.delete_Curso(id)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': status, 'message': 'Method not allowed!'})


# Rutas Cursoespecialidad

@app.route('/api/cursoesp', methods = ['GET'])
def api_cursoesp_get():
    if request.method == 'GET':
        status, data = db.get_Cursoesp()
        return jsonify({'status': status,'data':  data, 'message': 'CURSO POR ESPECIALIDAD'})
        

