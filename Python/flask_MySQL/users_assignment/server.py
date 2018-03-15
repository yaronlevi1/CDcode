from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'users_assignemnt')


@app.route('/users')
def index():
    query = "SELECT user_id, CONCAT(first_name,' ',last_name) AS name, email , DATE_FORMAT(created_at, '%b %D %Y') AS date FROM users" 
    all_users = mysql.query_db(query) 
    print(all_users)
    return render_template('index.html', all_users=all_users) 

@app.route('/users/new')
def new():
    return render_template('new.html') 


@app.route('/adduser', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) \
                       VALUES (:first_name, :last_name, :email , NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'email': request.form['email'],
           }
    mysql.query_db(query, data)   
    return redirect('/users')

@app.route('/users/<user_id>')
def show(user_id):
    query = "SELECT user_id, CONCAT(first_name,' ',last_name) AS name, email , DATE_FORMAT(created_at, '%b %D %Y') AS date \
          FROM users \
          WHERE user_id=:user_id " 
    user = mysql.query_db(query, {'user_id': user_id}) 
    print(user)
    return render_template('show.html', user=user[0]) 

@app.route('/delete/<user_id>')
def delete(user_id):
    query = "DELETE FROM users WHERE user_id=:user_id " 
    user = mysql.query_db(query, {'user_id': user_id}) 
    print(user)
    return redirect('/users')

@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = "SELECT user_id, first_name, last_name, email  \
          FROM users \
          WHERE user_id=:user_id " 
    user = mysql.query_db(query, {'user_id': user_id}) 
    print(user)
    return render_template('edit.html', user=user[0])


@app.route('/update', methods=['POST'])
def update():
    query = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW()  WHERE user_id=:user_id" 
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'user_id': request.form['user_id']}
    mysql.query_db(query, data) 
    return redirect('/users')

app.run(debug=True)