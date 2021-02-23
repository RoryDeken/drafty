# Drafty

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.4.1-red.svg?longCache=true&style=flat-square&logo=flask&logoColor=white&colorA=4c566a&colorB=5e81ac)


Welcome to Drafty, a Vue/Python/Mysql application for "Offline" drafting of players for your fantasy leagues.
 

# Getting Started

Get set up locally in two steps:
```git clone https://github.com/RoryDeken/drafty.git```
```cd drafty```

This project uses [pipenv](https://pypi.org/project/pipenv/) to manage both dependencies and environments.

Install pipenv and install the dependencies using 
```pipenv install ```

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application; should be `wsgi.py`.
* `FLASK_ENV`: The environment in which to run your application; either `development` or `production`.
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: SQLAlchemy connection URI to a SQL database. (This codebase was built using the pmysql extension but you can use others)

*Remember never to commit secrets saved in .env files to Github.*

### Run the db migration
Make sure your database is up and running if necessary before you run the migration.
```pipenv run python drafty/player_import.py ```
*Note: This is currently working with python3 but you may encounter bugs as it was originally written as a one off and later tied into flask_sqalchemy*

### Run the application
```pipenv run flask run ```
You should be able to see the application running on localhost:5000 and should see a hello message.
The current supported route is /dashboard to see the available players and to be able to draft them.


#### There are probably lots of bugs I will need to work through at this point but feel free to contribute 






