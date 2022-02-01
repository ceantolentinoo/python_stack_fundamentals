from email import message
from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'admin'

@app.route("/")
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    else:
        session['activities'].reverse()
    return render_template("index.html", gold=session['gold'], activities=session['activities'])

@app.route("/process_money", methods=['POST'])
def process_money():
    data = request.form
    gold_earned = random.randrange(int(data['start']), int(data['end']))
    if(gold_earned<0):
        session['activities'].append(f"<span class='text-danger d-block'>Lost {gold_earned} golds from the casino! {datetime.now()}</span>")
    else:
        session['activities'].append(f"<span class='text-success d-block'>Earned {gold_earned} golds from the {data['building']}! {datetime.now()}</span>")
    session['gold'] += gold_earned 
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)