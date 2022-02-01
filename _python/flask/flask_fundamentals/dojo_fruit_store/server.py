from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'admin'
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    session['data'] = request.form
    return redirect("/show")

@app.route("/show")
def show_checkout():
    print(session['data'])
    total_order = int(session['data']['strawberry']) + int(session['data']['raspberry']) + int(session['data']['apple'])
    return render_template("checkout.html", total=total_order, strawberry=session['data']['strawberry'], raspberry=session['data']['raspberry'], apple=session['data']['apple'], name=session['data']['name'], id=session['data']['id'])
    
if __name__ == "__main__":
    app.run(debug=True)