from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import csv

 
 
app = Flask(__name__)
 
 
app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dbpv'
app.config['MYSQL_DB'] = 'dbsystem'
 
mysql = MySQL(app)
 
@app.route('/')

@app.route('/mainpage' )
def mainpage():
    msg = ''


    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT idpost, title, description, hour_currency, service_tag, status FROM post')
    
    u = cursor.fetchall()

    data = []
    for row in u:
        data.append([    row['idpost'],
            row['title'],
            row['description'],
            row['hour_currency'],
            row['service_tag'],
            row['status'] ]
                )
    print(data)


    return render_template('mainpage.html', data=data)

#######################################################



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




@app.route('/addpost' , methods =['GET', 'POST'])
def addpost():
    msg = ''
    if not session.get('UserID'):
        msg = "Você não está logado !"
        return render_template('login.html', msg=msg)
    elif request.method == 'POST' and session.get('UserID'):
        title = request.form['title']
        description = request.form['description']
        hour_currency = request.form['hour_currency']
        service_tag = request.form['service_tag']
        status = request.form['status']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('INSERT INTO post (title, description,  service_tag, hour_currency, status) VALUES (%s, %s,  %s, %s, %s)', (title, description, service_tag, hour_currency
        , status))
        mysql.connection.commit()
        msg = "Post publicado"
        return render_template("mainpage.html", msg=msg)

    else:
        return render_template('add_post.html', msg=msg)


@app.route('/exchange', methods = ['POST'])
def exchange():
    if not session.get('UserID'):
        msg = 'Você deve estar logado'
        return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        

        
    else:
        return render_template('exchange.html')



 



