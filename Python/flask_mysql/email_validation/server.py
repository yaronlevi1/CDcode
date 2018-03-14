from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re 


app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'email_validation')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/add_email', methods=['POST'])
def add():
    email = request.form['email']
    if len(email) < 1:
        flash("Email cannot be blank!") 
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
       flash("Invalid Email Address!")
       return redirect('/')
    else:
       query = "SELECT email FROM emails"
       emails_list = mysql.query_db(query)
       for i in emails_list:
           if i['email'] == email:
               flash("Email Already Exists!")
               return redirect('/')
       flash("The email you entered ("+ email+ ") is a VALID email address! Thank you!")
       query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email , NOW(), NOW())"
       data = { 'email': email }
       mysql.query_db(query, data)
       return redirect('/success')
            
@app.route('/success')
def success():
    query = "SELECT email_id, email, created_at FROM emails" 
    emails = mysql.query_db(query) 
    return render_template('success.html', all_emails=emails)   
 
@app.route('/delete', methods=['POST'])
def delete():
    query = "DELETE FROM emails WHERE email_id=:id"
    data = { 'id':  request.form['delete'] }
    mysql.query_db(query, data)
    return redirect('/success')


app.run(debug=True)