from flask import Flask, render_template, request
from model import db,User,Review

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:password@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/signup", methods=['GET'])
def sign_up():
    return render_template("sign_up.html")

@app.route("/login", methods=['GET'])
def log_in():
    return render_template("log_in.html")

@app.route("/home", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/my_books", methods=['GET'])
def my_books():
    return render_template("my_books.html")

@app.route("/profile", methods=['GET'])
def profile():
    return render_template("profile.html")

@app.route("/book", methods=['GET'])
def book():
    return render_template("book.html")

@app.route("/review", methods=['GET'])
def review():
    return render_template("review.html")

@app.route("/error", methods=['GET'])
def error():
    return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)
