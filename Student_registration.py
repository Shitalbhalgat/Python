from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index3.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    mobile = request.form.get("mobile")
    age = request.form.get("age")
    dob = request.form.get("dob")
    gender = request.form.get("gender")
    course = request.form.get("course")
    address = request.form.get("address")
    city = request.form.get("city")

    hobbies = request.form.getlist("hobbies")

    return render_template(
        "success.html",
        name=name,
        email=email,
        password=password,
        mobile=mobile,
        age=age,
        dob=dob,
        gender=gender,
        course=course,
        address=address,
        city=city,
        hobbies=hobbies
    )


if __name__ == "__main__":
    app.run(debug=True)