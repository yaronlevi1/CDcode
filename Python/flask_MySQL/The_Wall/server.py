from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re 
import hashlib # imports the md5 module to generate a hash
import os, binascii # include this at the top of your file

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'the_wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/test')
def test():
    print("testing place")
    query = "SELECT * from users "
    sss= mysql.query_db(query)
    print(sss)
    return redirect('/') 

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

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")
        j+=1
    elif len(request.form['password']) < 1 :
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
        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    j=0
    query = "SELECT email, password , salt FROM users"
    emails_list = mysql.query_db(query)
    for i in emails_list:
        if i['email'] == request.form['email'] and i['password'] == hashlib.md5(request.form['password'].encode() + i['salt'].encode() ).hexdigest():
            query = "SELECT user_id, first_name FROM users WHERE email = :email"
            zzz = mysql.query_db(query ,{ 'email':request.form['email']})
            session['user_id']    = zzz[0]['user_id']
            session['first_name'] = zzz[0]['first_name']
            return redirect('/wall')
    flash("Wrong Email Password combination!")
    session['login'] = True
    return redirect('/')


@app.route('/logoff', methods=['POST'])
def logoff():
    return redirect('/')

@app.route('/wall')
def wall():
    query = "SELECT CONCAT(users.first_name, ' ',users.last_name) AS name, messages.message_id, messages.user_id, \
            messages.message, date_format( messages.created_at, '%M %D %Y') AS date \
            FROM messages \
            JOIN users ON messages.user_id = users.user_id \
            ORDER BY messages.created_at "
    session['messages'] = mysql.query_db(query)
    # print(len(session['messages']))
    # print(session['messages'][0]['name'])
    # print(session['messages'][0]['message_id'])
    # print(session['messages'][0]['user_id'])
    # print(session['messages'][0]['message'])
    # print(session['messages'][0]['date'])
    query = "SELECT CONCAT(users.first_name, ' ',users.last_name) AS name, comments.message_id, \
            comments.comment, date_format( comments.created_at, '%M %D %Y') AS date \
            FROM comments \
            JOIN users ON comments.user_id = users.user_id \
            ORDER BY comments.message_id, comments.created_at"
    session['comments'] = mysql.query_db(query)
    # print(session['comments'][0]['name'])
    # print(session['comments'][0]['message_id'])
    # print(session['comments'][0]['comment'])
    # print(session['comments'][0]['date'])
    return render_template('wall.html')   
@app.route('/newmessage', methods=['POST'])
def newmessage():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {  'user_id': session['user_id'] ,'message':request.form['message']}
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/newcomment', methods=['POST'])
def newcomment():    
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
    data = { 'message_id':request.form['message_id'],  'user_id': session['user_id'] ,'comment':request.form['comment']}
    mysql.query_db(query, data)
    return redirect('/wall')


app.run(debug=True)