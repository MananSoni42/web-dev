# Web Developement
Learning full stack development through [CS50's Web Programming]([https://www.youtube.com/playlist?list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5](https://www.youtube.com/playlist?list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5)) with Python and JavaScript.

## Frontend
Contains basic static pages created using only HTML and CSS. The pages can be opened directly in your browser (or you can click the links below).
The pages are:
* [nav](https://manansoni42.github.io/web-dev/frontend/nav.html) - A basic navigation bar with clickable buttons
* [box](https://manansoni42.github.io/web-dev/frontend/box.html) - Learning to use the CSS grid module
* [members](https://manansoni42.github.io/web-dev/frontend/members.html) - A generic members page for any organization
## Notes
A dynamic website created using Flask, HTML and CSS (along with Bootstrap) where you can jot down post-it style notes.
To run the webiste, navigate to the /notes directory and run:
```
python3 server.py
```
Then, navigate to the website, try going to your name by typing the following in the URL bar:
```
localhost:5000/your_name_here
```
## Flights
A sample flights website, where you can book flights and see details about all the flights. Built using HTML, CSS, Flask and Postgre SQL
### Setting up the server:
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
### Structure of the website:
* /: Book flights or see all current flights
* /book: Book a flight
* /flights: List all current flights
* /flights/\<flight_id\>: Get information about a particular website
## License
This project is licensed under the [MIT](https://opensource.org/licenses/MIT) License
