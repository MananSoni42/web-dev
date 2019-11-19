from flask import Flask
from model import Book
import csv

app = Flask(__name__)
app.secret_key = "RandOM PasSwoRd"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:password@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

path = 'project1/books.csv'
with open(path) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        db.session.add(
            Book(
            isbn=row[0],
            tite=row[1],
            author=row[2],
            year=int(row[3]),
            )
        )
        db.session.commit()
