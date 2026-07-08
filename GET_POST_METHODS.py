from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return "Display Login Form"

    if request.method == "POST":
        return "Process Login"

if __name__ == "__main__":
    app.run(debug=True)