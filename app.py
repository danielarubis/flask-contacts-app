from crypt import methods
from flask import Flask, render_template, request #importamos módulos instalados
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts' #database

mysql = MySQL(app)

@app.route('/') #ruta inicial
def Index():
  return render_template('index.html') #si un user visita el route inicial se encontrará con este msj

@app.route('/add_contact', methods=['POST']) #ruta para agregar contacto
def add_contact():
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    print(fullname)
    print(phone)
    print(email)
    return 'Received'

@app.route('/edit') #ruta para editar contacto
def edit_contact():
  return 'Edit contact'

@app.route('/delete') #ruta para eliminar contacto
def delete_contact():
  return 'Delete contact'

if __name__ == '__main__':
  app.run(port = 3000, debug = True)

