from flask import Flask, render_template, request, session, redirect, url_for
from model import db,User,Review
from sqlalchemy import exc

app = Flask(__name__)
app.secret_key = "RandOM PasSwoRd"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:password@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def index():
    print(session)
    try:
        uname, logged_in = session['user']
        if logged_in:
            return redirect(url_for("home"))
        else:
            return render_template("index.html")
    except KeyError:
        return render_template("index.html")

@app.route("/signup", methods=['GET','POST'])
def sign_up():
    print(request.method)
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        uname = request.form.get("uname")
        mail = request.form.get("email")
        password = request.form.get("pass")
        re_password = request.form.get("repass")

        if password == re_password:
            try:
                db.session.add(
                    User(
                    fname=fname,
                    lname=lname,
                    uname=uname,
                    mail=mail,
                    password=password))
                db.session.commit()
                session['user'] = [uname,True]
                return render_template(url_for("index.html"))
            except exc.IntegrityError:
                return render_template("error.html", message='Username or e-mail already exists', callback='sign_up')
        else:
            return render_template("error.html", message='Passwords don\'t match', callback='sign_up')
    if request.method == 'GET':
        return render_template("sign_up.html")

@app.route("/login", methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        uname = request.form.get("uname")
        password = request.form.get("pass")
        user = User.query.get(uname)
        if user:
            if user.verify_pass(password):
                u = session['user']
                u[0] = uname
                u[1] = True
                session.pop('user',None)
                session['user'] = u
                return redirect(url_for("index"))
            else:
                return render_template("error.html", message='Incorrect Username or Password', callback='log_in')
        else:
            return render_template("error.html", message='Incorrect Username or Password', callback='log_in')
    else:
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

@app.route("/log_out", methods=['GET'])
def log_out():

    u = session['user']
    u[1] = False
    session.pop('user',None)
    session['user'] = u
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True,port=8000)
