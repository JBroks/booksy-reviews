import os
import logging
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_paginate import Pagination, get_page_args, get_page_parameter
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from user import User
from datetime import datetime, date
from flask_toastr import Toastr

# Create an instance of Flask / Flask app and store it in the app variable
app = Flask(__name__)
toastr = Toastr(app)
        
# Configure MONGO_DBNAME and MONGO_URI and pass it via os environment
app.config['MONGO_DBNAME'] = 'booksyDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Configure SECRET_KEY and pass it via os environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Set up the connection to the booksyDB database
mongo = PyMongo(app)
loginM = LoginManager(app)
loginM.login_view = 'login'

# INDEX
''' 
Function with a route in it that will direct you to 
the landing site / home page
'''

@app.route('/')
@app.route('/index')
def index():
    
    return render_template("index.html")

# REGISTER USER
# Function that enables user to register and create an account

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        
        flash('You are currently logged in!', 'info')
        
        return redirect(url_for('index'))
        
    form = RegistrationForm()
    
    if form.validate_on_submit():
        
        existing_user = mongo.db.users.find_one({"username": form.username.data}, {"email": form.email.data})
        
        if existing_user is None:
            
            password = generate_password_hash(request.form['password'])
            mongo.db.users.insert_one({'username': request.form['username'].lower(),'email': request.form['email'],
                             'password': password})
            flash(f'Congratulations {form.username.data.lower()}, you are now a registered user!', 'success')
            
            return redirect(url_for('login'))
            
        else:
            
            flash('Username or email that you provided already exists', 'warning')
            
    return render_template('register.html', title='Sign Up', form=form)

# USER LOADER
''' 
This callback is used to reload the user object from the username
stored in the session
'''

@loginM.user_loader
def load_user(username):
    
    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None
        
    return User(u['username'])

# LOGIN USER
# Function that logs user in and checked if password is correct

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one({"username": form.username.data.lower()})
        
        if user and User.check_password(user['password'], form.password.data):
            
            user_obj = User(user['username'])
            login_user(user_obj)
            flash(f'Hello {form.username.data.lower()}, you have successfully logged into your account', 'success')
            
            return redirect(request.args.get("next") or url_for("index"))
            
        flash("Wrong username or password", 'error')
        
    return render_template('login.html', title='Sign In', form=form)

# LOGOUT USER
# Function that enables user logout

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# USER LAST SEEN
'''
Function that records time and date when a particular user 
(current user) was seen last
'''

@app.before_request
def before_request():
    
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow().strftime("%A, %d. %B %Y %I:%M%p")
        username = current_user.get_id()
        mongo.db.users.find_one_and_update({'username': username}, {'$set': {'last_seen': current_user.last_seen}})

# USER PROFILE
'''
Function that displays user name in his/her profile and displays all reviews
added, liked / disliked and commented on by the user
'''

@app.route('/user/<username>')
@login_required
def profile(username):
    
    user = mongo.db.users.find_one({'username': username})
    
    # Find all reviews added by the user
    user_review = mongo.db.reviews.find({'added_by': username }).sort([("_id", -1)])
    
    # Find all reviews liked by the user
    user_upvotes = mongo.db.reviews.find({ 'upvote': {'username': username} }).sort([("_id", -1)])
    
    # Find all reviews disliked by the user
    user_downvotes = mongo.db.reviews.find({ 'downvote': {'username': username} }).sort([("_id", -1)])
    
    # Find all reviews commented on by the user
    user_comments = mongo.db.reviews.aggregate([
        { '$lookup': { 'from': 'comments',
                       'localField': '_id',
                       'foreignField': 'review_id',
                       'as': 'commentsData'} },
        { '$unwind': { 'path': "$commentsData"} },
        { '$match': { 'commentsData.username': username } },
    ]);
    
    return render_template('profile.html', user=user, reviews=user_review, 
                            upvotes=user_upvotes, downvotes=user_downvotes, 
                            comments=user_comments, title='Profile')

# DELETE ACCOUNT
'''
Function that deletes the user account.
When user deletes the account pernamentaly, all votes, reviews and comments
added by him or her are being deleted as well
'''

@app.route('/delete_account/<user_id>')
@login_required
def delete_account(user_id):
    
    username = current_user.username
    
    # Recalculate total upvotes and downvotes
    # Remove votes for a given user from all reviews they voted for
    # Deduct user voted from total count
    
    mongo.db.reviews.update_many(
    { 'upvote': {'username': username} },
    {'$inc': { 'upvote_total' : -1} } )
    
    mongo.db.reviews.update_many(
    { 'downvote': {'username': username}  },
    {'$inc': { 'downvote_total' : -1} } )
    
    # Remove username from all reviews that user voted for
    # Remove votes for a given user from all reviews they voted for
    # Remove username from upvote /downvote array
    
    mongo.db.reviews.update_many(
    { 'upvote': {'username': username} },
    { '$pull': { 'upvote': {'username': username}  } } )
    
    mongo.db.reviews.update_many(
    { 'downvote': {'username': username}  },
    { '$pull': { 'downvote': {'username': username}  } } )
   
    # Remove all reviews and comments added by the user
    mongo.db.reviews.remove({'added_by': username })
    mongo.db.comments.remove({'username': username })
    
    # Remove user
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    
    return redirect(url_for('index'))

