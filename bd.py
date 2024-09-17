from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="ochoa"
)

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    cursor = db.cursor()
    NOMBRE = request.form['NOMBRE']
    CORREO = request.form['CORREO']
    FECHA = request.form['FECHA']
    HORA = request.form['HORA']
    PERSONAS = request.form['PERSONAS']
        
    sql = "INSERT INTO registro (Nombre,Correo,Fecha,Hora,Personas) VALUES (%s,%s,%s,%s,%s)" # Cambia 'nombre_tabla' y 'nombre_campo' por los nombres reales de tu tabla y campo en la base de datos
    cursor.execute(sql, (NOMBRE,CORREO,FECHA,HORA,PERSONAS))
    db.commit()
    cursor.close()
    print("Datos insertados correctamente")
    return 'Datos insertados correctamente'

if __name__ == '__main__':
    app.run(debug=True)