from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninja():
  return render_template("ninja.html")


@app.route('/ninja/<nincolor>')
def ninja2(nincolor):
  if nincolor == "blue":
    ninpic = "leonardo"
  elif nincolor == "red":
    ninpic = "raphael"
  elif nincolor == "orange":
    ninpic = "michelangelo"
  elif nincolor == "purple":
    ninpic = "donatello"
  else:
    ninpic = "notapril"
  print(nincolor, ninpic )
  return render_template("specific_ninja.html", ninpic=ninpic)










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