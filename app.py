from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os
import os
import dataset

db_url = "postgres://fxvwwuudxofxkv:6e3d0abfa272fd0a9c69a9ab078da49560a81f2734a50981c4d18e5da5467111@ec2-54-204-23-228.compute-1.amazonaws.com:5432/d8cdlb2l5pl69j"
db = dataset.connect(db_url)
app = Flask(__name__)
app.secret_key = os.urandom(24)
usertable = db['users']


loggedinuser = ""

@app.route('/')
def login1():
	return render_template("login.html")
@app.route('/home')
def homepage():
	return render_template('home.html')
@app.route('/register')
def registerpage():
	return render_template('userform.jinja')
@app.route("/contact")
def contact():
	return render_template("contact.html")
@app.route('/map')
def map():
	return render_template("mapp.html")
@app.route("/handlelogin", methods = ["GET","POST"])
def handlelogin():
	global loggedinuser
	username = request.form["username"]
	password = request.form["password"]
	if usertable.find_one(name=username , password=password):
		loggedinuser = True
		return render_template ("home.html")
	else:
		return("please check username or password")
def add_user(username ,password):
	if usertable.find_one(name = username):
		return ("ERROR : USER ALREADY EXISTS")
	usertable.insert(dict(name=username , password=password))
	return ("user added")

	
@app.route("/showdb")
def show_db():

	all_users = list(usertable.find())
	
	return "user table:<br>" + str(all_users) 
@app.route("/handleuser",methods =["GET","POST"])
def handle_user():
	name = request.form["username"]
	password = request.form["password"]
	add_user(name ,password)
	
	return ("user and password added")


@app.route("/userform")
def show_userform():
	return render_template ("userform.jinja")
	

if __name__ == "__main__":
    app.run(port=3000, debug = True)











