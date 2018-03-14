from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re 
import hashlib # imports the md5 module to generate a hash
import os, binascii # include this at the top of your file

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'login_and_registration')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/register', methods=['POST'])
def add():
    j=0
    if len(request.form['first_name']) < 2:
        flash("First Name must have at least 2 characters!")
        j+=1
    elif any(char.isdigit() for char in request.form['first_name'])==True:
        flash("First Name cannot contain numbers!")
        j+=1

    if len(request.form['last_name']) < 2:
        flash("Last Name must have at least 2 characters!")
        j+=1
    elif any(char.isdigit() for char in request.form['last_name'])==True:
        flash("Last Name cannot contain numbers!")
        j+=1

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        j+=1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        j+=1
    else:
       query = "SELECT email FROM users"
       emails_list = mysql.query_db(query)
       for i in emails_list:
           if i['email'] == request.form['email']:
               flash("Email Already Exists!")        

    if len(request.form['password']) < 0:
        flash("Password cannot be blank!")
        j+=1
    elif len(request.form['password']) < 0 :
        flash("Password must be longer than 8 characters!")
        j+=1

    if len(request.form['password_confirmation']) < 1:
        flash("Password Confirmation cannot be blank!")
        j+=1
    elif request.form['password_confirmation']!=request.form['password']:
        flash("Passwords do not match!")
        j+=1

    if j>0:
        session['login'] = False
        return redirect('/')
    elif j==0:
        salt = binascii.b2a_hex(os.urandom(15))        
        password =  hashlib.md5(request.form['password'].encode() + salt ).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
        data = { 'first_name':request.form['first_name'], 'last_name':request.form['last_name'], 'email':request.form['email'], 'password':password , 'salt':salt}
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    j=0
    query = "SELECT email, password , salt FROM users"
    emails_list = mysql.query_db(query)
    for i in emails_list:
        if i['email'] == request.form['email'] and i['password'] == hashlib.md5(request.form['password'].encode() + i['salt'].encode() ).hexdigest():
            return redirect('/success')
    flash("Wrong Email Password combination!")
    session['login'] = True
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')   



app.run(debug=True)