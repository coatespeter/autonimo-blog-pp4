# Autonimo Andalucia

Autonimo Andalucia is a job posting website designed to be used by self-employed (Autónomos) people. It currently has listings in four different categories: Land Management, Swimming Pool Maintenance, Transportation, and Handyman Work. It allows users to register and interact with job postings.

- Link to deployed site - [https://autonimo-662c76ca9bdc.herokuapp.com/](https://autonimo-662c76ca9bdc.herokuapp.com/)
- Link to GitHub repository - [https://github.com/coatespeter/autonimo-blog-pp4](https://github.com/coatespeter/autonimo-blog-pp4)


## Table of Contents

- [Autonimo Andalucia](#autonimo-andalucia)
  - [Table of Contents](#table-of-contents)
  - [Wireframes](#wireframes)
  - [Post and Comment Relationship Diagram](#post-and-comment-relationship-diagram)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Future Features](#future-features)
  - [Setting up Django](#setting-up-django)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
    - [Django Testing](#django-testing)
    - [Automated Testing](#automated-testing)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Libraries \& Frameworks](#libraries--frameworks)
    - [Acknowledgements](#acknowledgements)

## Wireframes

- At the beginning of the project, I made up some rough wireframes to give me an idea of what I wanted the site to look like. I used draw.io to create these wireframes. I made a wireframe for the home page and the about page.

![home](static/images/wireframe1.png)
![about](static/images/wireframe2.png)

## Post and Comment Relationship Diagram

![post and comment relationship model](static/images/post:comment_relationship.png)

## User Stories

- As a site user, I can view a paginated list of posts so that I can select which post I want to view.
- As a Site User / Admin, I can view comments on an individual post so that I can read the conversation.
- As a Site User I can register an account so that I can comment on a post.
- As a Site User I can leave comments on a post so that I can interact with the listings
- As a Site User I can modify or delete my comment on a post.
- As a Site Admin I can create, read, update and delete posts so that I can manage the listings.
- As a Site Admin I can create draft posts so that I can finish writing the content later.
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

## Features

- Pagination - The posts are paginated so that the user can view 6 posts per page. There is a link to the next page at the bottom of the page. When the user is not on the first page of listings, there is a link to the previous page.
  
![next](static/images/next-pic.png)
![prev](static/images/prev-pic.png)

- Navbar - The navbar is fixed to the top of the page so that the user can easily navigate the site. The navbar contains links to the home page, about page and the login/logout page and register page.

![navbar](static/images/nav-bar.png)

- login status - When site usere are or are not logged in to the site, there is a banner below the buttons which will tell them their status.

![logged in](static/images/logged-in.png)
![not logged in](static/images/not-logged-in.png)

- About Page - On this page, new users can learn what the site is all about and can follow the instructions to make their own account and interact with the listings. 

![about](static/images/about-intro.png)

- Register Page

![register](static/images/register.png)

- Login Page

![login](static/images/sign-in.png)

- Logout Page

![logout](static/images/sign-out.png)

- Listings Page - On the main listings page, the user can scroll and view a max of 6 listings per page. The user can then click next to see the next page of 6 listings and so on.

![listings](static/images/listings.png)

- Authentication for comments.

![auth](static/images/authentication.png)

- Comments box

![comments](static/images/comment-box.png)

- Comment counter

![comment counter](static/images/comment-counter.png)

- Contact admin form

![contact admin](static/images/contact-form.png)

## Technologies Used

- HTML - The project uses HTML to create the structure of the site.
- CSS - The project uses CSS to style the site.
- JavaScript - JavaScript was used to link the buttons to functionality
- Python - The project uses Python to create the backend of the site.
- Django - The project uses Django as the web framework.
- Heroku - The project is deployed on Heroku.
- Git - The project uses Git for version control.
- GitHub - The project uses GitHub to store the code and to plan the project.
- Postgres - The project uses Postgres as the database.
- Bootstrap - The project uses Bootstrap to style the site.
- Google Fonts - The project uses Google Fonts to import the font used in the site.
- ElephantSQL - The project uses ElephantSQL to host the database.
- Draw.io - The project uses Draw.io to create the wireframe.
- Cloudinary - The project uses Cloudinary to host the images.

## Future Features

- The next feature of the site will likely be a seperate "advertise" page which will contain a form for users to submit their own listings. This will be a feature that will only be available to registered users. It will have inputs for every part of the post and the image upload.

## Setting up Django

- Firstly, I installed all the relevant packages necessary for this site. These were, Django Gunicorn, Psycopg2, Django Heroku, Django Crispy Forms, Pillow, Cloudinary, DJ Database URL, and Whitenoise.
- I then created a new Django project and app.
- I migrated the database and created a superuser.
- I created a Procfile and a requirements.txt file.
- I created an admin account.
- I then created the models for the site and migrated the database again.
- I used Elephantsql to host the database and connected it to the site vis a newly created instance.
- I linked the database to the site using the DJ Database URL package.
- I then created the views and urls for the site.
- I then created the templates for the site.
- I then created the static files for the site.
- I then created the forms for the site.
- I logged into Heroku and created a new app. This app was linked via GitHub to my code base. I was able to deploy early on Heroku and keep an eye out for any bugs during the build process by redeploying the app and making sure everything was working as expected.
- I added the necessary config vars to Heroku to connect the database and the cloudinary image hosting.
  

## Deploying to Heroku

- Firstly, I created a new app on Heroku.
- I then connected the app to my GitHub repository.
- I then added the necessary config vars to Heroku to connect the database and the cloudinary image hosting.
- In the deploy section, I was able to manually deploy the app and keep an eye out for any bugs during the build process by redeploying the app and making sure everything was working as expected.

## Testing

### Manual Testing

|        Component     |       Test       |     Expected Result.      |           Actual Result         |
|----------------------|------------------|---------------------------|---------------------------------|
| Home page display as expected | Click on Home | Home page displayed | Home page with job listings and images visible.  |
| About page link working | Selected About link | About page to display | About page displayed |
| About page displays | Click on About | About page to display as expected | About page displayed paragraph about the site and the table to contact admin |
| Form to register interest | Fill in all form fields | Alert renders on admin about page | Alert appeared on admin and about page |
| Form fields | Skip completing form fields | Alert to please fill in field  | Alert appeared to fill in field |
| Email form field | Fill in email in incorrect format | Alert to include @ in email | Alert appeared to include @ for email |
| Work list display | Click on home | List of blog posts appears as 6 per page | List of work post displayed as 6 per page |
| Next and Prev Buttons | Work as expected | Next brings to next page, prev brings to previous | Next brought to next page, previous brought to previous list of blog posts |
| Full Listing display | On click of listing title in blog list full listing display | Full listing displays | Full listing displayed |
| Comment Counter | Scroll to comment section | Shows users a small graphic with number of comments | Displays correctly |
| Log in Prompt | To display when not log in | Message display in like and comment to prompt a log in | Messaged displayed to visitor to log in to interact with post |
| Like Log in Prompt Link Working | Link to sign in page working | User brought to sign in page when clicked | User is brought to log in page when link |
| Comment | Site User can leave a comment | User can leave a comment and receive confirmation | Member placed comment and received notification that comment is awaiting approval |
| Not logged in Comment | If not logged in cannot comment | Message displaying to prompt visitor to log in if they want to leave a comment | Message displayed to visitor to sign in to leave comment |
| Comment Log in Link | Link working | On click of link user brought to sign in page | User clicked log in link and brought to log in page |
| Edit Comment | Can only edit own comment | Only users own comment can be edited | User could only edit their comment and receive an alert to state they did so |
| Delete Comment | Users can delete own comments | Users can delete comment once confirmation received | User could delete a comment they left once confirming they were happy to do so |
| Sign Up Form | Working as expected | New user created as a result | All fields of form completed and new user created |
| Log In Link on Sign Up page | Link working | On click log in link brings to log in page | User brought to log in page once clicked |
| Sign In Field Validation | Field Validation | Alert user if field missed | Field missed on completing form and alert received to fill in missing field |
| Password Validation | Password | Alert raised if criteria not met | Alert raised as a result of not matching password or too similar to user name |
| Log In Form | Allows user to sign in | User can sign in and gain full functionality of blog | User signed in successfuly when correct credentials supplied |
| Sign Up Link on Log In Page | Link working | On click brought to sign up page | User brought to log in page once clicked |
| Sign Out | User can sign out | Sign out successfully and asked to confirm | User could sign out once they confirmed that was their intention|

## Bugs

![bugs](static/images/message-bug.png)

- I had a but where the user, upon recieving a message, would recieve a message not displaying with a contrast and was therefore, extremely difficult to read. This was fixed by adding the message tag seen below:

![code fix](static/images/comment-green-fix1.png)

![message tag](static/images/message-tag.png)

![message fix](static/images/comment-green.png)

- I had a bug where the deployed site, header and footer were not displaying the correct background color, therefore making the text impossible to read. I fixed this by altering the css, implementing a color via bootstrap and collecting the static files again.

- While testing the site. I found that there were contrast errors I was unaware of during the development process. I discovered this through a Wave report. I fix this by changing the color scheme of the site to be more readable and inclusive.

![wave](static/images/wave.png)

### Django Testing

![django test](static/images/django-tests.png)

### Automated Testing

![w3](static/images/w3-html-posts.png)

![w3](static/images/w3-2.png)

![python linter](static/images/ci-linter-pass.png)

## Credits

### Content

- The content for this site was inspired by the Code Institute Django project "I think therefore I blog".
- I used some Django educational material for some help with the setup of a Django-based site. [Django Tutorial](https://www.youtube.com/watch?v=oU9kN13-Xbs&t=269s)

### Media

- The images used in this site were obtained from [Unsplash](https://unsplash.com/).
- Font - The font I used called Madina One was obtained from [Google Fonts](https://fonts.google.com/).
- Data storage - The data for this site is managed using [ElephantSQL](https://www.elephantsql.com/).

### Libraries & Frameworks

- The site uses the [Django web framework](https://www.djangoproject.com/).
- The site uses the [Bootstrap framework](https://getbootstrap.com/).

### Acknowledgements

- I would like to thank my mentor Luke Buchanan for his help and guidance throughout the project.

- I would also like to thank my wife Philippa for her unwavering support and encouragement throughout the project.

- I would like to thank the Code Institute for the educational material and and support throughout the project.
