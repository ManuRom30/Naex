# app.py

from flask import Flask, render_template, request, redirect, url_for
from db_mongo import agregar_tutor, agregar_estudiante, obtener_estudiantes, obtener_tutores, registrar_clase
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/agregar_tutor', methods=['GET', 'POST'])
def agregar_tutor_web():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        especialidad = request.form['especialidad']
        documento = request.form['documento']
        telefono = request.form['telefono']
        agregar_tutor(nombre, correo, especialidad, documento, telefono)
        return redirect(url_for('index'))
    return render_template('agregar_tutor.html')

@app.route('/agregar_estudiante', methods=['GET', 'POST'])
def registrar_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        documento = request.form['documento']
        correo = request.form['correo']
        clases = int(request.form['clases_compradas'])
        agregar_estudiante(nombre, clases, documento, correo)
        return redirect(url_for('index'))
    return render_template('agregar_estudiante.html')

@app.route("/registrar_clase", methods=["GET", "POST"])
def vista_registrar_clase():
    if request.method == 'GET':
        estudiantes = obtener_estudiantes()
        tutores = obtener_tutores()
        return render_template("agregar_clase.html", estudiantes=estudiantes, tutores=tutores)
        
    if request.method == 'POST':

        estudiante_id = request.form["estudiante_id"]
        tutor_id = request.form["tutor_id"]
        fecha = request.form["fecha"]
        registrar_clase(estudiante_id, tutor_id, fecha)

        estudiantes = obtener_estudiantes()
        tutores = obtener_tutores()

        return render_template("agregar_clase.html", estudiantes=estudiantes, tutores=tutores)

if __name__ == '__main__':
    app.run(debug=True)
