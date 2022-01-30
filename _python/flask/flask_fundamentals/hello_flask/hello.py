from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html")	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)

