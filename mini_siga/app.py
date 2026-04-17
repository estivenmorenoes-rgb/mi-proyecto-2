from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

def crear_bd():
    conexion = sqlite3.connect("siga.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aulas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            capacidad INTEGER
        )
    """)
    
    conexion.commit()
    conexion.close()


@app.route("/", methods=["GET", "POST"])
def inicio():
    conexion = sqlite3.connect("siga.db")
    cursor = conexion.cursor()

    if request.method == "POST":
        nombre = request.form["nombre"]
        capacidad = request.form["capacidad"]

        cursor.execute("INSERT INTO aulas (nombre, capacidad) VALUES (?, ?)", (nombre, capacidad))
        conexion.commit()

    cursor.execute("SELECT * FROM aulas")
    aulas = cursor.fetchall()

    conexion.close()

    return render_template("index.html", aulas=aulas)

crear_bd()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))