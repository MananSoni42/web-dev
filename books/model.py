from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.types.password import PasswordType

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String, nullable=False, default='')

    def __str__(self):
        return f'{self.isbn} - {self.title} by {self.author} on {self.year}'

class User(db.Model):
    __tablename__ = "users"
    uname = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False, unique=True)
    _books = db.Column(db.String, nullable=False, default='')
    password = db.Column(PasswordType(
            schemes=[
                'pbkdf2_sha512',
                'md5_crypt'
            ],
            deprecated=['md5_crypt']
        ),
        nullable=False)

    def verify_pass(self,password):
        return self.password == password

    @property
    def books(self):
        return [x.strip() for x in self._books.split(';') if x.strip()]

    def add_book_user(self,book_id):
        print(book_id,self.books)
        if book_id not in self.books:
            self._books += f'{book_id};'

    def __str__(self):
        return f'{self.uname} - {self.fname} {self.lname}: {self.mail}'

class Review(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    bid = db.Column(db.String, db.ForeignKey("books.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    def __str__(self):
        return f'{self.id} by {self.uid} for {self.bid}: {self.rating}\n title: {self.title}\n {self.body}'
