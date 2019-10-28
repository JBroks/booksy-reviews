import os
# Import Flask functionality in order to set up the application for use
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash

# Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)

# Configure MONGO_DBNAME and MONGO_URI and pass it via os environment
app.config['MONGO_DBNAME'] = 'booksDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Configure SECRET_KEY and pass it via os environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Set up the connection to the booksyDB database

mongo = PyMongo(app)
loginM = LoginManager(app)
loginM.login_view = 'login'

class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)


# Function with a route in it that will direct you to the landing site / home page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# Function that enables user to register and create an account
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are currently logged in!', 'success')
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one({"username": form.username.data}, {"email": form.email.data})
        if existing_user is None:
            password = generate_password_hash(request.form['password'])
            mongo.db.users.insert_one({'username': request.form['username'],'email': request.form['email'],
                             'password': password})
            flash(f'Congratulations {form.username.data}, you are now a registered user!')
        else:
            flash('Username or email that you provided already exists', 'danger')
            
    return render_template('register.html', title='Sign Up', form=form)

@loginM.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None
    return User(u['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one({"username": form.username.data})
        if user and User.check_password(user['password'], form.password.data):
            user_obj = User(user['username'])
            login_user(user_obj)
            flash(f'Hello {form.username.data}, you have successfully logged into your account', 'success')
            return redirect(request.args.get("next") or url_for("index"))
        flash("Wrong username or password", 'error')
    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)