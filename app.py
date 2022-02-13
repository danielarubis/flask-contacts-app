from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, flash #importamos módulos instalados
from flask_mysqldb import MySQL

#Mysql conect
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Quentin123' #cambiar a palabra reservada 'PASSWORD'
app.config['MYSQL_DB'] = 'flaskcontacts' #database
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/') #ruta inicial
def Index():
  return render_template('index.html') #si un user visita el route inicial se encontrará con este msj

@app.route('/add_contact', methods=['POST']) #ruta para agregar contacto
def add_contact():
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor() #cursor: saber donde está la conexión
    cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email)) # Escribimos la consulta en MySql
    mysql.connection.commit() # Ejecutamos la consulta en MySql
    flash('Contact Added Successfully')
    return redirect(url_for('Index'))

@app.route('/edit') #ruta para editar contacto
def edit_contact():
  return 'Edit contact'

@app.route('/delete') #ruta para eliminar contacto
def delete_contact():
  return 'Delete contact'

if __name__ == '__main__':
  app.run(port = 3000, debug = True)

