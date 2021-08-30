from flask import Flask, redirect, render_template, request, session, make_response, jsonify
from helpers import login_required, getNews, searchNews
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3 as sql
from newsapi import NewsApiClient
import time

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
	data = getNews()
	session["pages"] = int(data["totalResults"]/20)
	session["category"] = "general"
	print("Total Result", data["totalResults"])
	data = data["articles"]
	return render_template("index.html", data=data)


@app.route('/load')
def load():
	time.sleep(0.2)
	if request.args:
		page = int(request.args.get("p"))
		if page+1 > session["pages"]:
			print("No more posts")
			res = make_response(jsonify({}), 200)
		else:
			print(page)
			print(session["pages"])
			newsapi = NewsApiClient(api_key='e4d87e0f7a344caab7bb41c4f7318e84')
			top_headlines = newsapi.get_top_headlines(language='en', page_size=10, page=page+1, category=session["category"])
			res = make_response(jsonify(top_headlines), 200)
	return res

@app.route('/category/<ext>')
def category(ext):
	newsapi = NewsApiClient(api_key='e4d87e0f7a344caab7bb41c4f7318e84')
	data = newsapi.get_top_headlines(language='en', page_size=10, category=ext)
	session["category"] = ext
	data = data["articles"]
	return render_template("index.html", data=data)

@app.route('/search', methods=["POST"])
def search():
	search = request.form.get("search-input")
	print(search)
	if search != None:
		data = searchNews(search)
		session["pages"] = int(data["totalResults"]/20)
		data = data["articles"]
		return render_template("search.html", data=data)

# @app.route('/login', methods=["GET", "POST"])
# def login():
# 	## LOGIN THE USER

# 	session.clear()

# 	if request.method == "POST":
# 		with sql.connect("project.db") as db:
# 			db.row_factory = sql.Row
# 			cur = db.cursor()
# 			cur.execute("SELECT * FROM users WHERE name = ?",[request.form['username']])
# 			rows = cur.fetchall()
# 			if len(rows) == 0 or not check_password_hash(rows[0]["password"], request.form.get("password")):
# 				return render_template("login.html", msg="No Account with registered with that Username and Password")
# 			else:
# 				session["user_id"] = rows[0]["id"]
# 				return redirect('/')
# 	else:
# 		return render_template("login.html")

# @app.route('/register', methods=["GET", "POST"])
# def register():
# 	#REGISTER AN ACCOUNT FOR THE USER

# 	if request.method == "GET":
# 		return render_template("register.html")
# 	else:
# 		username = request.form.get("username")
# 		password = request.form.get("password")
# 		pass_hash = generate_password_hash(password)
# 		with sql.connect("project.db") as db:
# 			cur = db.cursor()
# 			cur.execute("SELECT * FROM users WHERE name = ?", [username])
# 			row = cur.fetchall()
# 			if len(row) != 0:
# 				return render_template("register.html",msg="Account with Username already exists!")
# 			cur.execute("INSERT INTO users (name,password) VALUES (?,?)",(username,pass_hash))
# 			return redirect("/")


# @app.route("/logout")
# def logout():
#     # Forget any user_id
#     session.clear()

#     # Redirect user to login form
#     return redirect("/")

if __name__=='__main__':
	app.run(debug=True)