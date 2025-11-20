from flask import Flask, render_template, request, redirect, jsonify
from db import usuarios

app = Flask(__name__)

@app.route("/")
def register_form():
    return render_template("register.html")

@app.route("/registrar", methods=["POST"])
def register():
    nombre = request.form.get("nombre")
    dni = request.form.get("dni")
    telefono = request.form.get("telefono")

    if not nombre or not dni or not telefono:
        return jsonify({"error": "Faltan datos"}), 400

    nuevo_usuario = {
        "nombre": nombre,
        "dni": dni,
        "telefono": telefono
    }

    usuarios.insert_one(nuevo_usuario)
    return redirect("/?success=1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
