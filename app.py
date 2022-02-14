from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, flash #importamos módulos instalados
from flask_mysqldb import MySQL

#Mysql conect
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Quentin123'
app.config['MYSQL_DB'] = 'flaskcontacts' #database
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/') #ruta inicial
def Index():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contacts')
  data = cur.fetchall() #visualizar los datos
  return render_template('index.html', contacts = data) #si un user visita el route inicial se encontrará con este msj

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

@app.route('/edit/<id_contacts>') #ruta para editar contacto
def get_contact(id_contacts):
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contacts WHERE id_contacts = %s', (id_contacts))
  data = cur.fetchall()
  return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id_contacts>', methods=['POST'])
def update_contacts(id_contacts):
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("""
      UPDATE contacts
      SET fullname = %s,
          phone = %s,
          email = %s
      WHERE id_contacts = %s
    """, (fullname, phone, email, id_contacts))
    mysql.connection.commit()
    flash('Contact Updated Successfully')
    return redirect(url_for('Index'))

@app.route('/delete/<string:id_contacts>') #ruta para eliminar contacto
def delete_contact(id_contacts):
  cur = mysql.connection.cursor()
  cur.execute('DELETE FROM contacts WHERE id_contacts = {0}'.format(id_contacts))
  mysql.connection.commit()
  flash('Contact Removed Successfully')
  return redirect(url_for('Index'))


if __name__ == '__main__':
  app.run(port = 3000, debug = True)

