from db import connectToMySQL
from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secret"
# our index route will handle rendering our form
@app.route('/')
def index():
    mysql = connectToMySQL("user_db")
    return render_template("login.html")

@app.route('/register')
def show_register():
    return render_template("register.html")

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/create_user', methods=['POST'])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    mysql = connectToMySQL("user_db")
    query = "INSERT INTO users(first_name, last_name, email, password) VALUES(%(fname)s, %(lname)s, %(email)s, %(password)s)"
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password": pw_hash
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("user_db")
    query = "SELECT * FROM users where email = %(email)s"
    data = {
        'email': request.form['email']
    }
    user = mysql.query_db(query, data)
    print(user)
    if(user):
        if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
            return redirect('/success')
    
    flash("Invalid email or password")
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)