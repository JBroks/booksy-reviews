import os
# Import Flask functionality in order to set up the application for use
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm

# Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)

# Configure MONGO_DBNAME and MONGO_URI and pass it via os environment
app.config['MONGO_DBNAME'] = 'booksDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Configure SECRET_KEY and pass it via os environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Set up the connection to the booksyDB database

mongo = PyMongo(app)

# Function with a route in it that will direct you to the landing site / home page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# Function that will renders sign in template

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)





# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)