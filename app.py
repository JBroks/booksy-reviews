import os
# Import Flask functionality in order to set up the application for use
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)

# Configure MONGO_DBNAME and MONGO_URI and pass it via os environment
app.config['MONGO_DBNAME'] = 'booksyDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Configure SECRET_KEY and pass it via os environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Set up the connection to the booksyDB database

mongo = PyMongo(app)
loginM = LoginManager(app)
loginM.login_view = 'login'

# User class
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
            return redirect(url_for('login'))
        else:
            flash('Username or email that you provided already exists', 'danger')
            
    return render_template('register.html', title='Sign Up', form=form)

@loginM.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None
    return User(u['username'])
    
# Function that logs user in and checked if password is correct
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
    return render_template('login.html', title='Sign In', form=form)

# Function that enables user logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Function that records time and date when a particular user (current user) was seen last
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        username = current_user.get_id()
        mongo.db.users.find_one_and_update({'username': username}, {'$set': {'last_seen': current_user.last_seen}})

# Function that displays user name in his/her profile and displays all reviews added by the user
@app.route('/user/<username>')
@login_required
def profile(username):
    user = mongo.db.users.find_one({'username': username})
    user_review = mongo.db.reviews.find({'added_by': username }).sort([("_id", -1)])
    return render_template('profile.html', user=user, reviews=user_review, title='Profile')

# Function that deletes the user account
@app.route('/delete_account/<user_id>')
@login_required
def delete_account(user_id):
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    flash('We are sorry to see you go, please note that your account has been pernamently deleted.')
    return redirect(url_for('index'))

# Function that renders add review template. Form request imput from the user. Function activated when user clicks "add review" in the navbar 
@app.route('/add_review/<username>')
@login_required
def add_review(username):
    user = mongo.db.users.find_one({'username': username})
    return render_template('addreview.html', user=user, title='Add Review')

# Function that sends user input (review record) to the reviews database - activated when user clicks "add review" button  
@app.route('/insert_review', methods=['POST'])
@login_required
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one({
        'title': request.form['title'],
        'author': request.form['title'],
        'publication_year': request.form['title'],
        'type': request.form['title'],
        'genre': request.form['title'],
        'cover': request.form['title'],
        'summary': request.form['title'],
        'review': request.form['title'],
        'added_by': request.form['title'],
        'upvote': []
    })
    
    return redirect(url_for('show_collection'))
    
# Reviews collection pagination

itemtotal = mongo.db.reviews.find().count()

def get_reviews(offset=0, per_page=3):
    collection = mongo.db.reviews.find().sort([("_id", -1)])
    return collection[offset: offset + per_page]

@app.route('/show_collection')
@login_required
def show_collection():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = itemtotal
    paginated_reviews = get_reviews(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('collection.html',
                            reviews=paginated_reviews,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)

# Function that renders view review template of a selected by user review
@app.route('/view/<review_id>')
@login_required
def view_review(review_id):
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('viewreview.html', review=the_review)

# Function that deletes review
@app.route('/delete_review/<review_id>')
@login_required
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    flash('Your review has now been pernamently deleted from our collection.')
    return redirect(url_for('show_collection'))
 
# Function that renders edit review template i.e. displays edit review form to the user 
@app.route('/edit_review/<review_id>')
@login_required
def edit_review(review_id):
    the_review =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)

# Function that submits user input to the database
@app.route('/update_review/<review_id>', methods=["POST"])
@login_required
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId(review_id)},
    {
        'title':request.form.get('title'),
        'author':request.form.get('author'),
        'publication_year': request.form.get('publication_year'),
        'type': request.form.get('type'),
        'genre': request.form.get('genre'),
        'cover': request.form.get('cover'),
        'summary': request.form.get('summary'),
        'review': request.form.get('review'),
        'added_by': request.form.get('added_by')
    })
    return redirect(url_for('show_collection'))
    
# Functions that allows upvoting and adds increment of 1 to the review table

@app.route('/upvote/<review_id>', methods=['GET', 'POST'])
def upvote(review_id):

    username = current_user.username
    
    match_count = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'upvote': {'$elemMatch': { "username": username}},
    })


    if match_count > 0:
        print("not equal to 0")
        mongo.db.reviews.update({ "_id": ObjectId(review_id) },
                                        { '$pull':
                                            { 'upvote':
                                            {'username': username}  } } )

    else:
        print("equal to 0")
        mongo.db.reviews.update({ "_id": ObjectId(review_id) },
                                        { '$push':
                                            { 'upvote':
                                            {'username': username}  } } )

    return redirect(url_for('view_review', review_id=review_id))
      
# Functions that allows downvoting and adds increment of 1 to the review table

@app.route('/downvote/<review_id>', methods=['GET', 'POST'])
def downvote(review_id):
    mongo.db.reviews.find_one_and_update({'_id': ObjectId(review_id)},
                                            {'$inc': {'downvote': 1}})
    return redirect(url_for('view_review', review_id=review_id))

# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)