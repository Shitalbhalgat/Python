import mysql.connector

try:

    con = mysql.connector.connect( host="localhost", user="root", password="",  database="studentdb")

    if con.is_connected():

        print("Connected Successfully")

except mysql.connector.Error as e:

    print("Error :", e)

finally:

    if 'con' in locals() and con.is_connected():

        con.close()

        print("Connection Closed")