import os
# Import Flask functionality in order to set up the application for use
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)

# Use the OS library to set a constant called MONGO_URI
# by using the getenv() method to read in the environment variable that we just set.
# Set another constant called MONGO_DBNAME and give that the name of our database

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = "booksyDB"

# Set up the connection to the booksyDB database

mongo = PyMongo

# Create a function with a route in it
@app.route('/')
def hello():
    return 'Hello World'

# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)