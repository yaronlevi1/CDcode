from flask import Flask, render_template, redirect, request, session, flash
import re 

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
  j=0
  result = request.form
  if len(request.form['email']) < 1:
    flash("Email cannot be blank!")
    j+=1
  elif not EMAIL_REGEX.match(request.form['email']):
      flash("Invalid Email Address!")

  if len(request.form['first_name']) < 1:
    flash("First Name cannot be blank!")
    j+=1
  elif any(char.isdigit() for char in request.form['first_name'])==True:
    flash("First Name cannot contain numbers!")
    j+=1

  if len(request.form['last_name']) < 1:
    flash("Last Name cannot be blank!")
    j+=1
  elif any(char.isdigit() for char in request.form['last_name'])==True:
    flash("Last Name cannot contain numbers!")
    j+=1

  if len(request.form['password']) < 1:
    flash("Password cannot be blank!")
    j+=1
  elif len(request.form['password']) < 9:
    flash("Password must be longer than 8 characters!")
    j+=1

  if len(request.form['password_confirmation']) < 1:
    flash("Password Confirmation cannot be blank!")
    j+=1
  elif request.form['password_confirmation']!=request.form['password']:
    flash("Passwords do not match!")
    j+=1

  if len(request.form['birthday']) < 1:
    flash("Birthday cannot be blank!")
    j+=1

  if j==0:
    flash("Thank you For submitting your information!")
  
  print(j)
  return redirect('/')


app.run(debug=True)

#   if len(request.form['Comment']) < 1:
#     flash("Comment cannot be blank!")
#     j+=1
#   if len(request.form['Comment']) >120:
#     flash("Comment is too long!")
#     j+=1
#   if j>0:
#     return redirect('/')
#   else:
#     return render_template("inforview.html", result=result)

