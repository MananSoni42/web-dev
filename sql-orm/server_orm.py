import os
from flask import Flask, render_template, request
from model import db,Flight,Passenger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:password@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/book", methods=['GET'])
def book():
    flights = Flight.query.all()
    names = [f'{f.id} - {f.origin} to {f.destination} lasting {f.duration} minutes' for f in flights]
    return render_template("book.html",flights=names)

@app.route("/success", methods=['POST'])
def success():
    name = request.form.get("name")
    fl_id = int(request.form.get("fl_id"))
    flight = Flight.query.get(fl_id+1)
    flight.add_passenger(name)
    return render_template("success.html")

@app.route("/flights", methods=['GET'])
def list_flights():
    flights = Flight.query.all()
    fl_names = [(f.id,f'{f.id} - {f.origin} to {f.destination} lasting {f.duration} minutes') for f in flights]
    return render_template("list.html",flights=fl_names)

@app.route("/flights/<int:fl_id>")
def get_flight_by_id(fl_id):
    flight = Flight.query.get(fl_id)
    print(fl_id)
    passengers = flight.passengers
    return render_template("info_orm.html", flight=flight,passengers=passengers)

if __name__ == "__main__":
    app.run(debug=True)
