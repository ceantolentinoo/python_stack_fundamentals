from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("first_flask")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/add_pet", methods=["POST"])
def add_pet():
    print(request.form)
    mysql = connectToMySQL("first_flask")
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
    query = "INSERT INTO pets(name, type) VALUES (%(name)s, %(type)s);"
    data = {
        "name": request.form['name'],
        "type": request.form['type'],
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)