from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 
 
app = Flask(__name__)
 
 
app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dbpv'
app.config['MYSQL_DB'] = 'dbsystem'
 
mysql = MySQL(app)
 
@app.route('/')
@app.route('/mainpage' , methods =['GET', 'POST'])
def mainpage():
    msg = ''
    return render_template('mainpage.html', msg=msg)

@app.route('/profile' , methods =['GET', 'POST'])
def profile():
    msg = ''
    return render_template('profile.html', msg=msg)

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'passwort' in request.form:
        email = request.form['email']
        passwort = request.form['passwort']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Client_user WHERE email = % s AND passwort = % s', (email, passwort, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['UserID'] = account['UserID']
            session['email'] = account['email']
            session['Fullname'] = account['Fullname']
            session['bankclient'] = account['bankclient']
            session['address'] = account['address']
            session['services'] = account['services']
            session['contact'] = account['contact']

            msg = 'Logged in successfully !'
            return render_template('profile.html', msg = msg)
        else:
            msg = ' Email ou Senha errados !'
    return render_template('login.html', msg = msg)
 
@app.route('/logout')

def logout():
    session.pop('loggedin', None)
    session.pop('UserID', None)
    session.pop('email', None)
    return redirect(url_for('login'))
 
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'passwort' in request.form and 'email' in request.form :
        email = request.form['email']
        passwort = request.form['passwort']
        Fullname = request.form['Fullname']
        cpf = request.form['CPF']
        Age = request.form['Age']
        bankclient =request.form['bankclient']
        services =request.form['services']
        skills = request.form['skills']
        address = request.form['address']


        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Client_user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Já existe!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Email invalido !'
        elif not email or not passwort :
            msg = 'Preencha !'
        else:
            cursor.execute('INSERT INTO Client_user (Fullname, cpf, Age, email, passwort, bankclient, services, skills,address ) VALUES (% s, % s, % s, % s, %s, % s , % s , % s, %s  )', (Fullname, cpf, Age, email, passwort, bankclient, services, skills,address  ))
            mysql.connection.commit()
            msg = 'Você foi registrado!'
            return render_template('login.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Formulário não preenchido adequadamente !'
    return render_template('register.html', msg = msg)



