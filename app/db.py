import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("ERROR: La variable de entorno MONGO_URI no está definida.")

client = MongoClient(mongo_uri)

db = client["usuarios_db"]
usuarios = db["usuarios"]
