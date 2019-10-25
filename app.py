import os
#import Flask functionality in order to set up the application for use
from flask import Flask

#Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)

#Create a function with a route in it
@app.route('/')
def hello():
    return 'Hello World'

#Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)