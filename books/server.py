from flask import Flask, render_template, request, session, redirect, url_for, Markup
from sqlalchemy import exc
from model import db,User,Review,Book
from utils import get_image_url, get_book_info, get_rating_info, get_book_basic_backup,generate_star_rating

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
                return redirect(url_for("index"))
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

@app.route("/book/<string:isbn>/<string:review>", methods=['GET'])
def book(isbn,review):
    review = eval(review)
    book_url = get_image_url(str(isbn))
    summ, descr = get_book_info(str(isbn))
    descr = Markup(descr)
    try:
        book_db = Book.query.get(isbn)
        title = book_db.title
        author = book_db.author
        year = book_db.year
    except:
        title,author,year = get_book_basic_backup(isbn)
    book_info = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn,
        "img_url": book_url,
        "summary": summ,
        "description": descr,
    }

    if review:
        av, dist = get_rating_info(isbn)
        dist_perc = [round(100*d/dist[-1]) for d in dist[:-1]]
        star_html = Markup(generate_star_rating(av))

        rating_info = {
        "average": av,
        "stars_html": star_html,
        "dist_num": dist[:-1],
        "dist_perc": dist_perc,
        "reviews": ['hello'],
        }

    if review:
        print(dist_perc)
        return render_template("review.html",book=book_info, rating=rating_info)
    else:
        return render_template("book.html",book=book_info)

@app.route("/log_out", methods=['GET'])
def log_out():
    try:
        u = session['user']
        u[1] = False
        session.pop('user',None)
        session['user'] = u
    except KeyError:
        pass
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True,port=8000)
