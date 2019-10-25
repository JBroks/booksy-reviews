import os
# Import Flask functionality in order to set up the application for use
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)

# Configure MONGO_DBNAME and MONGO_URI and pass it via os environment
app.config['MONGO_DBNAME'] = 'booksDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Set up the connection to the booksyDB database

mongo = PyMongo(app)

# Create a function with a route in it
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)