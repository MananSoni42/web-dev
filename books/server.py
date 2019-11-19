from flask import Flask, render_template, request, session, redirect, url_for, Markup
from sqlalchemy import exc,func
from model import db,User,Review,Book
from utils import get_image_url, get_book_info, get_rating_info, get_book_basic_backup,generate_star_rating,search_from

app = Flask(__name__)
app.secret_key = "RandOM PasSwoRd"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:password@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

MAX_BOOKS_READ = 100
MAX_BOOK_HOME = 50
MAX_BOOK_SEARCH = 10

@app.route("/", methods=['GET'])
def index():
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
    if not session["user"][1]:
        return render_template("error.html", message='Not logged in', callback='index')

    books = []
    book_list = Book.query.all()
    count = 0
    for book in book_list:
        count += 1
        if count > MAX_BOOK_HOME:
            break
        if not book.img_url:
            db.session.query(Book).filter(Book.isbn == book.isbn).update({'img_url': get_image_url(book.isbn)})
            db.session.commit()
        book_info = {
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "img": book.img_url
        }
        books.append(book_info)
    return render_template("home.html",books=books)

@app.route("/my_books", methods=['GET'])
def my_books():
    if not session["user"][1]:
        return render_template("error.html", message='Not logged in', callback='index')
    user = User.query.get(session["user"][0])
    books = []
    book_list = Book.query.filter(Book.isbn.in_(user.books))
    count = 0
    for book in book_list:
        count += 1
        if count > MAX_BOOK_HOME:
            break
        if not book.img_url:
            db.session.query(Book).filter(Book.isbn == book.isbn).update({'img_url': get_image_url(book.isbn)})
            db.session.commit()
        book_info = {
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "img": book.img_url
        }
        books.append(book_info)
    return render_template("my_books.html",books=books)

@app.route("/profile", methods=['GET'])
def profile():
    if not session["user"][1]:
        return render_template("error.html", message='Not logged in', callback='index')

    uname = session['user'][0]
    user = User.query.get(uname)
    user_info = {
    "fname": user.fname,
    "lname": user.lname,
    "uname": user.uname,
    "books_num": len(user.books),
    "books_perc": 100*len(user.books)/MAX_BOOKS_READ
    }
    return render_template("profile.html",user=user_info)

@app.route("/book/<string:isbn>", methods=['GET'])
def book(isbn):
    try:
        review = request.args.get('review')
        book_db = Book.query.get(isbn)

        if review:
            review = eval(review)
        else:
            review = False

        if book_db.img_url:
            book_url = book_db.img_url
        else:
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
            return render_template("review.html",book=book_info, rating=rating_info)
        else:
            return render_template("book.html",book=book_info)
    except:
        return render_template("error.html", message='Not logged in', callback='home')

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

@app.route("/add_book", methods=['GET'])
def add_book():
    if not session["user"][1]:
        return render_template("error.html", message='Not logged in', callback='index')
    try:
        isbn = request.args.get("isbn")
        user = User.query.get(session["user"][0])
        user.add_book_user(isbn)
        db.session.commit()
        return redirect(url_for('book',isbn=isbn))
    except:
        return render_template("error.html", message='Failed to add book', callback='home')

@app.route("/search", methods=['GET'])
def search():
    title = request.args.get('title')
    books = Book.query.all()
    title_list = [book.title.lower() for book in books]
    close_titles = search_from(title_list,title,max_results=MAX_BOOK_SEARCH)
    books = []
    book_list = Book.query.filter(func.lower(Book.title).in_(close_titles))
    count = 0
    for book in book_list:
        count += 1
        if count > MAX_BOOK_HOME:
            break
        if not book.img_url:
            db.session.query(Book).filter(Book.isbn == book.isbn).update({'img_url': get_image_url(book.isbn)})
            db.session.commit()
        book_info = {
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "img": book.img_url
        }
        books.append(book_info)
    return render_template("home.html",books=books)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
