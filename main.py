from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/ozil")
def benzi_or_messi():
    return "<h1>By Boi Benzi!!!</h1>"


@app.route("/user/<name>")
def user(name):
    return render_template('user.html', user_name=name)


app.run(debug=True)
