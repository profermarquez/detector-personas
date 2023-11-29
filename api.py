from flask import Flask
import sqlite3
from pyngrok import ngrok

def connect_to_db():
    conn = sqlite3.connect('personas.db')
    return conn

def obtener_personas(conn):
    ipersona = {"codigo": "error"}
    try:
        cur = conn.cursor()
        cur.execute('SELECT SUM(cantidad) FROM personas')
        ipersona = list(cur)
        print(list(cur))
    except Exception as error:
        print(error, "Error en la consulta de personas db")
    return ipersona

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World</p>'

@app.route('/api/get_personas2')
def nroPer():
    return '5'

@app.route('/api/get_personas')
def obtener():
    print('pasa')
    conn = connect_to_db()
    return obtener_personas(conn)

if __name__ == '__main__':
    public_url = ngrok.connect(port=5000)
    print(' * ngrok tunnel "{}" -> "http://127.0.0.1:{}/"'.format(public_url, 5000))
    app.run(debug=True, host='localhost',port=5000)