# AMAZON LINK
'''
Generate amazon link that will redirect user to search on amazon website.
Search takes into account book title and author.
'''

def generate_amazon_link(title, author):
    
	base_link = 'https://www.amazon.co.uk/s?k='
	
	amazon_concat = base_link + title.replace(' ', '+') + "+" + author.replace(' ', '+')
	
	amazon_link = amazon_concat.replace('&', 'and')
	
	return amazon_link

# ADD REVIEW
'''
Function that renders add review template. Form requires input from a user. 
Function is activated when user clicks "add review" in the navbar
'''

@app.route('/add_review/<username>')
@login_required
def add_review(username):
    
    user = mongo.db.users.find_one({'username': username})
    
    return render_template('addreview.html', user=user, title='Add Review')

# INSERT REVIEW
'''
Function that submits user input (review record) to the reviews collection.
It is activated when user clicks "add review" (submit) button
'''

@app.route('/insert_review', methods=['POST'])
@login_required
def insert_review():
    
    reviews = mongo.db.reviews
    username = current_user.username
    
    # Retrive author and title from the form in order to generate amazon link
    author = request.form['author'].title()
    title = request.form['title'].title()
    
    # Generate amazon link
    amazon_link = generate_amazon_link(title, author)
    
    # Check if review with a given author and title already exists
    existing_review = mongo.db.reviews.count_documents({ '$and': 
        [{ 'author' : author },
        { 'title': title }] 
    })
    
    # If review does not exist in the collection insert it    
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
            'amazon': amazon_link,
            'added_by': username,
            'upvote': [],
            'downvote': [],
            'upvote_total': 0,
            'downvote_total': 0
        
        })
        
    # If review with the same title and author already exists throw an error message
    else: 
        
        flash('Book with the same title and author already exists in our collection', 'error')
    
    return redirect(url_for('show_collection'))

# REVIEWS COLLECTION PAGINATION
# Function that displays all reviews and paginates them using flask-paginate

def get_reviews(offset=0, per_page=10):
    
    reviews = mongo.db.reviews.find().sort([("_id", -1)])

    reviews_list = list(reviews)
    
    return reviews_list[ offset: offset + per_page ]

@app.route('/show_collection')
@login_required
def show_collection():
    
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    # Count all reviews
    total = mongo.db.reviews.count_documents({})

    paginated_reviews = get_reviews(offset=offset, per_page=per_page)
    
    pagination = Pagination(page=page, per_page=per_page, total=total)
    
    return render_template('collection.html',
                            reviews=paginated_reviews,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)

# VIEW REVIEW
# Function that renders view review template of a selected by user review

@app.route('/view/<review_id>')
@login_required
def view_review(review_id):
    
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    
    # Display all comments for the review
    review_comments = mongo.db.comments.find({ "review_id": ObjectId(review_id) }).sort([("_id", -1)])
    
    username = current_user.username
    
    # Check if given user upvoted the review
    match_count_upvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'upvote': {'$elemMatch': { "username": username}},
    })
    
    # Check if given user downvoted the review
    match_count_downvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'downvote': {'$elemMatch': { "username": username}},
    })
    
    # Check if user liked / disliked the review to change button's text

    if match_count_upvote > 0:
        
        like_btn = "un-like"
        dislike_btn = "dislike"
        
    elif match_count_downvote > 0:
        
        like_btn = "like"
        dislike_btn = "un-dislike"
        
    else:
        
        like_btn = "like"
        dislike_btn = "dislike"
    
    return render_template('viewreview.html', review=the_review, comments=review_comments, like=like_btn, dislike=dislike_btn)

# DELETE REVIEW
# Function that deletes review from the review collection

@app.route('/delete_review/<review_id>')
@login_required
def delete_review(review_id):
    
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    
    return redirect(url_for('show_collection'))

# EDIT REVIEW
'''
Function that renders edit review template
When user clicks on edit review button, the review form is displayed
'''

@app.route('/edit_review/<review_id>')
@login_required
def edit_review(review_id):
    
    the_review =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    
    return render_template('editreview.html', review=the_review)

