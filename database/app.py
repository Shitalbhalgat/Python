from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


#  Insert Student 
@app.route("/save", methods=["POST"])
def save():

    name = request.form.get("name")
    email = request.form.get("email")
    course = request.form.get("course")

    con = get_connection()
    cursor = con.cursor()

    sql = """ INSERT INTO registration(name,email,course)VALUES(%s,%s,%s)"""
    values = (name, email, course)

    cursor.execute(sql, values)
    con.commit()
    cursor.close()
    con.close()
    return redirect(url_for("students"))


#  Display Students

@app.route("/students")
def students():

    con = get_connection()

    cursor = con.cursor()

    cursor.execute("SELECT * FROM registration")

    students = cursor.fetchall()

    cursor.close()

    con.close()

    return render_template("students.html", students=students)


# Edit Student

@app.route("/edit/<int:id>")
def edit(id):

    con = get_connection()

    cursor = con.cursor()

    sql = "SELECT * FROM registration WHERE id=%s"

    cursor.execute(sql, (id,))

    student = cursor.fetchone()

    cursor.close()

    con.close()

    return render_template( "edit.html",student=student)

#  Update Student

@app.route("/update", methods=["POST"])
def update():

    id = request.form.get("id")
    name = request.form.get("name")
    email = request.form.get("email")
    course = request.form.get("course")

    con = get_connection()

    cursor = con.cursor()

    sql = """ UPDATE registration SET  name=%s,email=%s, course=%s WHERE id=%s """

    values = (name,email, course, id)

    cursor.execute(sql, values)

    con.commit()

    cursor.close()

    con.close()

    return redirect(url_for("students"))


# - Delete Student 

@app.route("/delete/<int:id>")
def delete(id):

    con = get_connection()

    cursor = con.cursor()

    sql = "DELETE FROM registration WHERE id=%s"

    cursor.execute(sql, (id,))

    con.commit()

    cursor.close()

    con.close()

    return redirect(url_for("students"))

# Run Flask 
if __name__ == "__main__":
    app.run(debug=True)