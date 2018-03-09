from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"


@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
  j=0
  result = request.form
  if len(request.form['name']) < 1:
    flash("Name cannot be blank!")
    j+=1
  if len(request.form['Comment']) < 1:
    flash("Comment cannot be blank!")
    j+=1
  if len(request.form['Comment']) >120:
    flash("Comment is too long!")
    j+=1
  if j>0:
    return redirect('/')
  else:
    return render_template("inforview.html", result=result)

@app.route('/goback', methods=['GET'])
def goback():
  return redirect('/')

app.run(debug=True)



