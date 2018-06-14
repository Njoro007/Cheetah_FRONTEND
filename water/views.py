from flask import Flask, render_template, redirect, request, url_for, json, session
import os

from water import *

@app.route('/')
@login_required
def index():
    # load local json for water pans
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
    data = json.load(open(json_url))
    # return render_template('showjson.jade', data=data)
    return render_template('index.html', data=data)

# proposals
@app.route("/proposals")
@login_required
def proposals():
	return render_template("proposals.html")

@app.route("/waterpans")
@login_required
def waterpans():
	# load local json for water pans
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
    data = json.load(open(json_url))
    json_url_location = os.path.join(SITE_ROOT, "static/files", "location.json")
    location = json.load(open(json_url_location))
    return render_template("waterpans.html", data=data, location=location)


@app.route("/apan/<string:name>", methods=['GET'])
@login_required
def apan(name):
	# load local jsons
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/files", "capacity.json")
	data = json.load(open(json_url))
	json_url_location = os.path.join(SITE_ROOT, "static/files", "location.json")
	location = json.load(open(json_url_location))
	json_url_pan = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
	waterpan = json.load(open(json_url_pan))
	json_url_user = os.path.join(SITE_ROOT, "static/files", "users.json")
	user = json.load(open(json_url_user))

	return render_template("apan.html", name=name, data=data, location=location, waterpan=waterpan, user=user)

@app.route("/addpan", methods=["POST", "GET"])
@login_required
def addpan():

	if request.method == "POST":
		return render_template("addpan.html")
	elif request.method == "GET":
		return render_template("addpan.html")

@app.route("/editpan", methods=['GET', 'POST'])
@login_required
def editpan():
	if request.method == "GET":
		# load local json for water pans
		SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
		json_url = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
		data = json.load(open(json_url))
		return render_template("editpan.html", data=data)
	return render_template("editpan.html")

@app.route("/login", methods=["GET", "POST"])
def login():

	session.clear()
	if request.method == "GET":
		return render_template("login.html")
	elif request.method == "POST":
		username= request.form['username']
		password = request.form['password']
		# load local json for water pans
		SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
		json_url_credentials = os.path.join(SITE_ROOT, "static/files", "credentials.json")
		credentials = json.load(open(json_url_credentials))
		# json_url = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
		# data = json.load(open(json_url))
		if credentials['username'] == username:
			session['username'] = username
			return redirect(url_for('index'))
		else:
			return render_template("login.html")