from tabnanny import check
from db import connectToMySQL
from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secret"

def check_email():
    mysql = connectToMySQL("user_db")
    query = "SELECT * FROM users where email = %(email)s"
    data = {
        'email': request.form['email']
    }
    return mysql.query_db(query, data)

def check_id(userId):
    mysql = connectToMySQL("user_db")
    query = "SELECT * FROM users where id = %(userId)s"
    data = {
        'userId': userId
    }
    return mysql.query_db(query, data)[0]

def get_all_users():
    mysql = connectToMySQL("user_db")
    query = "SELECT id, first_name, last_name FROM users WHERE id NOT IN (%(userId)s)"
    data = {
        "userId": session['user_loggedIn']
    }
    return mysql.query_db(query, data)

def get_all_messages():
    mysql = connectToMySQL("user_db")
    query = "SELECT messages.id, contents, first_name, last_name, messages.created_at FROM messages JOIN users ON users.id = messages.user_id WHERE recipient_id = %(userId)s"
    data = {
        "userId": session['user_loggedIn']
    }
    return mysql.query_db(query, data)

@app.route('/')
def index():
    if "email" not in session:
        session['email'] = ""

    mysql = connectToMySQL("user_db")
    return render_template("login.html", email = session['email'])

@app.route('/register')
def show_register():
    if "fname" not in session:
        session['email'] = ""
    if "lname" not in session:
        session['email'] = ""
    if "email" not in session:
        session['email'] = ""
    return render_template("register.html")

@app.route('/check_username', methods=['POST'])
def check_username():
    found = False
    mysql = connectToMySQL("user_db")
    query = "SELECT first_name from users WHERE username = %(username)s"
    data = {
        "username": request.form['username']
    }
    result = mysql.query_db(query, data)
    if result:
        found = True
    return render_template("partials/username.html", found=found)

@app.route('/wall')
def success():
    if "user_loggedIn" not in session:
        return redirect('/')
    user = check_id(session['user_loggedIn'])
    all_users = get_all_users()
    user_messages = get_all_messages()
    print(all_users)
    print(len(user_messages))

    return render_template('wall.html', fname=user['first_name'], all_users=all_users, user_messages=user_messages, count_messages=len(user_messages))

@app.route('/send_message', methods=['POST'])
def send_message():
    mysql = connectToMySQL("user_db")
    query = "INSERT INTO messages(contents, user_id, recipient_id) VALUES(%(contents)s, %(userId)s, %(recipient_id)s)"
    data = {
        "contents": request.form['contents'],
        "userId": session['user_loggedIn'],
        "recipient_id": request.form['recipient_id']
    }
    mysql.query_db(query, data)
    flash("Message sent!")
    return redirect('/wall')

@app.route("/message_delete/<messageId>")
def delete_message(messageId):
    mysql = connectToMySQL("user_db")
    query = "DELETE FROM messages WHERE id = %(messageId)s"
    data = {
        "messageId": messageId
    }
    mysql.query_db(query, data)
    return redirect("/wall")

@app.route('/create_user', methods=['POST'])
def register():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
    if request.form['password'] != request.form['cpassword']:
        flash("Passwords does not match!")

    if check_email():
        flash("Email already exist!")
        return redirect("/register")

    if not "_flashes" in session.keys():
        pw_hash = bcrypt.generate_password_hash(request.form['password'])

        mysql = connectToMySQL("user_db")
        query = "INSERT INTO users(first_name, last_name, username, email, password) VALUES(%(fname)s, %(lname)s, %(username)s, %(email)s, %(password)s)"
        data = {
            "fname": request.form['fname'],
            "lname": request.form['lname'],
            "username": request.form['username'],
            "email": request.form['email'],
            "password": pw_hash
        }
        mysql.query_db(query, data)
        flash("User created!", "success")
        return redirect("/")
    else:
        return redirect("/register")

@app.route('/login', methods=['POST'])
def login():
    user = check_email()
    if(user):
        if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
            session['user_loggedIn'] = user[0]['id']
            return redirect('/wall')
    
    session['email'] = request.form['email']
    flash("Invalid email or password", "result")
    return redirect("/")

@app.route('/logout')
def logout():
    session.pop("user_loggedIn")
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)