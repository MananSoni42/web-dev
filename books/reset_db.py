from flask import Flask
from model import Book,User,Review,db
from tqdm import tqdm
import csv

app = Flask(__name__)
app.secret_key = "RandOM PasSwoRd"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:psql@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()
    Book.query.delete()
    User.query.delete()
    Review.query.delete()
    db.session.commit()

    path = 'project1/books.csv'
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in tqdm(reader):
            db.session.add(
                Book(
                isbn=row[0],
                title=row[1],
                author=row[2],
                year=int(row[3]),
                )
            )
            db.session.commit()
