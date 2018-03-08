from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
  session['count'] +=1
  return render_template("index.html")

@app.route('/two')
def two():
  session['count'] +=1
  return redirect('/')

@app.route('/reset')
def reset():
  session['count'] = 0
  return redirect('/')
  
app.run(debug=True)
