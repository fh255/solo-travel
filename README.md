# Solo Travel - Traveling Blog

This is my fourth milestone project with Code Institute. Solo Travel is a Django-based blog application designed for travel enthusiasts, especially those who love exploring the World.

The site allows users to share their travel stories, upload photos from their journeys, and interact with other posts by commenting, liking, and disliking the liked comments.

[View the live project here.](https://future-travel2024-0cad95f48932.herokuapp.com/)

<img width="934" alt="Mock up" src="https://github.com/fh255/solo-travel/assets/34744096/b412e0ca-aee8-416a-ab09-f772945ee9f1">

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
  * [Project Goals:](#project-goals)
  * [Strategy:](#strategy)
  * [User stories:](#user-stories)
* [Features](#features)
  * [Existing Features](#existing-features)
    * [Navigation bar:](#navigation-bar)
    * [Home page:](#home-page)
    * [Post detail page:](#post-detail-page)
    * [Add post page:](#add-post-page)
    * [Post edit page:](#post-edit-page)
    * [Delete post :](#delete-post)
    * [Sign_up page:](#sign-up-page)
    * [Login page:](#login-page)
    * [Logout page:](#logout-page)
    * [Django Admin page:](#django-admin-page)
    * [System messages:](#system-messages)
    * [Footer:](#footer)
* [Design](#design)
  * [Colours](#colours)
  * [Typography](#typography)
  * [Entity Relationship diagrams for DBMS](#entity-relationship-diagrams-for-DBMS)
  * [Imagery](#imagery)
* [Technologies Used](#technologies-used)
  * [Languages Used:](#languages-used)
  * [Frameworks and Libraries Used:](#frameworks-and-libraries-used)
  * [Software and Web Applications Used:](#software-and-web-applications-used)
* [Testing](#testing)
  * [Browser Testing](#browser-testing)
  * [Responsiveness](#responsiveness)
  * [Validator Testing](#validator-testing)
    * [W3C Markup Validator:](#w3c-markup-validator)
    * [W3C CSS Validator:](#w3c-css-validator)
    * [JSHint:](#jshint)
    * [PEP8 Online:](#pep8-online)
    * [Lighthouse:](#lighthouse)
  * [Test Cases for Models](#test-cases-for-models)
  * [Solved bugs](#solved-bugs)
  * [Known bugs](#known-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Project Goals:
The main objective of this project is to develop a travel blog that offers full CRUD functionality for registered users. This allows users to Create, Read, Update, and Delete their own blog posts and comments directly on the site, without any delays or intermediaries. Users will have complete control over their content, with all changes being immediately reflected on the site.

### Strategy:
An Agile methodology was employed to plan and execute this project. The project management was facilitated through a Kanban board on GitHub Projects, where tasks were organized into three main columns: To Do, In Progress, and Done. This structure ensured a clear visual representation of the project workflow and helped maintain focus on task progression and completion.

To achieve the project goals, the work was divided into 21 distinct parts, each representing a significant component or feature. These parts were tracked through the Kanban board, allowing for efficient prioritization and management of tasks.

The tasks within the project were categorized using labels to indicate their priority and progress status. The labels and their distribution among the tasks were as follows:

  - To Do: Tasks that are yet to be started.
  - In Progress: Tasks currently being worked on.
  - Done: Tasks that have been completed.

For more information: [View the Kanban Board](https://github.com/users/fh255/projects/7/views/1)

### User stories:
 - User Story: Create django environment:
      - As an admin I want to Create a django environment so that I can write and run my code without any Barrier.
 - User Story: Account Registration:
      - As a new user,I want to register for an account on the platform,so that I can access and use the platform's features and services. 
 - User Story: Heroku Deployment :
      - As a developer,I want to deploy my application to Heroku, so that it can be accessible online and I can demonstrate its functionality to users.
 - User Story: Integrate ElephantSQL Database:
      - As a registered user, I want to post comments on articles or posts, so that I can engage with the content and share my thoughts with other users.
 - User Story: Comments on a Post:
      - As a registered user, I want to post comments on articles or posts, so that I can engage with the content and share my thoughts with other users.
 - User Story: Approve Comments:
      - As an admin, I want to approve comments before they are published, so that I can ensure the content is appropriate and adheres to community guidelines.
 - User Story: Create Comments:
      - As a registered user,I want to create comments on posts, so that I can engage in discussions and share my thoughts with the community.
 - User Story Edit post:
      - As a registered user who has created a post, I want to edit my post so that I can update or correct the content.
   - Delete post:
      - As a registered user who has created a post, I want to delete my post so that I can remove content that is no longer relevant or necessary.
 - User Story: Message Alert:
      - As a user, I want to see alert messages displayed in a clear and visually appealing manner so that I can easily understand important notifications.
 -  User Story: Images & Multiple Images:
      - As a User, I want to add multiple images to my travel posts so that I can visually share my experiences and adventures with others.
 - User Story: Account Registration
      - As a new user,I want to register for an account on the platform,so that I can access and use the platform's features and services.
 - User Story: User Login:
      - As a registered user, I want to log into my account,So that I can access personalised features and content on the Solo Travel Blog.
 - User Story: User Logout:
      - As a logged-in user, I want to log out of my account so that I can securely end my session on the Solo Travel Blog.
 - User Story: Likes/Unlikes on Comments:
      -  As a registered user, I want to like or unlike comments on posts, so that I can express my agreement with the comments and then again disagreement with the liked comments.
 - User Story: Number of Comments:
      - As a site user, I want to see the number of comments displayed without entering the detail page for each post so that I can quickly identify popular and engaging posts.
 - User Story: Number of Likes:
      - As a site user, I want to see the number of likes displayed without entering the detail page for each post so that I can quickly gauge popular and interesting content.
 - User Story: View Comments:
      - As a Site User, I want to view comments on an individual post so that I can read and participate in the conversation. 
 - User Story: Hero Image:
      - As a Site User, I want to be presented with a hero image so that I can quickly grasp the purpose and essence of the site.
 - User Story: Design:
      - As a Site User, I want to have an overall positive impression of the site based on principles of user experience design, accessibility, and responsivity so that I can quickly understand its purpose and enjoy using it.
 - User Story: Responsive:
      - As a Site User, I want to use the site seamlessly across desktops, laptops, tablets, and smartphones so that I can access all functionalities regardless of the device I'm using.
   
## Features

### Existing Features

#### Navigation bar:
The site's navigation bar is consistently visible across all pages, utilizing Bootstrap's **fixed-top** class to remain fixed at the top of the browser viewport as the user scrolls.

On the left-hand side of the navigation bar, users will find the Blog name "Solo|Travel". Clicking on this name redirects users to the home page.

Following the Blog name, navigation links to other pages of the site are displayed. Depending on the user's login status, additional links may be present.
  - Not logged in: Home, Add Post, Register, Login

<img width="619" alt="login" src="https://github.com/fh255/solo-travel/assets/34744096/1956b693-fd9b-4666-90ee-8bed872d869c">


  - Logged in: Home, Add Post, Logout
<img width="507" alt="logout" src="https://github.com/fh255/solo-travel/assets/34744096/6a9656d7-6c46-4b32-aba1-7220fad47c06">



The navbar is fully responsive; on smaller devices, it collapses, and navigation links are accessed through a "hamburger menu".

<details>
<summary>View collapsed navbar:</summary>

<img width="485" alt="collapse" src="https://github.com/fh255/solo-travel/assets/34744096/1ae3f472-6388-4500-abee-3e8d1ec84319">
</details>

#### Home page:

##### Home page - Hero section:
At the top of the homepage, this section greets users with a background image of a person walking in a desert. On larger screens, the background image is set to "background-attachment: fixed," creating an appealing scrolling effect. A large text overlay reading "Solo Travel" features an included link that redirects users to the login page.
<img width="1264" alt="Home" src="https://github.com/fh255/solo-travel/assets/34744096/968adfa9-701c-4cb6-b235-f0aa82e9a53c">

<details>
<summary>Hero section on mobile devices:</summary>

![Hero Small]<img width="188" alt="Home-small" src="https://github.com/fh255/solo-travel/assets/34744096/da7dab4b-a230-404c-9464-40c17ab5891e">

</details>

When users browse the pages, they can view the three most recent blog posts, which include:
 - Featured Image: This can either be an image uploaded by the user when creating the post.
 - Author: The person who authored the post.
 - Title: The title of the post.
 - Date Created: The date when the post was created.
 - Likes: Displayed as a heart icon (Font Awesome: far fa-heart) followed by the number of likes received.
 - Comments: Displayed as a comments icon (Font Awesome: far fa-comments) followed by the number of comments posted.
<img width="1270" alt="body" src="https://github.com/fh255/solo-travel/assets/34744096/3b38664e-408f-445e-a709-4776affc0993">
When users click on a post, they are redirected to the detailed page for that specific post.
<details>
<summary>Home page on mobile devices:</summary>
<img width="454" alt="home_sm" src="https://github.com/fh255/solo-travel/assets/34744096/5efdae5b-25bf-4bd2-83a0-3a10d0a7b947">
</details>

#### Add post page:
This feature is available only to registered users and can be accessed via the provided navbar link. On the "Add Post" page, users can share their traveling stories and add photos to their post content.

<img width="555" alt="Add_post" src="https://github.com/fh255/solo-travel/assets/34744096/5777313c-09ce-4a2d-8db9-ff78ce41b823">

To submit a post, the following fields are required:
 - Title: A default post title is presented as the headline of the post. The user can choose to change this, but it must be unique.
 - Content: The user is presented with a "What You See Is What You Get" (WYSIWYG) editor and can use the included toolbar to upload photos and change the content.
 - Status: This field must be set to "Published." If not, the post will be saved as a draft.
   
When all fields are completed and the user clicks on "Post," their post will be automatically added to the list of posts, and the user will be redirected to the details page of their blog post.

#### Post detail page:
When a user clicks on a blog post, they are brought to the Post Detail page. On this page, the user is shown the entire post, along with a commenting section below. The user's ability to interact with the content depends on their status.

<img width="1265" alt="Post_details" src="https://github.com/fh255/solo-travel/assets/34744096/16853a3a-e1fd-45db-98eb-60cc4a2ac355">

The following information will be presented to the user on the Post Detail page:

- Featured Image: The image that the user uploaded when creating the post.
 - Title: The post title.
 - Author: The post author.
 - Date Created: The date when the post was created.
 - Content: The full post content.
 - Number of Likes: A Font Awesome heart icon (fa-heart) followed by the number of likes.
 - Number of Comments: A Font Awesome comments icon (fas fa-comments) followed by the number of comments.
 - Comments: Comments are ordered by date in ascending order.

Features Dependent on User Status:
 - User Not Logged In: The comment form is not displayed. Instead, the user is presented with links to the Login and Register pages. Users must be logged in to leave a comment.
   
<img width="928" alt="Logout_comment" src="https://github.com/fh255/solo-travel/assets/34744096/124baa16-4bf1-4a7f-80ad-2cd350570427">

 - Logged-In User Features:
     - Commenting: The comment form is displayed, allowing the user to comment on the post. When the user clicks "Submit," the comment is automatically approved and added to the list of comments. This immediate approval encourages continued engagement without delays.
     - The Font Awesome heart icon (fa-heart) changes color to indicate a liked post.
     - The user can liking or unliking the post.

 <img width="1150" alt="edit_comment" src="https://github.com/fh255/solo-travel/assets/34744096/dc129e74-de0d-4533-bf36-454e41d9f724">

 #### Post edit page:
 Authors can update their blog posts via the dedicated Post Update page, accessible from the "Update this post" link on the Post Detail page. This feature grants authors full control over their published content, allowing them to effortlessly edit and correct any information directly. All fields are conveniently pre-populated, ensuring a seamless editing experience to maintain accuracy and relevance.

<img width="581" alt="Edit_post" src="https://github.com/fh255/solo-travel/assets/34744096/6cc5e63d-e292-4a99-9b13-6ed16fe38b98">


 #### Delete Post:
 When a user chooses to delete their post, they will need to confirm their action. A modal window will be displayed, providing the user with options to either Delete or Cancel the deletion process. This ensures that users can proceed with confidence when removing their posts, while also offering a safeguard against accidental deletions.

 <img width="457" alt="Delete Post" src="https://github.com/fh255/solo-travel/assets/34744096/4b115ada-5a10-4bcd-93e6-17f5e5d462c3">

#### Sign Up Page:
To engage with the site, users must sign up and log in. Unregistered users can access the Sign up page through various methods:

 - Via the link in the navigation bar.
 - Using the link provided on the Login page
Creating a new account is straightforward. Users need to provide the following information:

 - Username - must be unique
 - Email - needed
 - Password - must be entered twice
 
<img width="375" alt="Sign up" src="https://github.com/fh255/solo-travel/assets/34744096/cf4ed8e1-db2f-4504-9a46-3e3e8a1b2d17">

When all fields are completed and the user clicks on "Register," a new account is automatically created, and the user is redirected to the Home page.

#### Login Page
For full CRUD functionality on posts and comments, or the ability to like/unlike a post, a user is required to log in to the site. The Login page can be accessed via:

- **Start Your Journey** link, in the Hero section on the Home page
- The link in the navigation bar
- The link on the Register page
- Using the link provided on the Signup page
Provided that a user is registered on the site, the login process is very quick. The user needs to enter the following information:

 - Valid username
 - Correct password
 - The user is able to log in directly using their Gmail account.

<img width="334" alt="Login" src="https://github.com/fh255/solo-travel/assets/34744096/5247ed32-278a-46f3-9310-41ddbe29b801">

#### Logout Page:
The Logout page is accessible via the navbar link available when a user is logged in. Upon clicking "Logout," the user will be instantly logged out and redirected to the Home page.

<img width="435" alt="Logout" src="https://github.com/fh255/solo-travel/assets/34744096/49f2a4a8-9547-42eb-ace0-4d27daf3f0e2">

#### Django Admin Page:
A superuser account was created to manage the blog content on the site, granting administrative privileges. The Admin panel can be accessed by logging in at the /admin URL with the superuser credentials. From there, the superuser can delete specific posts, comments, or users, essential for maintaining the blog and ensuring unwanted content is removed.

<img width="440" alt="Admin" src="https://github.com/fh255/solo-travel/assets/34744096/ba624da1-7e58-44a3-a43a-f2585fe01818">

Additionally, the admin panel offers further functionality to the superuser, such as creating post drafts that can be published later.

#### System Messages:
Throughout the site, system or flash messages provide feedback to users upon completing certain actions. These messages appear at the top of the screen and automatically disappear after a short period.

<img width="582" alt="Massgae_alert" src="https://github.com/fh255/solo-travel/assets/34744096/0b711165-011a-40af-aa48-57d31e21603b">

#### Footer
The footer of our webpage showcases a tranquil, forested path, symbolizing our journey of discovery and growth. Connect with us on social media platforms including Facebook, YouTube, Instagram, and Twitter for solo travelers.

<img width="490" alt="footer-sm" src="https://github.com/fh255/solo-travel/assets/34744096/c730fbce-20c6-465a-aa2c-dec767e5b2fd">

## Design

### Colours

#### Background Colors:
 - #F9FAFC (General body background, .main-bg)
 - #f8f9fa (Masthead background, .add-post-card background, .card background)
 - #fff (card-header background, .signup-card background, .edit-post-card background)
 - #445261 (Masthead text background, .dark-bg)
 - #ffffff (login-card background, .signup-card background)
 - rgba(0, 0, 0, 0.5) (Hero section overlay)
 - rgba(0,0,0,0.1) (Shadow for .add-post-card, .img-thumbnail)
 - rgba(0,0,0,0.15) (Shadow for .login-card, .signup-card, .edit-post-card)
 - #23BBBB (Image flash background in .image-container)
#### Text Colors:
 - white (Masthead text color, .hero text, .footer text, .author text)
 - #007bff (Primary button text, .btn-signup text, .signup-card .link text)
 - #0056b3 (Primary button hover text)
 - #003f7f (Primary button border hover text)
 - #f6801f (New label background color)
 - #343a40 (Card h3 color, .signup-card h3 color, .edit-post-card h3 color)
 - #6c757d (Card p color, .signup-card p color, .card-text color)
 - #2C3E50 (.brand color)
 - #16A085 (.highlight color)
 - #E74C3C (.accent color, .footer color)
 - #445261 (.dark-bg background color)
 - rgba(205, 239, 240, 0.974) (Alert background color)
#### Border Colors:
 - #dee2e6 (Masthead bottom border, .add-post-card border, card borders, .signup-card border, .edit-post-card border)
 - #ccc (.login-card border)
 - #445261 (.alert border-color)

### Typography
Two types of fonts were used in this project:

 - General body font family: 'Roboto', sans-serif
 - Brand font family: 'Lato', sans-serif

### Entity-Relationship diagrams for DBMS:
The following Entity-Relationship Diagram (ERD) provides a visual representation of the database schema used in this project. The diagram illustrates the entities, their attributes, and the relationships between them. This helps in understanding the structure of the database and how different entities interact with each other.

#### User
 - Primary Key: id
 - Attributes:
   - username: The username of the user.
   - password: The password of the user.
   - email: The email address of the user.
 - Relationships:
   - Many-to-Many with Post: A user can like multiple posts, and a post can be liked by multiple users.
#### Post
 - Primary Key: id
 - Attributes:
   - title: The title of the post.
   - slug: A unique slug for the post.
   - author: The author of the post (Foreign Key referencing User).
   - featured_image: The featured image of the post.
   - excerpt: A short excerpt of the post.
   - updated_on: The date and time when the post was last updated.
   - content: The content of the post.
   - created_on: The date and time when the post was created.
   - status: The status of the post (e.g., Draft, Published).
 - Relationships:
   - One-to-Many with Comment: A post can have multiple comments.
   - One-to-Many with Image: A post can have multiple images.
   - Many-to-Many with User: A post can be liked by multiple users, and a user can like multiple posts.
#### Comment
 - Primary Key: id
 - Attributes:
   - post: The post to which the comment belongs (Foreign Key referencing Post).
   - name: The name of the commenter.
   - email: The email address of the commenter.
   - body: The body of the comment.
   - created_on: The date and time when the comment was created.
   - approved: Whether the comment is approved or not.
 - Relationships:
   - One-to-Many with Post: Each comment belongs to a specific post.
#### Image
 - Primary Key: id
 - Attributes:
   - post: The post to which the image belongs (Foreign Key referencing Post).
   - image: The image file.
   - caption: The caption for the image.
 - Relationships:
   - One-to-Many with Post: Each image belongs to a specific post.

<img width="755" alt="ER diagram" src="https://github.com/fh255/solo-travel/assets/34744096/e116fd1f-e59a-40a4-9809-4fcc10d3a670">

### Imagery

All current images on the site and uploaded blog posts is downloaded from [Unsplash:](https://unsplash.com/de) .

## Technologies Used
### Languages Used:

  - HTML5
  - CSS3
  - JavaScript
  - Python
### Frameworks and Libraries Used:

  - [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages.
  - [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images.
  - [Django:](https://www.djangoproject.com/) Main Python framework used in the development.
  - [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration.
  - [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
  - [dj_database_url:](https://pypi.org/project/dj-database-url/) Used to allow database urls to connect to the postgres database.
  - [Gunicorn:](https://gunicorn.org/) Green Unicorn, used as the Web Server to run Django on Heroku.
  - [psycopg2:](https://pypi.org/project/psycopg2/) Used PostgreSQL database adapter.
  - [Summernote:](https://github.com/summernote/django-summernote) To provide a WYSIWYG editor for customizing new blog content and add images.

### Software and Web Applications Used:

  - [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsive.
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.
  - [Font Awesome:](https://fontawesome.com/) Used throughout the site to add icons for aesthetic and UX purposes.
  - [Google Sheets:](https://docs.google.com/spreadsheets/u/0/) Used to design the tables.
  - [Git:](https://git-scm.com/) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  - [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git and to create the Kanban board used for this project.
  - [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
  - [HTML Validator:](https://validator.w3.org/) Check the code for HTML validation.
  - [Unsplash:](https://unsplash.com/photos/NtkCemIfaiU) All Images were downloaded from Unsplash.
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
  - [Writer:](https://writer.com/grammar-checker/) Free Grammar Check.

## Testing

### Browser Testing

I have tested that this application works using Macbook using the following browsers:
  - Safari 
  - Google 
  - Firefox

### Responsiveness

Chrome developer tool have been used to check the responsiveness.

  - I have tested that this application works on different screen sizes from iPhone SE (375px wide) and  large screens (1200px wide).
All tests confirmed that the application functions correctly across these browsers, devices, and screen sizes.

### Validator Testing

#### W3C Markup Validator:
The HTML on all pages of the project was validated using the W3C Markup Validator to ensure there were no syntax errors. To validate the HTML files, all Django template tags were removed manually, and the HTML code was copied and inserted into the base template.

Index page:

<img width="1214" alt="home_testing" src="https://github.com/fh255/solo-travel/assets/34744096/9a36c28c-f6a5-4c18-ba74-ed382acd99f2">

Add Post page:

<img width="1205" alt="add_post_test" src="https://github.com/fh255/solo-travel/assets/34744096/efce770b-1fe5-46ea-82f7-68455d0817b2">

 Edit Post page:
 
<img width="1208" alt="Edit Post test" src="https://github.com/fh255/solo-travel/assets/34744096/f9d90ded-0238-45d9-bc33-26d2cff4ecff">

#### W3C CSS Validator:
The W3C CSS Validator were used to validate the CSS to ensure there were no errors .
<img width="1205" alt="CSS" src="https://github.com/fh255/solo-travel/assets/34744096/4a1b2032-d5bf-4cfb-93b6-af49d3575a3f">

#### JSHint:
JSHint was used to validate the JavaScript code, and no errors were found.

<img width="991" alt="JS" src="https://github.com/fh255/solo-travel/assets/34744096/a34937d5-c83c-4f1c-961e-6a62019dd238">

#### PEP8 Online:
PEP8 Online linter (Python validator) The code passed without any errors on all files tested:

  - admin.py

<img width="998" alt="admin" src="https://github.com/fh255/solo-travel/assets/34744096/24cc151a-54d8-458d-8c5b-315d3217747b">

  - forms.py

<img width="964" alt="forms" src="https://github.com/fh255/solo-travel/assets/34744096/9ef356ce-eaa6-4bb7-a8bf-69493f96bcd5">

  - models.py

<img width="973" alt="models" src="https://github.com/fh255/solo-travel/assets/34744096/850ff9b3-5e66-4ba7-8c48-a154e577325c">

  - urls.py(blog)

<img width="988" alt="blog:urls" src="https://github.com/fh255/solo-travel/assets/34744096/43101c73-72fc-4f12-918d-60f11f6f6293">

  - views.py
<img width="970" alt="views" src="https://github.com/fh255/solo-travel/assets/34744096/924a4336-3954-4b8c-a99e-3c2b687a7363">

  - settings.py

<img width="1057" alt="settings" src="https://github.com/fh255/solo-travel/assets/34744096/5355b480-6eac-465d-9b2c-7bff91a55738">

  - manage.py

<img width="979" alt="manage" src="https://github.com/fh255/solo-travel/assets/34744096/3def5021-9301-44f1-9e78-67c4169cd2be">

#### Lighthouse:
I have verified that the chosen colors and fonts are easy to read and accessible by running them through Lighthouse in Chrome Developer Tools on the following pages:

Home page:

<img width="799" alt="lightHouse home" src="https://github.com/fh255/solo-travel/assets/34744096/3fc09e95-c251-4e6a-b000-9d261b08b8fa">

Post Detail page:

<img width="787" alt="Post details LH" src="https://github.com/fh255/solo-travel/assets/34744096/567dccfc-2187-4ee8-99b2-a792555d661b">

### Test Cases for Models:

#### User Model
 - Create a new user: Test creating a User object with valid data to ensure it is saved successfully in the database.
 - Ensure username is unique: Test that creating two User objects with the same username raises an IntegrityError.
 - Password is hashed: Test that the password is stored in a hashed format after creating and saving a User object.
 - Email format validation: Test that creating a User object with an invalid email raises a ValidationError.
<img width="543" alt="User Model Tests" src="https://github.com/fh255/solo-travel/assets/34744096/8d9b50df-4884-42fc-a9d6-5d781cb6e7d1">

#### Post Model
 - Create a new post: Test creating a Post object with valid data to ensure it is saved successfully in the database.
 - Ensure slug is unique: Test that creating two Post objects with the same slug raises an IntegrityError.
 - Associate post with user: Test that a Post object is correctly associated with a User object through the author field.
 - Ensure status is within choices: Test that creating a Post object with an invalid status raises a ValidationError.
 - Post likes functionality: Test that adding a User to a post's likes updates the likes count correctly.
<img width="586" alt="Post Model test" src="https://github.com/fh255/solo-travel/assets/34744096/c8544557-b611-415d-a355-02da57fb1900">

#### Comment Model
 - Create a new comment: Test creating a Comment object with valid data to ensure it is saved successfully in the database.
 - Associate comment with post: Test that a Comment object is correctly associated with a Post object.
 - Comment approval status: Test that the approval status of a Comment object is updated correctly.
<img width="586" alt="comment model test" src="https://github.com/fh255/solo-travel/assets/34744096/d7140e5a-aef9-43cc-87e9-e1cdfe88d431">

#### Image
 - Create a new image: Test creating an Image object with valid data to ensure it is saved successfully in the database.
 - Associate image with post: Test that an Image object is correctly associated with a Post object.
 - Caption can be blank: Test that creating an Image object with a blank caption is saved successfully in the database.
<img width="587" alt="Image model test" src="https://github.com/fh255/solo-travel/assets/34744096/c182a043-5873-4828-a2ff-af2b33edd68b">

### Solved bugs

  - Django test error -During testing of my Python files, I encountered and resolved errors in both views.py and settings.py.
  - Am I responsive? - I had to install the Google Chrome extension, Ignore X-Frame headers to generate mockup images using Am I responsive. Thanks to Code Institute’s Slack Channel, this was solved.
  - Throughout my coding journey, I encountered numerous challenges and bugs. Thanks to the constant availability of tutor assistance during my project, I was able to overcome them effectively.
  - After finishing my project, I deployed it on Heroku. Initially, I was unable to see my footer. With the help of my tutor Rebecca, I resolved the bug. I copied the image link from the cloud and pasted it into the CSS file's footer section.

### Known bugs

  - Currently no known bugs.

## Deployment

The application was successfully deployed to Heroku with the following steps:
 - Login to Heroku dashboard to view installed apps.
 - Click on **New** => **Create new app**.
 - Choose a unique name for your application and select your region.
 - Click on Create app.
 - Once your application is created, navigate to the Settings tab => click on Reveal Config Vars.
 - Copy the DATABASE_URL value to the clipboard.
 - In GitPod, create a new env.py file at the top level directory.
 - In the env.py file
    - Set environment variables: **os.environ["DATABASE_URL"]** = **"Paste in Heroku DATABASE_URL Link"**
    - Add in secret key: **os.environ[”SECRET_KEY"]** = **"Generate your own randomSecretKey”**
 - In Heroku, navigate to the Settings tab => click on Reveal Config Vars.
 - Add SECRET_KEY to Config Vars using the randomSecretKey you generated.
 - In the settings.py file:
    - Replace the insecure secret key with: **SECRET_KEY = os.environ.get("SECRET_KEY")**
    - Update to use the DATABASE_URL: import dj_database_url and DATABASES['default'] = dj_database_url.parse(os.environ.get("DATABASE_URL"))
- Save all files and run migrations: python3 manage.py migrate
- Log in to Cloudinary and navigate to the Cloudinary Dashboard.
- Copy your CLOUDINARY_URL API Environment Variable to the clipboard.
- In the env.py file
    - Add Cloudinary **URL: os.environ["CLOUDINARY_URL"] = "cloudinary://paste in your API Environment Variable"**
  - In Heroku, go to the Settings tab => click on Reveal Config Vars.
  - Add 'CLOUDINARY_URL' to Config Vars with the API Environment Variable value.
  - Add 'DISABLE_COLLECTSTATIC' = 1 to Heroku Config Vars (temporary, remove before final deployment).
  - In the settings.py file:
    - Add Cloudinary Libraries to installed apps (order matters): **'cloudinary_storage', 'django.contrib.staticfiles', 'cloudinary'**
    - Add the following code below STATIC_URL = ’/static/' to use Cloudinary to store media and static files:
      - STATICFILES_STORAGE = ’cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      - STATICFILES_DIRS = [os.path.join(BASE_DIR, ’static')]
      - STATIC_ROOT = os.path.join(BASE_DIR, ’staticfiles')
      - MEDIA_URL = '/media/'
      - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    - Link file to the templates directory in Heroku: **TEMPLATES_DIR = os.path.join(BASE_DIR, ’templates')**
    - Change the templates directory to: TEMPLATES_DIR: 'DIRS': [TEMPLATES_DIR],
    - Add Heroku Hostname to ALLOWED_HOSTS: ALLOWED_HOSTS = [”Your_Project_name.herokuapp.com”, ”localhost”]
  - Create 3 new folders on top level directory: media, static, templates
  - Create a Procfile on the top level directory
  - In the Procfile file:
    - Add the following code with your project name: web: gunicorn PROJ_NAME.wsgi
  - In the terminal: Add, Commit and Push.
  - In Heroku navigate to the Deploy tab => click on Deploy Branch.
  - When build process is finished click on Open App to visit the live site.
### Final Deployment steps
- Set DEBUG to False: In settings.py, set the DEBUG flag to False.
- Update X_FRAME_OPTIONS: Ensure this line exists in settings.py to make Summernote work in the deployed environment (for CORS security): X_FRAME_OPTIONS = 'SAMEORIGIN'.
- Push changes to GitHub: Push your updated files to GitHub.
- Remove DISABLE_COLLECTSTATIC: In the Heroku Config Vars for the application, delete the environment variable: DISABLE_COLLECTSTATIC.
- Deploy the application: On the Heroku dashboard, go to the Deploy tab for the application and click on "Deploy Branch".

## Credits

  - [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsive.
  - [Bootstrap documentation:](https://getbootstrap.com/docs/4.6/getting-started/introduction/) Bootstrap documentation used for styling and to build responsive web pages.
  - [Code Institute:](https://codeinstitute.net/) Walkthrough modules in Full Stack Frameworks.
  - [Code Institute Slack Community:](https://app.slack.com/) Slack community for troubleshooting and FAQ.
  - [Code Institute Tutor Support:](https://app.slack.com/) For help and support.
  - [Codemy Youtube:](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) Inspiration for creating A simple blog with Django.
  - [Django documentation:](https://docs.djangoproject.com/en/4.1/) Everything you need to know about Django.
  - [Stack Overflow:](https://stackoverflow.com) For troubleshooting and FAQ.
  - [Unsplash:](https://unsplash.com/photos/NtkCemIfaiU) All images were downloaded from Unplash.
  - [W3Schools:](https://www.w3schools.com) Online Web Tutorials.

### Acknowledgements

  - Special thanks to the tutor assistance and my mentor at Code Institute, Brian Macharia, for their invaluable support with code reviews, assistance, and feedback. It has been immensely appreciated!























