from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    
    return redirect("/show")

@app.route("/show")
def show_checkout():
    print(request.form)
    total_order = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    return render_template("checkout.html", total=total_order, strawberry=request.form['strawberry'], raspberry=request.form['raspberry'], apple=request.form['apple'], name=request.form['name'], id=request.form['id'])
if __name__ == "__main__":
    app.run(debug=True)