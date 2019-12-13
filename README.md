# Booksy - Book reviews application

Stream Three Project: Data Centric Development - Milestone Project

![alt text](........................... "Gif")

This project is part of the 'Data Centric Development' module of the Code Institute Full Stack Software Development course.

Project consists of the following sections:

1. Homepage - Containing 'sign up' and 'sign in' button when user is not authenticated and 'See our collection' button when user is logged into his / her account.

2. Login form - Page containg the form that enables user to log into their account to use the app.

3. Sign up form - Page containg the form that enables user to sign up for the Booksy app.
 
4. Collection - Page displaying list of paginated reviews.

5. Add review - Page containing the form that enables users to input and submit their book reviews. 

6. Edit review - Page containing the form that pulls a given review that was previously submitted by a user. User is able to amend information and resubmit the review.

7. View review - Page that contacins all information about a given book, including review and summary. Page enables user to edit/delete review, vote and comments on the review.

8. Profile - Page containing user information, such as username, last seen (date and time), and all reviews that a given user added, commented and voted for.

## Table of Contents

- [Demo](#demo)
- [UX](#ux)
- [Database](#database)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

<a name="demo"/>

## Demo

Website demo is available [here](https://booksy-reviews.herokuapp.com/ "booksy-reviews").

<a name="ux"/>

## UX

### UX Design

In this project I was aiming to achieve a simple and user friendly user design, while providing all required information. All sections are arranged in a logical order to provide intuitive user experience.

To create warm and cosy design I used the following colors in my project: white (`#ffffff`), off-white (`#f5f5f5`), light-red (`#e64a1e`), black (`#373737`, `#292826`), grey (`#848482`, `#d2d1d1`), and range of gold / dark-gold colors (`#bdaa6c`, `#a99c72`, `#c0b283`, `#e4d29b`).

### Target Audience

This application aims to attract people that like to read, look for next book to read, like to share their thoughts on books they have read, and interact with other readers. The website provides user with information about various books and reviews, and enables them to share their own revious and interact with other users. Users are also able to upvote / downvote reviews. 

The main objective of the website is to provide a user with a tool that will enable them to read / add / comment / vote for reviews.


### User Stories

The following user stories were used to design this project:

**User Story 1:** As a user I would like to create an account to access reviews available in the app.

**User Story 2:** As a user I would like to be able to delete my account and all content added by me at any point.

**User Story 3:** As a user I would like to have an option to login and logout of my account so nobody else can access it.

**User Story 4:** As a user I would like to explore different books to decide which book I will read next.

**User Story 5:** As a user I would like to be able to add my own reviews and share them with other app users.

**User Story 6:** As a user I would like to be able to go back to any review added by me and edit information about it.

**User Story 7:** As a user I would like to be able to delete any contet added by me (i.e. reviews, comments, votes).

**User Story 8:** As a user I would like to be able to like or dislike any review in order to share my opinion.

**User Story 9:** As a user I would like to be able to interact with other users and share my views and opinions about various books.

**User Story 10:** As a user I would like to see all my inputs within the app (i.e. comments, reviews, votes) in case I would like to edit or delete them.

**User Story 11:** As a user I would like to search any particular book quickly using e.g. book title, author, genre etc.

**User Story 12:** As a user I would like to be sure that no other user is able to edit or delete my input.

**User Story 13:** As a user I would like to see all collection of reviews in an organised, easy to navigate way.

### Mockups & Wireframes

The following [wireframe](..........) sketches were created to design the project layout options for large, medium and mobile displays.

<a name="database"/>

## Database

### Database Type

For this project I used document-oriented cloud database called **MongoDB Atlas**.

My database consists of three collections, namely : users, reviews, comments.

Users collection contains information about each user who signed up for the app. Reviews collection contains information about each book, person who added it and voting information. Comments collection contains comment text, username of person who added it, and id of the review about commented review.

### Database Design

Picture below presents the database schema outlining structure of each collection and relationship between each collection.

![alt text](https://github.com/JBroks/booksy-reviews/blob/master/database_schema/database_schema.png "database_schema")

<a name="features"/>

## Features

### Existing Features

The project consists of various features presented below.

#### Page loading

- **Spinner** - jQuery method `show()` and `hide()` was used to create spinner showing while page is loading;

- **Overlay** - overlay that fades out the background while page is loading;

#### Buttons

- **Buy online button** - link redirecting a user to amazon search for a given review;

- **Like / Dislike button** - voting buttons enabling user to like or dislike a book review;

- **Edit / Delete buttons* - buttons that enable editing and deleting reviews and comments;

- **See our collection button* - buttons that redirects user from the hompage to the paginated collection page;

- **View review button** - button that is linked to the view review page;

- **Delete account button** - button that performs action of deleting an account and all votes, comments and reviews assocciated with it;

- **Cancel buttons** - button that cancels update review or comment;

- **Add review button** - button that submits the new review into the monngoDB database;

- **Update review button** - button that submits the updated review in to the mongoDb database;

- **Back to top button** - static back to top button was implemented at the bottom of the page so user can go back to the top of the page without scrolling back. The feature is especially useful on mobile devices.

#### Forms

- **Sign up form** - flask register form that enables user to use the app. User input includes username, email address, and password (that has to be repeated);

- **Sign in form** - flask login form that enables user to sig into the user account;

- **Post comment form** - form that enables user to post a comment for a given review;

- **Update comment form** - form that enables user to edit and resubmit the comment;

- **Add review form** - form that enables user to add a new review to the website;

- **Edit review form** - form that pulls information about the existing review and enables the user to edit it;

#### Structure

- **Navbar** - the navbar stays collapsed on medium and small devices. To create Materialize mobile collapsed button `class=sidenav-trigger` was applied. The navbar contains brand logo and links to associated sections i.e. Home, Collection, Add Review, Profile, Sign Out;

- **Footer** - contains disclaimer GitHub link and copyrights information;

#### Alerts

- **Toast messages** - `flask_toastr` extension was used to style flash messages and present them as toast messages to the user;

- **Delete confirmation alerts** - alerts created using **Sweetalert2** framework that asks user to confirm deletion.

#### Other

- **Pagination** - `flask_paginate` extension used to paginate reviews, so users view ten reviews per page;

- **Accordion** - Materialize accordion feature that stores book review and summary;

- **Materialize cards** - feature used to present comments added by users;

- **Search bar** - search bar that enables users to search any book by type, genre, title, author etc.

- **Comment counter** - javascritp function added that re-counts comments.

### Features left to implement

List of features to be implemented in the future:

- add and edit username details;

- affiliate link for the amazon link;

- reset password option;

- improved search function.

<a name="technologies-used"/>

## Technologies used

### Programming languages

- **HTML** - The project used HTML to define structure and layout of the web page;

- **CSS** - The project used CSS stylesheets to specify style of the web document elements;

- **JavaScript** - The project used Javascript to implement Maps Javascript API and customize it.

- **Python** - The project back-end functions are written using Python. Flask and Python is used to build route functions;

### Libraries

- [jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - 

- [Sweetalert2](https://sweetalert2.github.io/#download) - 

- [Font Awesome](https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css) - 

- [Google Fonts](https://fonts.google.com/) -  Google Fonts library was used to set up font type for the document;

### Frameworks & Extensions

- [Materialize]() - responsive CSS framework based on Material Design by Google. Materialize was used to create grid layout and to style various features such as cards, acordion, buttons, forms, navbar, and footer.

- [Flask]() - web application framework used to create functions with Python that are injected into html templates. Various flask extensions were used to validate login / register form, create routes, paginate reviews, manage login and logout and create toast messages;

- [Flask-toastr]() - flask extension used to show non-blocking notifications in Flask templates using toastr;

- [Flask-paginate]() - flask extension used to paginate reviews;

- [Flask-login]() - flask extension used to handle the common tasks of logging in, logging out, and remembering users’ sessions;

### Database

- [MongoDB Atlas]() - a fully-managed cloud database used to store manage and query datasets;

### Other

- [Gifox](https://gifox.io/) - Tool was used to record the gif presented in the demo secion of this README files;

- [Am I Responsive](http://ami.responsivedesign.is/#) - Online tool was used to display the project on various devices;

- [MockFlow WireframePro](https://www.mockflow.com/) - Online tool that was used to create wireframes.
- 
- [DBDiagram](https://dbdiagram.io/home) - A relational database diagram design tool used to create database schema.

<a name="testing"/>

## Testing

### Code validation

#### CSS

CSS code was validated using the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/).

.........

#### HTML

HTML code was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

...........

#### JavaScript

JavaScript code was validated using [JSHint](https://jshint.com/).

.......

#### Python

...........

Python code was tested using unittest and flask_testing.

### Features testing

#### Feature 1

##### Bugs:

#### Feature 2

##### Bugs:

### Responsivness testing

This site was tested across multiple browsers (Google Chrome, Safari, Mozilla Firefox, Opera) and on multiple mobile devices (iPad Mini, iPad, Huawei P20) to ensure compatibility and responsiveness.

Chrome developer tools were used to additionally inspect responsiveness for the following devices:

- iPad Pro / iPad / iPad Mini (portrait & landscape);

- iPhone 5/SE (portrait & landscape);

- iPhone 6/7/8 (portrait & landscape);

- iPhone 6/7/8 Plus (portrait & landscape);

- iPhone X (portrait & landscape);

- Android (Pixel 2) (portrait & landscape).

Furthermore, [Responsinator](https://www.responsinator.com/) was used to test responsiveness of the final version of the project.

The website is fully responsive and working well on mobile devices.

#### Bugs:

.....

### Peer-code-review

...........TBC.......

#### Bugs:

...........TBC.......

### User stories testing

**User Story 1:**

- Solution:

**User Story 2:**

- Solution:

<a name="deployment"/>

## Deployment

The site was developed using AWS Cloud 9. To keep records of different versions of all project files git version control system was used. 

In order to track the changes in the local repository the following steps were taken:

- command `git add 'filename'` - to update what will be committed;

- command `git commit` - to commit the changes.

Using `git push` command all changes from the local repository were pushed to the remote one on GitHub.

.............

<a name="credits"/>

## Credits

### Content

..............

### Media

Favicon used for the project was download from [here](https://icons8.com/icons/).

..........

### Acknowledgements

............

### Disclaimer

*This is for educational use.*