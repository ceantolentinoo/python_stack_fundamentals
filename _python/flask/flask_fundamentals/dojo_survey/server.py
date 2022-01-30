from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['POST'])
def create_user():
    print(request.form)
    data=request.form
    return render_template("show.html", name=data['name'], campus=data['location'], language=data['language'], comment=data['comment'])


if __name__ == "__main__":
    app.run(debug=True)