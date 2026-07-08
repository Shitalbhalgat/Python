from flask import Flask, render_template

app = Flask(__name__)

@app.route("/control")
def home():

    student = {"name": "Rahul Sharma","roll": 101,"course": "Computer Engineering", "city": "Pune","marks": 82}

    subjects = ["Python", "Flask","HTML","CSS","JavaScript"]

    return render_template("index2.html",student=student,subjects=subjects )

if __name__ == "__main__":
    app.run(debug=True)