from app import app
from app.gestor import *
from flask import request, jsonify


@app.route('/api/alumno', methods=['POST'])
def api_alumno_get():
    if request.method == 'POST':
        data = request.json
        status, message = db.new_Alumno(data)
        return jsonify({'status': status, 'message': message})
    return jsonify({'status': False, 'message': 'Metodo no permitido'})
