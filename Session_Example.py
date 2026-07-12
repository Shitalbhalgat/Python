from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "mysecretkey"

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/check", methods=["POST"])
def check():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":

        session["user"] = username

        return redirect(url_for("dashboard"))

    return "Invalid Login"


@app.route("/dashboard")
def dashboard():

    if "user" not in session:

        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)