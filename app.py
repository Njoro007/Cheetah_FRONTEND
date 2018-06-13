from flask import Flask, render_template, redirect, request, url_for, json
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'zyxwvutsrqponmlkj'

app.debug = True

# root
@app.route('/')

def index():
    # load local json for water pans
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
    data = json.load(open(json_url))
    # return render_template('showjson.jade', data=data)
    return render_template('index.html', data=data)

# proposals
@app.route("/proposals")
def proposals():
	return render_template("proposals.html")

@app.route("/waterpans")
def waterpans():
	return render_template("waterpans.html")


@app.route("/apan/<string:name>", methods=['GET'])
def apan(name):
	# load local json for water pans
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/files", "waterpan.json")
	data = json.load(open(json_url))
	return render_template("apan.html", name=name)

@app.route("/addpan", methods=["POST", "GET"])
def addpan():

	if request.method == "POST":
		return render_template("addpan.html")
	elif request.method == "GET":
		return render_template("addpan.html")

@app.route("/editpan", methods=['GET', 'POST'])
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
			return redirect(url_for('index'))
		else:
			return render_template("login.html")
if __name__ == '__main__':
    app.run(debug=True)