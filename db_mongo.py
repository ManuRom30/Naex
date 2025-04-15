# db_mongo.py
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
# Conexión a MongoDB local
client = MongoClient(mongo_uri)
db = client["Naex"]
estudiantes = db["estudiantes"]
clases = db["clases"]
tutores = db["tutores"]

def agregar_estudiante(nombre, clases_compradas, documento, correo ):
    nuevo_estudiante = {
        "nombre": nombre,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
        "clases_compradas": int(clases_compradas),
        "clases_consumidas": 0,
        "documento": documento,
        "correo": correo
    }
    estudiantes.insert_one(nuevo_estudiante)

def obtener_estudiantes():
    return list(estudiantes.find())

def obtener_tutores():
    return list(tutores.find())

def registrar_clase(estudiante_id, tutor_id, fecha):
    estudiante_id = ObjectId(estudiante_id)
    tutor_id = ObjectId(tutor_id)

    estudiante = estudiantes.find_one({"_id": estudiante_id})
    tutor = tutores.find_one({"_id": tutor_id})
    clases.insert_one({
        "nombreEstudiante": estudiante['nombre'],
        "fecha_clase": datetime.strptime(fecha, "%Y-%m-%d"),
        "nombreTutor":tutor['nombre']
    })
    estudiantes.update_one(
        {"_id": estudiante_id},
        {"$inc": {"clases_consumidas": 1}}
    )

def agregar_tutor(nombre, correo, especialidad, documento, telefono):
    nuevo_tutor = {
        "nombre": nombre,
        "correo": correo,
        "documento": documento,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
        "especialidad": especialidad,
        "clases_impartidas": 0,
        "telefono": telefono
    }
    tutores.insert_one(nuevo_tutor)
