from flask import Flask, render_template, request, redirect, url_for 

app = Flask(__name__)

email=""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=['POST', 'GET'])
def signin():
    if request.method == "POST":
        try:
            global email
            email = request.form["email"]
            password = request.form["password"]
            # print(email)
            # print(password)
            return redirect(url_for("home"), code=302)
        except:
            return render_template("signin.html")
    elif request.method == "GET":
        return render_template("signin.html")
    else:
        return render_template("signin.html")

@app.route("/home")
def home():
    print(f"email is {email}")
    return render_template("home.html", username=email)

@app.route("/register")
def register():
    return "you are now attempting to register a new user"

app.run(host="0.0.0.0", debug=True)