from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():

    return render_template("login.html")

@app.route("/check", methods=["POST"])
def check():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":

        return redirect(url_for("dashboard"))

    return "Invalid Username or Password"

@app.route("/dashboard")
def dashboard():

    return "<h2>Welcome Admin</h2>"

if __name__=="__main__":
    app.run(debug=True)