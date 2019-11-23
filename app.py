import os
import json
import logging
# Import Flask functionality in order to set up the application for use
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_paginate import Pagination, get_page_args, get_page_parameter
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
    author = request.form['author'].title()
    title = request.form['title'].title()
    
    existing_review = mongo.db.reviews.count_documents({ '$and': 
        [{ 'author' : author },
        { 'title': title }] 
    })
        
    if existing_review == 0:
        
        reviews.insert_one({
            'title': request.form['title'].title(),
            'author': request.form['author'].title(),
            'publication_year': request.form['publication_year'],
            'type': request.form['type'],
            'genre': request.form['genre'].title(),
            'cover': request.form['cover'],
            'summary': request.form['summary'],
            'review': request.form['review'],
            'added_by': request.form['added_by'],
            'upvote': [],
            'downvote': [],
            'upvote_total': 0,
            'downvote_total': 0
        
        })
        
    else: 
        flash('Book with the same title and author already exists in our collection')
    
    return redirect(url_for('show_collection'))
    
# Reviews collection

def get_reviews(offset=0, per_page=10):
    reviews = mongo.db.reviews.find().sort([("_id", -1)])

    reviews_list = list(reviews)
    
    return reviews_list[ offset: offset + per_page ]

@app.route('/show_collection')
@login_required
def show_collection():
    
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    total = mongo.db.reviews.count_documents({})
    
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
    review_comments = mongo.db.comments.find({ "review_id": ObjectId(review_id) }).sort([("_id", -1)])
    return render_template('viewreview.html', review=the_review, comments=review_comments)

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
    { '$set':
        {
        'title':request.form.get('title').title(),
        'author':request.form.get('author').title(),
        'publication_year': request.form.get('publication_year'),
        'type': request.form.get('type'),
        'genre': request.form.get('genre').title(),
        'cover': request.form.get('cover'),
        'summary': request.form.get('summary'),
        'review': request.form.get('review'),
        'added_by': request.form.get('added_by')
        }
    })
    return redirect(url_for('show_collection')) 

# Function that sends user input (comment) to the comments collection - activated when user clicks "post" button  
@app.route('/insert_comment/<review_id>', methods=['POST', 'GET'])
@login_required
def insert_comment(review_id):
    username = current_user.username
    comments = mongo.db.comments
    comments.insert_one({
        'comment': request.form['comment'],
        'username': username,
        'review_id': ObjectId(review_id)
    })
    return redirect(url_for('view_review', _anchor='comments-section', review_id=review_id))

# Function that submits user input to the database
@app.route('/update_comment/<review_id>/<comment_id>', methods=["POST"])
@login_required
def update_comment(comment_id, review_id):
    username = current_user.username
    comments = mongo.db.comments
    comments.update({'_id': ObjectId(comment_id)},
        { '$set': 
            { 'comment': request.form['comment'] }
        })
    
    return redirect(url_for('view_review', comment_id=comment_id, review_id=review_id))

# Function that deletes comment
@app.route('/delete_comment/<review_id>/<comment_id>')
@login_required
def delete_comment(comment_id, review_id):
    mongo.db.comments.remove({'_id': ObjectId(comment_id)})
    
    return redirect(url_for('view_review', comment_id=comment_id, review_id=review_id))

''' Define general functions that will add or remove vote from username list and vote total 
and set variable for keys upvote/downvote and upvote_total/downvote_total
'''
 
def add_vote(vote_type, vote_type_total, review_id, username):
    mongo.db.reviews.update({ "_id": ObjectId(review_id) },
                                        { '$push':
                                            { vote_type:
                                            {'username': username}  } } )
                                            
    mongo.db.reviews.find_one_and_update({'_id': ObjectId(review_id)},
                                            {'$inc': {vote_type_total: 1}})
                                            
def remove_vote(vote_type, vote_type_total, review_id, username):
    mongo.db.reviews.update({ "_id": ObjectId(review_id) },
                                        { '$pull':
                                            { vote_type:
                                            {'username': username}  } } )
                                            
    mongo.db.reviews.find_one_and_update({'_id': ObjectId(review_id)},
                                            {'$inc': {vote_type_total: -1}})
                                            
# Functions that allows upvoting and adds increment of 1 to the review table

@app.route('/upvote/<review_id>', methods=['GET', 'POST'])
@login_required
def upvote(review_id):

    username = current_user.username
    
    match_count_upvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'upvote': {'$elemMatch': { "username": username}},
    })
    
    match_count_downvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'downvote': {'$elemMatch': { "username": username}},
    })


    if match_count_upvote > 0:
        remove_vote('upvote', 'upvote_total', review_id, username)
                                            
    elif match_count_downvote > 0:
        add_vote('upvote', 'upvote_total', review_id, username)
        remove_vote('downvote', 'downvote_total', review_id, username)
                                            
    else:
        add_vote('upvote', 'upvote_total', review_id, username)

    return redirect(url_for('view_review', review_id=review_id))
      
# Functions that allows downvoting and adds increment of 1 to the review table

@app.route('/downvote/<review_id>', methods=['GET', 'POST'])
@login_required
def downvote(review_id):
    
    username = current_user.username
    
    match_count_upvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'upvote': {'$elemMatch': { "username": username}},
    })
    
    match_count_downvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'downvote': {'$elemMatch': { "username": username}},
    })

    if match_count_downvote > 0:
        remove_vote('downvote', 'downvote_total', review_id, username)
                                            
    elif match_count_upvote > 0:
        add_vote('downvote', 'downvote_total', review_id, username)
        remove_vote('upvote', 'upvote_total', review_id, username)
        
    else:
        add_vote('downvote', 'downvote_total', review_id, username)
    
    return redirect(url_for('view_review', review_id=review_id))

# Search function
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    
    search_input = request.form.get("search_input")
    search_string = str(search_input)
    mongo.db.reviews.create_index([('$**', 'text')])
    
    search_results = mongo.db.reviews.find({ "$text": { "$search": search_string }})
    results_count = mongo.db.reviews.count_documents({ "$text": { "$search": search_string }})
    
    
    if request.method == 'POST':
        logging.error('Entering the POST if')
        if search_string == '':
            logging.error('Entering the empty string if')
            flash('You have not provided any search input!')
            return redirect('/search')
            
        elif results_count == 0:
            logging.error('Entering no results if')
            flash('No results found!')
            return redirect('/search')
            
        else:
            logging.error('Entering results exist if')
            search_results
            
    return render_template('searchresults.html', reviews=search_results)

# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)