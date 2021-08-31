# THE NEWS
#### Video Demo:  <https://youtu.be/fPuHPZpIBSY>
### Description
A simple and responsive news site built using some of the technologies I learned in CS50x: HTML CSS (+Boostrap) Js for Frontend and Flask for Backend along with a news API gotten from https://newsapi.org

* app.py : This contains the main code for the backend of the website. The routes and functions for the routes which defines what happens when a request to specific routes are made.

* helpers.py : This contains two main functions that are crucial to the project, these functions supplies the data gotten from the news API used in the program

* static/content.js : This contains the JavaScript code for implementing the Infinite-Loading Feature of the site that lets the site load more news articles when you scroll to the bottom

* static/scripts.js : This contains JavaScript code for form validation, I originally had a register and login feature in the project but I removed it at the last minute because it's not needed but I left some of the files for it in the project in case I find a use for it later on, but I've closed it out of the website itself.

* static/main.css : Just CSS code for some HTML elements in the website

* templates/index.html : The HTML + Jinja template code for the main page in the website where the user first sees when they go to the website

* templates/layout.html : Basically a template for which other pages in the website are built on, It contains HTML and Jinja template code.

* templates/search.html : An almost exact replica of the index page but it serves as a page for search query results, It contains HTML and Jinja template code.

* templates/login.html + register.html : Disabled pages that were meant to serve as a means for users to login or register an account on the site, It contains HTML and Jinja template code.

About the login and register feature, I wanted the user to be able to create an account on the website and then have their news feed customized so that they only see news based on their specified interests but I ended up not implementing that feature because it would have been complex for my skill level and it also deviates from what I had in mind from my project which is a simple news site where users just see trending news rather than trying to make a simple Quora clone.