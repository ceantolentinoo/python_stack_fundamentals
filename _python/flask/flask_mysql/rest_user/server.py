from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    mysql = connectToMySQL("first_flask")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("index.html", users=users)

@app.route('/new')
def create_user_page():
    return render_template("new.html")

@app.route('/edit/<userId>')
def edirt_user_page(userId):
    mysql = connectToMySQL("first_flask")
    query = "SELECT * FROM users WHERE id = %(userId)s;"
    data = {
        'userId': userId
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("edit.html", user=user)

@app.route('/show/<userId>')
def show_user(userId):
    mysql = connectToMySQL("first_flask")
    query = "SELECT * FROM users WHERE id = %(userId)s;"
    data = {
        'userId': userId
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("show.html", id=userId, this_user = user)

@app.route('/edit_user', methods=['POST'])
def edit_user():
    mysql = connectToMySQL("first_flask")
    query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(userId)s"
    data = {
        'userId': request.form['userId'],
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route('/create', methods=['POST'])
def add_user():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(request.form['fname']) < 1:
        flash("Please enter a first name", "fname")
    if len(request.form['lname']) < 1:
        flash("Please enter a last name", "lname")
    if len(request.form['email']) < 1:
        flash("Please enter a email", "email")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!!", "email")
    
    if not '_flashes' in session.keys():
        mysql = connectToMySQL("first_flask")
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(fname)s, %(lname)s, %(email)s)"
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email']
        }
        flash("Friend successfully added!")
        new_user = mysql.query_db(query, data)
        return redirect("/")
    else:
        return redirect("/new")
    

@app.route('/delete/<userId>')
def delete_user(userId):
    mysql = connectToMySQL("first_flask")
    query = "DELETE FROM users where id = %(userId)s"
    data = {
        'userId': userId
    }
    user = mysql.query_db(query, data)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)