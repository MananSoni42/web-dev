# Flights
A sample flights website, where you can book flights and see details about all the flights. Built using HTML, CSS, Flask and Postgre SQL.
## Setting up the server:
* Set up a local Postgre SQL server, follow the instructions from [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04).
* Install sqlalchemy, flask_sqlalchemy and psycopg2
	```
	pip3 install sqlalchemy flask_sqlalchemy
	apt-get install python-psycopg2 libpq-dev
	pip3 install psycopg2
	```
* Configure your Database URIs and change these in your server.
	```
	server_sql:
	engine = create_engine('postgresql://<role>:<password>@localhost/<database>')

	server_orm:
	app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://<role>:<password>@localhost/<database>'
	```
* You are good to go!

## Structure of the website:
* /: Book flights or see all current flights
* /book: Book a flight
* /flights: List all current flights
* /flights/\<flight_id\>: Get information about a particular flight
