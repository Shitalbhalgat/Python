from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Get uploaded file
    file = request.files["photo"]

    # Check whether file selected or not
    if file.filename == "":

        return "No File Selected"

    # Convert filename into safe filename
    filename = secure_filename(file.filename)

    # Save file inside uploads folder
    file.save( os.path.join(  app.config["UPLOAD_FOLDER"], filename))

    return render_template( "success.html",filename=filename)

if __name__ == "__main__":
    app.run(debug=True)