from flask import Flask, render_template, request, make_response

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Save Cookie
@app.route("/save", methods=["POST"])
def save():

    username = request.form.get("username")

    # Create Response
    response = make_response(render_template("welcome.html", username=username))

    # Create Cookie (Valid for 60 seconds)
    response.set_cookie("username", username, max_age=60)

    return response


# Read Cookie
@app.route("/profile")
def profile():

    username = request.cookies.get("username")

    if username:
        return render_template("cookie.html", username=username)

    return "<h2>Cookie Not Found</h2>"


# Delete Cookie
@app.route("/logout")
def logout():

    response = make_response("<h2>Cookie Deleted Successfully</h2>")

    response.delete_cookie("username")

    return response


if __name__ == "__main__":
    app.run(debug=True)