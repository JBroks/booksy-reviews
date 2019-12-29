# Booksy - Book reviews application

Stream Three Project: Data Centric Development - Milestone Project

![alt text](https://github.com/JBroks/booksy-reviews/blob/master/gif/booksy.gif "Gif")

This project is part of the 'Data Centric Development' module of the Code Institute Full Stack Software Development course.

Project consists of the following sections:

1. Homepage - Containing 'sign up' and 'sign in' button when user is not authenticated and 'All Reviews' button when user is logged into his / her account.

2. Login form - Page containing the form that enables user to log into their account to use the app.

3. Sign up form - Page containing the form that enables user to sign up for the Booksy app.
 
4. Collection - Page displaying list of paginated reviews.

5. Add review - Page containing the form that enables users to input and submit their book reviews. 

6. Edit review - Page containing the form that pulls a given review that was previously submitted by a user. User is able to amend information and resubmit the review.

7. View review - Page that contains all information about a given book, including review and summary. Page enables user to edit/delete review, vote and comments on the review.

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

To create warm and cosy design I used the following colors in my project: white (`#ffffff`), off-white (`#f5f5f5`), light-red (`#e64a1e`), black (`#373737`, `#292826`), grey (`#848482`, `#d2d1d1`), and range of gold / dark-gold colors (`#796a3b`, `#bdaa6c`, `#a99c72`, `#c0b283`, `#c3bb9e`, `#e4d29b`).

### Target Audience

This application aims to attract people that like to read, look for next book to read, like to share their thoughts on books they have read, and interact with other readers. The website provides user with information about various books and reviews, and enables them to share their own reviews and interact with other users. Users are also able to upvote / downvote reviews. 

The main objective of the website is to provide a user with a tool that will enable them to read / add / comment / vote for reviews.


### User Stories

The following user stories were used to design this project:

**User Story 1:** As a user I would like to create an account to access reviews available in the app.

**User Story 2:** As a user I would like to be able to delete my account and all content added by me at any point.

**User Story 3:** As a user I would like to have an option to login and logout of my account so nobody else can access it.

**User Story 4:** As a user I would like to explore different books to decide which book I will read next.

**User Story 5:** As a user I would like to be able to add my own reviews and share them with other app users.

**User Story 6:** As a user I would like to be able to go back to any review added by me and edit information about it.

**User Story 7:** As a user I would like to be able to delete any content added by me (i.e. reviews, comments, votes).

**User Story 8:** As a user I would like to be able to like or dislike any review in order to share my opinion.

**User Story 9:** As a user I would like to be able to interact with other users and share my views and opinions about various books.

**User Story 10:** As a user I would like to see all of my inputs within the app (i.e. comments, reviews, votes) in case I would like to edit or delete them.

**User Story 11:** As a user I would like to search any particular book quickly using e.g. book title, author, genre etc.

**User Story 12:** As a user I would like to be sure that no other user is able to edit or delete my input.

**User Story 13:** As a user I would like to see all collection of reviews in an organised, easy to navigate way.

### Mockups & Wireframes

The following [wireframe](https://github.com/JBroks/booksy-reviews/blob/master/wireframes/wireframes.png) sketches were created to design the project layout options for large, medium and mobile displays.

<a name="database"/>

## Database

### Database Type

For this project I used document-oriented cloud database called **MongoDB Atlas**.

My database consists of three collections, namely: users, reviews, comments.

Users collection contains information about each user who signed up for the app. Reviews collection contains information about each book, person who added it and voting information. Comments collection contains comment text, username of person who added it, and id of the review about commented review.

### Database Design

Picture below presents the database schema outlining structure of each collection and relationship between each collection.

![alt text](https://github.com/JBroks/booksy-reviews/blob/master/diagrams/database-schema.png "database-schema")

Relationships between collections are as follows:

- users and comments - one to many relationship as one record in user collection can be associated with many records in the comments collection;

- users and reviews - one to many relationship as one record in user collection can be associated with many records in the reviews collection;

- reviews and comments - one to many relationship as one record in reviews collection can be associated with many records in the comments collection.

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

- **Edit / Delete buttons** - buttons that enable editing and deleting reviews and comments;

- **All Reviews button** - buttons that redirects user from the homepage to the paginated collection page;

- **View review button** - button that is linked to the view review page;

- **Delete account button** - button that performs action of deleting an account and all votes, comments and reviews associated with it;

- **Cancel buttons** - button that cancels update review or comment;

- **Add review button** - button that submits the new review into the mongoDB database;

- **Update review button** - button that submits the updated review in to the mongoDB database;

- **Back to top button** - static back to top button was implemented at the bottom of the page so user can go back to the top of the page without scrolling back. The feature is especially useful on mobile devices.

- **Show more / Show less buttons** - anchors used to toggle Materialize `class="truncate"` to manage very long comments;

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

- **Tabs** - Materialize tabs feature used to contain user content on the profile page;

- **Materialize cards** - feature used to present comments added by users;

- **Search bar** - search bar that enables users to search any book by type, genre, title, author etc.

- **Comment counter** - JavaScript function added that re-counts comments.

### Features left to implement

List of features to be implemented in the future:

- add and edit username details;

- affiliate link for the amazon link (for now only tag added to all amazon links);

- reset password option;

- improved search function to find e.g. partial words;

- add search button as additional option to enter search input;

- add filters by e.g. genre, type, or year;

- review any issues that will appear due to mongoDB upgrade.

<a name="technologies-used"/>

## Technologies used

### Programming languages

- **HTML** - the project used HTML to define structure and layout of the web page;

- **CSS** - the project used CSS stylesheets to specify style of the web document elements;

- **JavaScript** - the project used JavaScript to implement Maps JavaScript API and customize it.

- **Python** - the project back-end functions are written using Python. Flask and Python is used to build route functions;

### Libraries

- [jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - used to initialize elements of Materialize framework, to manage spinner overlay (fade out), search bar (submit input on enter), back to top button (smooth scroll), comment counter (re-count comments), and deletion confirmation (with ajax);

- [Sweetalert2](https://sweetalert2.github.io/#download) - it was used to create customizable alert pop up boxes;

- [Google Fonts](https://fonts.google.com/) - Google Fonts library was used to set up font type for the document;

### Frameworks & Extensions

- [Materialize](https://materializecss.com/) - responsive CSS framework based on Material Design by Google. Materialize was used to create grid layout and to style various features such as cards, accordion, buttons, forms, navbar, and footer.

- [Flask](http://flask.palletsprojects.com/en/1.1.x/) - web application framework used to create functions with Python that are injected into html templates. Various flask extensions were used to validate login / register form, create routes, paginate reviews, manage login and logout and create toast messages;

- [Flask-toastr](https://github.com/wiltonsr/Flask-Toastr) - flask extension used to show non-blocking notifications in Flask templates using toastr;

- [Flask-paginate](https://pythonhosted.org/Flask-paginate/) - flask extension used to paginate reviews;

- [Flask-login](https://flask-login.readthedocs.io/en/latest/) - flask extension used to handle the common tasks of logging in, logging out, and remembering users’ sessions;

- [Flask-testing](https://readthedocs.org/projects/flask-testing/downloads/pdf/latest/) - flask extension used to test flask routes;

### Database

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - a fully-managed cloud database used to store manage and query datasets;

### Other

- [Gifox](https://gifox.io/) - Tool was used to record the gif presented in the demo section of this README files;

- [Am I Responsive](http://ami.responsivedesign.is/#) - Online tool was used to display the project on various devices;

- [MockFlow WireframePro](https://www.mockflow.com/) - Online tool that was used to create wireframes;

- [DBDiagram](https://dbdiagram.io/home) - A relational database diagram design tool used to create database schema.

- [Placeholder](https://placeholder.com/) - Online tool to create custom placeholder images. It was used to create image placeholder in cases when user did not provide a link to book cover image.

<a name="testing"/>

## Testing

### Code validation

#### CSS

CSS code was validated using the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/).

While validating CSS code the following warning appeared: 

```
Imported style sheets are not checked in direct input and file upload modes
```

This warning remains unresolved as it is only an information stating that validator is not able to validate imported stylesheets.

#### HTML

HTML code was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

The following issues were captured by the validator:

- The following issue appeared in the **add_review**, **edit_review** and **base** template and it was resolved by amending `for` attribute:
   ```
   The value of the for attribute of the label element must be the ID of a non-hidden form control.
   ```

- The following issue appeared in the login and register form. `action` attribute was removed as the submit is handled by flask:
  ```
  Bad value for attribute action on element form: Must be non-empty
  ```

- The following issue appeared in the **profile** template and it was fixed by replacing id with class:
  ```
  Duplicate ID profile-review-title
  ```

- The following issue highlighted for the **profile** and **view_review** template:
  ```
  Attribute href-return not allowed on element a at this point.
  ```
  The issue was resolved by removal of the attribute and adjustments made to the jQuery. `window.location.replace($(".delete-btn a").attr('href-return'));` code was replaced with `window.location.href='/show_collection'` for reviews deleted from the 'View review' page, with `window.location.href='/index'` for the account deletion, and with `window.location.reload()` for the reviews deleted from the **profile** template;

- The following issue highlighted for the **search_results** and **view_review** templates:
  ```
  Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections.
  ```
  This warning was ignored as no additional heading is required.

All warnings related to Jinja templates syntax were ignored as they are not recognised by the HTML validator.

#### JavaScript

JavaScript code was validated using [JSHint](https://jshint.com/).

Validator has indicated that there are two unknown / undefined variables, namely `$`, and `Swal`. The warning was ignored as I believe it is due to the fact that these libraries are separated and the validator does not have access to them.

Four unused variables were flagged, namely `confirmDel`, `confirmDelView`, `confirmDelCom`, `confirmationAcc`. The warning was ignored as these functions are activated by onlclick event.

#### Python

In order to debug python code while coding I used logging module (`import logging`) and pdb module (`import pdb`).

Python code was tested using unittest framework ([test.py](https://github.com/JBroks/booksy-reviews/blob/master/test.py) file). Flask routes ([test_routes.py](https://github.com/JBroks/booksy-reviews/blob/master/test_routes.py) file) was tested using unittest framework and flask_testing extension, the following tests were run:

- test for pages loading correctly without user being authenticated;

- test for each field in the register form;

- test for each field in the login form;

- test for user login.

All remaining features were tested manually. 

### Features testing

All the features were tested manually throughout the application development process. Table below outlines all features and tests performed on them, as well as all resolved and remaining bugs associated with tested features.

| Feature type                         | Feature                                  | Tests                                                                                                                                                                                                                                                                                                                                                                                                                       | Bugs                                                  |
| ------------------------------------ | :--------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------:|
| Page loading                         | Spinner                                  | - test if spinner appears when page is loading and disappears when the page is ready;<br> - test if spinner is on top of the overlay                                                                                                                                                                                                                                                                                         | No bugs.                                                |
|                                      | Overlay                                  | - test if overlay covers page when it is loading and disappears when the page is ready                                                                                                                                                                                                                                                                                                                                      | No bugs.                                                |
| Buttons (including anchor links)     | Buy online button                        | - test if button redirects to amazon;<br> - test if search of a given book performed correctly;<br> - test if amazon page opens in a new tab                                                                                                                                                                                                                                                                                  | Initially there was an issue<br>with '&' symbol but<br>function was adjusted<br>to replace it with 'and'.<br>Function has to be improved<br>to take into account <br>other scenarios such as<br>e.g. link contains other tag. |
|                                      | Like / Dislike button                    | - test if button not showing for the user that added a given content (i.e. user who added review should not be able to like it);<br> - test if text on the button changes afer clicking the button;<br> - check if vote added to the reviews collection;<br> - check if total incremented accordingly after vote has been added;<br> - check if 'View review' and 'Collection' page displays correct number of Likes / Dislikes; | No bugs remaining.                                      |
|                                      | Delete review button                     | - test if button available only for the content added by the authenticated user;<br> - test if confirmation message pops up after button has been clicked;<br> - test if item is not deleted after user clicks 'Cancel' on confirmation pop up;<br> - test if review deleted permanently from the database after user confirms the deletion;<br> - test if page is redirected correctly after deletion;                         | No bugs remaining.                                      |
|                                      | Delete account button                    | - test if confirmation message pops up after button has been clicked;<br> - test if item is not deleted after user clicks 'Cancel' on confirmation pop up;<br> - test if account and all user votes, comments and reviews are deleted permanently from the database after user confirms the deletion;<br> - test if page is redirected correctly after deletion;                                                               | No bugs remaining.                                      |
|                                      | Delete comment button                    | - test if button available only for the content added by the authenticated user;<br> - test if comment deleted from the database correctly;<br> - test if comment removed from the display on 'View review page';<br> - check if comment counter adjusted accordingly;                                                                                                                                                          |                                                         |
|                                      | Edit review button                       | - test if button available only for the content added by the authenticated user;<br> - test if button redirects user to the correct page;<br> - check if form displays information about correct review;                                                                                                                                                                                                                       | No bugs remaining.                                      |
|                                      | Edit comment button                      | - test if button available only for the content added by the authenticated user;<br> - test if card is replaced with editable form;<br> - check if 'Update' and 'Cancel buttons are being displayed after 'Edit' button is clicked;                                                                                                                                                                                            | No bugs remaining.                                      |
|                                      | All reviews button                       | - test if button is only showing when user is authenticated;<br> - test if button redirects user to paginated collection;<br> - test if button is not displayed when user is not authenticated;                                                                                                                                                                                                                                | No bugs remaining.                                      |
|                                      | View review button                       | - test if button redirects user to 'View review' page;<br> - test if correct review is being displayed;                                                                                                                                                                                                                                                                                                                       | No bugs.                                                |
|                                      | Cancel button                            | - test if button cancels all actions correctly (i.e. does not submit any changes made to the form);<br> - test if page if redirected correctly (as per template);<br> - in case of the cancel comment update, test if editable form is hidden and card with comment is displayed;<br> - in case of the cancel comment update, test if anchor works and page returns to the comments section;                                    | No bugs.                                                |
|                                      | Add review button                        | - test if button submits the data from the form to the reviews collection;<br> - test if page if redirected correctly (as per template);                                                                                                                                                                                                                                                                                      | No bugs.                                                |
|                                      | Post comment button                      | - test if button submits the data from the form to the comments collection;<br> - test if page if redirected correctly (as per template) and if anchor works;                                                                                                                                                                                                                                                                 | No bugs.                                                |
|                                      | Update review button                     | - test if button submits the data from the form to the reviews collection;<br> - test if page if redirected correctly (as per template);                                                                                                                                                                                                                                                                                      | No bugs.                                                |
|                                      | Update comment button                    | - test if button submits the data from the form to the comments collection;<br> - test if page if redirected correctly (as per template) and if anchor works (i.e. page redirected to the comments section);                                                                                                                                                                                                                  | No bugs.                                                |
|                                      | Back to top button                       | - test if clicking the button scrolls the page back to the top;                                                                                                                                                                                                                                                                                                                                                              | No bugs.                                                |
|                                      | GitHub link                              | - test if clicking the link redirects user to my repository;<br> - test if GitHub page opens in a new tab;                                                                                                                                                                                                                                                                                                                    | No bugs.                                                |
|                                      | Show more / show less                    | - test if clicking the link show less or more text;<br> - test if short comments (not truncated) don't display 'show more' button;                                                                                                                                                                                                                                                                                                                    | No bugs.                                                |
| Forms                                | Sign up form                             | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;<br> - test if password hashing works i.e. password saved to database is hashed;                                                                                                                                       | Initially username was<br>case sensitive but<br>that was fixed by applying<br>python `lower()` method<br>to the username. |
|                                      | Sign in form                             | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test is user can log in using incorrect password;                                                                                                                                                                                                                                   | Initially username was<br>case sensitive but<br>that was fixed by applying<br>python `lower()` method<br>to the username. |
|                                      | Add review form, Post comment form       | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                                                                                      | No bugs.                                                  |
|                                      | Update comment form, Edit review form    | - test if update forms pull data correctly from the database;<br> - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                     | Bug related to updates<br>in situation when<br>only some fields where update<br>other fields where removed.<br>Bug fixed using `$set`<br>mongoDB operator to only update<br>fields edited by the user. |
| Structure                            | Navbar                                   | - test if all navbar menu items redirect user to the appropriate page;<br> - test if item that is currently active is highlighted;<br> - test if navbar collapses on smaller devices;                                                                                                                                                                                                                                          | No bugs.                                                 |
|                                      | Footer                                   | - test if GitHub link works correctly;<br> - test if footer stays at the bottom of the page;                                                                                                                                                                                                                                                                                                                                  | No bugs.                                                 |
| Alerts                               | Toast messages                           | - test if all flash messages are styled with toastr;<br> - test if no text is cut off;<br> - test if delete button and progress displays correctly;<br> - test if different colors applied to different categories of toast messages;                                                                                                                                                                                           | No unresolved bugs left.                                 |
|                                      | Delete confirmation messages             | - test if confirmation message pops up when trying to delete a review or account;<br> - test if clicking 'delete' button on the message performs deleting;<br> - test if clicking 'cancel' cancels the action;                                                                                                                                                                                                                 | No unresolved bugs left.                                 |
| Other                                | Pagination                               | - test if ten reviews per page are displayed;<br> - test pagination links;<br> - check if total number of reviews is with accordance to the total number of records in the database;                                                                                                                                                                                                                                           | No unresolved bugs.<br>Initially pagination<br>did not work properly<br>but moving<br>`reviews = mongo.db.reviews.find().sort([("_id", -1)])`<br>inside the `get_reviews()`<br>function fixed the issue. |
|                                      | Accordion                                | - check if only one element is un-wrapped at the time;<br> test if clicking on the heading un-wraps the correct element;                                                                                                                                                                                                                                                                                                      | No bugs.                                                 |
|                                      | Tabs                                     | - check if tabs change when tab `li` is clicked;<br> test if information displays correctly in the tab;                                                                                                                                                                                                                                                                                                      | No bugs.                                                 |
|                                      | Search bar                               | - test various search bar inputs (ones that exist in the database and ones that do not);<br> - test search bar with no input provided;<br> - test if inputs are submitted on 'enter';<br> - check if search bar in not collapsing along with other menu items on smaller devices;                                                                                                                                               | Issue with the search bar<br>placeholder on Safari browser<br>(offset and not visible)<br>was fixed by setting `line-height`<br>property from `inherit` to `initial` |
|                                      | Comment counter                          | - test if comment counter is updated whenever comments is added or deleted;<br> - test if counter re-calculates the total when one user adds multiple comments;<br> - test if it re-calculates the total when different users add comments;<br> - test if it re-calculates the total when user account is deleted and multiple comments along with it;                                                                          | Error `Cannot set property 'innerHTML' of null`<br>resolved with [this](https://stackoverflow.com/questions/18239430/cannot-set-property-innerhtml-of-null) solution. |

### Responsiveness testing

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

No bugs left unresolved.

### Peer-code-review

The project was published on Code Institute Slack code-peer-review channel where other students and mentors are able to review the code and provide their feedback. No additional comments were provided.

#### Bugs:

No bugs as no feedback was provided.

### User stories testing

**User Story 1:**

- Solution: Any user can create their own account by using the register form. User has to provide username, email and password in order to register. After successful registration user can login in using the login form. When logged in user can explore all reviews, add their own reviews, comments and votes.

**User Story 2:**

- Solution: 'Delete Account' button in the 'Profile' page enables user to delete his / her account and all reviews, comments and votes added by that user.

**User Story 3:**

- Solution: Login form enables user to login to his / her account. Whenever user wants to logout he / she can click 'Sign out' located in the navbar menu. When user is not authenticated nobody else can access their account unless they know username and password of that user.

**User Story 4:**

- Solution: Users are able to use 'All reviews' button on the homepage, 'Collection' option in the navbar menu or search bar to explore reviews added to the application.

**User Story 5:**

- Solution: User can add his / her review to the overall collection by clicking 'Add review' option in the navbar menu. When review is submitted all other users can view, comment and post their votes.

**User Story 6:**

- Solution: User can at any point edit review that he / she added. All reviews added by the user will be listed in the 'Profile' page (along with edit and delete button). Edit and delete function is also available on the 'View review' page. After clicking 'Edit' button all information is presented to the user and can be edited. After user clicks 'Update review' button updated reviews are submitted to the database and displayed in the app.

**User Story 7:**

- Solution: User can at any point delete his / her review (from 'Profile' or 'View review' page), comments (from 'View review' page), and Likes / Dislikes (from 'View review' page). Reviews and comments are removed by clicking 'Delete' button and Likes / Dislikes are removed by clicking Like / Dislike button again.

**User Story 8:**

- Solution: User can Like / Dislike all reviews added by other users (so not his / her own). When e.g. user clicks on the Like button his / her vote is submitted to the database and text displayed on the button changes to the 'Un-like' so the user knows that he / she already voted for a given review. If user wishes to remove the vote he / she can click on the 'Un-like' button, the vote will be removed and button text will turn back to 'Like'.

**User Story 9:**

- Solution: User can comment any review in order to share his / her opinion and interact with other users.

**User Story 10:**

- Solution: User can see all his / her inputs i.e. added reviews, comments and votes on the 'Profile' page. Reviews can be deleted directly from the 'Profile' page. Comments and votes can only be removed from the 'View review' page, however link to all reviews commented / voted for by the user are available on the 'Profile' page. 

**User Story 11:**

- Solution: User can search reviews by typing title, author, genre, type etc. in the search bar.

**User Story 12:**

- Solution: Only authenticated user can edit and delete his / her content. 

**User Story 13:**

- Solution: Reviews collection is paginated using flask-paginate extension.

<a name="deployment"/>

## Deployment

### GitHub

The site was developed using AWS Cloud 9. To keep records of different versions of all project files git version control system was used. 

To initialize the local repository the command `$ git init` was used. After adding initial files and committing them `$ git remote add origin 'GitHub repo name'` command was used to add new remote repository. Code was then pushed to the master branch of the remote repository using `$ git push -u origin master`.

In order to track the changes in the local repository the following steps were taken:

- command `$ git add 'filename'` - to update what will be committed;

- command `$ git commit` - to commit the changes.

Using `$ git push` command all changes from the local repository were pushed to the remote one on GitHub.

### Heroku

This project is hosted using Heroku, deployed directly from the `master` branch. 

To deploy my project I followed these steps:

1. Create App: 

     - On Heroku website I logged onto my account and created [my app](https://dashboard.heroku.com/apps/booksy-reviews);
     - Under the **Settings** tab I clicked button **Reveal Config Vars** and I set the IP to 0.0.0.0 and the PORT to 5000;
     - At the later stage configuration for the MongoDB database were added, namely 'MONGO URI' and 'SECRET KEY';

2. Install the Heroku CLI: 

     - To install Heroku CLI I typed `$ sudo snap install --classic heroku` command into the terminal; 
     - In order to log in to the Heroku account I typed `$ heroku login` command into the terminal;

3. Git repository:

     - If repository not created already the following commands should be used in order to initialize a git repository in a new or existing directory: 
        ```
        $ cd 'directory-name'/
        $ git init
        $ heroku git:remote -a 'app-name''
        ```
        
    - For existing repositories add the Heroku remote should be used: `$ heroku git:remote -a 'app-name'`;

4. Requirements:

    - In order to run the app Heroku needs to install the required dependencies so make sure that 'requirements.txt' file was created and committed;
    - In order to create 'requirements.txt' file run `$ sudo pip3 freeze --local > requirements.txt` command in the terminal;

5. Procfile:

    - Procfile is a Heroku specific type of file that tells Heroku how to run our project;
    - For the 'Procfile' run `$ echo web: python > Procfile` command in the terminal;
    - In order to start web processes run `heroku ps:scale web=1` command in the terminal;

5. Deployment: Committed code was deployed to Heroku using the following command: `$ git push heroku master`.

           
<a name="credits"/>

## Credits

### Content

Reviews, book information and comments are based on two main sources, namely [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) and [Goodreads](https://www.goodreads.com/).

### Media

Favicon used for the project was created and downloaded from [here](https://favicon.io/favicon-generator/).

Image that constitutes the background for all pages was downloaded from [here](https://www.qualtrics.com/m/assets/blog/wp-content/uploads/2018/08/shutterstock_1068141515.jpg)

### Acknowledgements

While working with MongoDB Atlas I relied heavily on [MongoDB documentation](https://docs.mongodb.com/manual/reference/).

To paginate reviews collection I used [flask-paginate docs](https://pythonhosted.org/Flask-paginate/) and [this](https://github.com/DarilliGames/flaskpaginate) example presented by Stephen Moody (Tutor at Code Institute)

To learn how to create login I used [flask-login docs](https://flask-login.readthedocs.io/en/latest/) and [this](https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb) stackoverflow example.

I used [flask-testing docs](https://pythonhosted.org/Flask-Testing/) to learn about testing flask application.

[This](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial by Miguel Grinberg was also used to learn about elements (e.g. login, registration form etc.). 

[This](https://stackoverflow.com/questions/37194886/does-materialize-css-framework-have-a-container-fluid-equivalent) stackoverflow solution was used to create equivalent to Bootstrap `container-fluid` class.

[This](https://stackoverflow.com/questions/477691/submitting-a-form-by-pressing-enter-without-a-submit-button) stackoverflow discussion when working on search bar submit.

[This](https://stackoverflow.com/questions/45842597/prevall-not-working-in-more-complicated-dom) stackoverflow solution was used to make card with a comment be replaced with the editable comment form.

[This](https://stackoverflow.com/questions/45389140/handling-ajax-return-values-in-sweetalert2) stackoverflow solution inspired functions for delete confirmation using ajax and Sweetalert2.

Styling active item in the navbar menu was inspired by [this](https://stackoverflow.com/questions/22173041/styling-active-element-menu-in-flask) solution. 

To learn more about creating Materialize search bar [this](https://www.jquery-az.com/10-examples-learn-creating-materialize-navbar/) tutorial was used.

[This](https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string) solution used for `generate_amazon_link` and `generate_cover` functions.

Information about amazon affiliate links found in [here](https://amazon-affiliate.eu/en/how-to-add-amazon-affiliate-links/).

Function that checks if text was truncated was inspired by [this](https://jsfiddle.net/wzeLmnbo/) code found in [this](https://stackoverflow.com/questions/7738117/html-text-overflow-ellipsis-detection) discussion.

Many thanks to my mentor **Maranatha Ilesanmi** for support and advice throughout the project.

### Disclaimer

*This is for educational use.*