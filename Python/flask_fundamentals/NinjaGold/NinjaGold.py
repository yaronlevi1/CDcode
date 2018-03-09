from flask import Flask, render_template, request, redirect, session
import random 
import datetime


app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  session['count'] +=1
  if session['count']==1:
    session["score"]=0  
    session["history"] = [] 
  return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
  session["building"]=request.form["building"]
  if session["building"] == "Farm":
     session["delta"]=random.randrange(10, 21) 
  if session["building"] == "Cave":
    session["delta"]=random.randrange(5, 11) 
  if session["building"] == "House":
    session["delta"]=random.randrange(2, 6) 
  if session["building"] == "Casino":
    session["delta"]=random.randrange(-50, 51) 
  session["score"]+=session["delta"]
  session["history"].append ( [ session["count"], session["delta"] , session["building"], datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") ])
  print(session["history"])
  print(len(session["history"]))
  return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
  session['count'] = 0
  return redirect('/')

app.run(debug=True)

# @app.route('/')
# def index():
#   #session['count'] =0
#   session['count'] +=1
#   if session['count']==1:
#     session["rand"]=random.randrange(0, 101) 
#     session["guess"] = None
#   print(session["count"])
#   print(session["rand"])
#   print(session["guess"])
#   return render_template("index.html")

 
# @app.route('/guess', methods=['POST'])
# def guess():
#   session["guess"] = int(request.form["userguess"])
#   return redirect('/')


# @app.route('/reset', methods=['POST'])
# def reset():
#   session['count'] = 0
#   return redirect('/')


