from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():

    return redirect("/about")

@app.route("/about")
def about():

    return "<h2>Welcome to About Page</h2>"

if __name__=="__main__":
    app.run(debug=True)