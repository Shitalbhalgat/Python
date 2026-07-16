from flask import Flask, render_template
from student import student_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(student_bp)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