# UPDATE REVIEW
'''
Function that submits user input to the database
When user is done updating fields in the form  and clicks on the 'add review'
button the updated records are updated in the reviews collection
'''

@app.route('/update_review/<review_id>', methods=["POST"])
@login_required
def update_review(review_id):
    
    reviews = mongo.db.reviews
    
    # Retrive author and title from the form in order to generate amazon link
    author = request.form['author'].title()
    title = request.form['title'].title()
    
    # Generate amazon link
    amazon_link = generate_amazon_link(title, author)
    
    # Update the review
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
        'amazon': amazon_link
        }
    })
    
    return redirect(url_for('show_collection')) 

# INSERT COMMENT
'''
Function that sends user input (comment) to the comments collection.
It is activated when user clicks "post" button
'''

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

# UPDATE COMMENT
# Function that submits user input to comment collection

@app.route('/update_comment/<review_id>/<comment_id>', methods=["POST"])
@login_required
def update_comment(comment_id, review_id):
    
    comments = mongo.db.comments
    
    comments.update({'_id': ObjectId(comment_id)},
        { '$set': 
            { 'comment': request.form['comment'] }
        })
    
    return redirect(url_for('view_review', comment_id=comment_id, review_id=review_id))

# CANCEL COMMENT
# Function that cancels comment update

@app.route('/cancel_comment/<review_id>')
@login_required
def cancel_comment(review_id):
    
    return redirect(url_for('view_review', _anchor='comments-section', review_id=review_id))

# DELETE COMMENT
# Function that deletes the comment

@app.route('/delete_comment/<review_id>/<comment_id>')
@login_required
def delete_comment(comment_id, review_id):
    
    mongo.db.comments.remove({'_id': ObjectId(comment_id)})
    
    return redirect(url_for('view_review', comment_id=comment_id, review_id=review_id))

# ADD / REMOVE VOTE FUNCTION

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

# UPVOTE                                           
# Functions that allows upvoting and adds increment of 1 to the review table

@app.route('/upvote/<review_id>', methods=['GET', 'POST'])
@login_required
def upvote(review_id):

    username = current_user.username
    
    # Check if given user upvoted the review
    match_count_upvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'upvote': {'$elemMatch': { "username": username}},
    })
    
    # Check if given user downvoted the review
    match_count_downvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'downvote': {'$elemMatch': { "username": username}},
    })
    
    # If user already liked the review then remove his/her upvote
    if match_count_upvote > 0:
        
        remove_vote('upvote', 'upvote_total', review_id, username)
    
    # If user already disliked the review then remove his/her downvote and add upvote
    elif match_count_downvote > 0:
        
        add_vote('upvote', 'upvote_total', review_id, username)
        remove_vote('downvote', 'downvote_total', review_id, username)
        
    # If user did not liked nor dislike the review add upvote
    else:
        
        add_vote('upvote', 'upvote_total', review_id, username)
        
    return redirect(url_for('view_review', review_id=review_id))

# DOOWNVOTE     
# Functions that allows downvoting and adds increment of 1 to the review table

@app.route('/downvote/<review_id>', methods=['GET', 'POST'])
@login_required
def downvote(review_id):
    
    username = current_user.username
    
    # Check if given user upvoted the review
    match_count_upvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'upvote': {'$elemMatch': { "username": username}},
    })
    
    # Check if given user downvoted the review
    match_count_downvote = mongo.db.reviews.count_documents({
        '_id' : ObjectId(review_id),
        'downvote': {'$elemMatch': { "username": username}},
    })
    
    # If user already disliked the review then remove his/her downvote
    if match_count_downvote > 0:
        
        remove_vote('downvote', 'downvote_total', review_id, username)
    
    # If user already liked the review then remove his/her upvote and add downvote                                        
    elif match_count_upvote > 0:
        add_vote('downvote', 'downvote_total', review_id, username)
        remove_vote('upvote', 'upvote_total', review_id, username)
    
    # If user did not liked nor dislike the review add downvote
    else:
        add_vote('downvote', 'downvote_total', review_id, username)
        
    return redirect(url_for('view_review', review_id=review_id))

# SEARCH
'''
Function that enables user to search a review using keywords such as book title,
author, genre etc.
Search returns list of matching results.
'''

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
        
        # If no search input flash the message
        if search_string == '':
            
            logging.error('Entering the empty string if')
            flash('You have not provided any search input!', 'warning')
            
            return redirect('/search')
        
        # If no results display info message     
        elif results_count == 0:
            
            logging.error('Entering no results if')
            flash('No results found!', 'info')
            
            return redirect('/search')
            
        # Display search result
        else:
            
            logging.error('Entering results exist if')
            search_results
            
    return render_template('searchresults.html', reviews=search_results)

# Set up IP address and port number so that AWS how to run and where to run the application 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)