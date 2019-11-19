# Web Developement
Learning full stack development through [CS50's Web Programming]([https://www.youtube.com/playlist?list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5](https://www.youtube.com/playlist?list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5)) with Python and JavaScript.

## Frontend
Contains basic static pages created using only HTML, CSS and JavaScript. The pages can be opened directly in your browser (or you can click the links below).
The pages are:
* [nav](https://manansoni42.github.io/web-dev/frontend/nav.html) - A basic navigation bar with clickable buttons (HTML & CSS)
* [box](https://manansoni42.github.io/web-dev/frontend/box.html) - Learning to use the CSS grid module (HTML & CSS )
* [members](https://manansoni42.github.io/web-dev/frontend/members.html) - A generic members page for any organization (HTML & CSS)
* [members-dynamic](https://manansoni42.github.io/web-dev/frontend/members-dynamic.html) - Template for a generic members page for any organization with the ability to add/delete members (HTML, CSS & JavaScript(Handlebars))
* [Scroller](https://manansoni42.github.io/web-dev/frontend/inf_scroll.html) - An infinite list of posts that generates new posts as soon as you reach the bottom of the page (HTML, CSS(animation), JavaScript)
* [Clock](https://manansoni42.github.io/web-dev/frontend/clock.html) - An analog clock that shows your system time (HTML(SVG), CSS, JavaScript)
* [Paint](https://manansoni42.github.io/web-dev/frontend/paint.html) - A paint like application where you can draw on the screen with your mouse (HTML(SVG), CSS, JavaScript(Handlebars, D3))
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

## Project 1 - Books
This project was done as a part of the CS50 course. The original instructions can be found [here](https://docs.cs50.net/ocw/web/projects/1/project1.html). View the full project at  [books](https://github.com/MananSoni42/web-dev/tree/master/books).

## License
This project is licensed under the [MIT](https://opensource.org/licenses/MIT) License
