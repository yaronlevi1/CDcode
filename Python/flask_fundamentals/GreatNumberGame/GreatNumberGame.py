from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  #session['count'] =0
  session['count'] +=1
  if session['count']==1:
    session["rand"]=random.randrange(0, 101) 
    session["guess"] = None
  print(session["count"])
  print(session["rand"])
  print(session["guess"])
  return render_template("index.html")

 
@app.route('/guess', methods=['POST'])
def guess():
  session["guess"] = int(request.form["userguess"])
  return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
  session['count'] = 0
  return redirect('/')

app.run(debug=True)
