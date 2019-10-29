import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request

engine = create_engine('postgresql://manan:password@localhost/manan')
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

flights = db.execute("SELECT * FROM flights;").fetchall()
fl_names = [(i+1,f'{f[0]} - {f[1]} to {f[2]} lasting {f[3]} minutes') for i,f in enumerate(flights)]
names = [f'{f[0]} - {f[1]} to {f[2]} lasting {f[3]} minutes' for f in flights]

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/book", methods=['GET'])
def book():
    return render_template("book.html",flights=names)

@app.route("/success", methods=['POST'])
def success():
    name = request.form.get("name")
    fl_id = int(request.form.get("fl_id"))
    db.execute("INSERT INTO passengers (name,flight_id) VALUES (:name,:fl_id);",
                {"name": name, "fl_id": fl_id+1})
    db.commit()
    return render_template("success.html")

@app.route("/flights", methods=['GET'])
def list_flights():
    return render_template("list.html",flights=fl_names)

@app.route("/flights/<int:fl_id>")
def get_flight_by_id(fl_id):
    ps = db.execute("SELECT name from passengers WHERE flight_id=:id;", {"id": fl_id}).fetchall()
    plist = [p[0] for p in ps]
    f = db.execute("SELECT * FROM flights WHERE id=:id;",{"id": fl_id}).fetchall()[0]
    return render_template("info.html", flight=f,passengers=plist)

if __name__ == "__main__":
    app.run(debug=True)
