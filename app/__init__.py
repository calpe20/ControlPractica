from flask import Flask
from app.gestor import *

app = Flask('__main__')


@app.route('/')
def index():
    return 'Hola Mundo'


@app.route('/admin')
def admin():
    return 'Admin eres tu?'


if __name__ == '__main__':
    app.run()
