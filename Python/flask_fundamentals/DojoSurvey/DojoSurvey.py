from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/formsub', methods=['POST'])
def create_user():
   print ("Got Post Info")
   result = request.form
   print(request.form)
   return render_template("inforview.html", result=result)

@app.route('/goback')
def index2():
  return render_template("index.html")

app.run(debug=True)