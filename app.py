from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'zyxwvutsrqponmlkj'

app.debug = True

# root
@app.route('/')

def index():
    return render_template('index.html')

# proposals
@app.route("/proposals")
def proposals():
	return render_template("proposals.html")

@app.route("/waterpans")
def waterpans():
	return render_template("waterpans.html")


@app.route("/apan")
def apan():
	return render_template("apan.html")

@app.route("/addpan", methods=["POST", "GET"])
def addpan():

	if request.method == "POST":
		return render_template("addpan.html")
	elif request.method == "GET":
		return render_template("addpan.html")

@app.route("/editpan")
def editpan():
	return render_template("editpan.html")

if __name__ == '__main__':
    app.run(debug=True)