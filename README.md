# Solo Travel - Traveling Blog

This is my fourth milestone project with Code Institute. Solo Travel is a Django-based blog application designed for travel enthusiasts, especially those who love exploring the Worls.

The site allows users to share their travel stories, upload photos from their journeys, and interact with other posts by commenting, liking, and disliking the liked comments.

[View the live project here.](https://fishtales-mittnamnkenny.herokuapp.com/)

![Mockup](.jpg)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
  * [Project Goals:](#project-goals)
  * [Strategy:](#strategy)
  * [User stories:](#user-stories)
* [Features](#features)
  * [Existing Features](#existing-features)
    * [Navigation bar:](#navigation-bar)
    * [Home page:](#home-page)
    * [Add post page:](#add-post-page)
    * [Post detail page:](#post-detail-page)
    * [Post update page:](#post-update-page)
    * [Comment update page:](#comment-update-page)
    * [Register page:](#register-page)
    * [Login page:](#login-page)
    * [Logout page:](#logout-page)
    * [Django Admin page:](#django-admin-page)
    * [System messages:](#system-messages)
    * [Footer:](#footer)
    * [Additional features:](#additional-features)
    * [Meta Data:](#meta-data)
  * [Features to Implement in the future](#features-to-implement-in-the-future)
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Data Model](#data-model)
  * [Site map](#site-map)
  * [Colours](#colours)
  * [Typography](#typography)
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
  * [Automated Testing](#automated-testing)
    * [Jest:](#jest)
    * [Django testing tools:](#django-testing-tools)
  * [User Stories testing](#user-stories-testing)
    * [Testing which features support which stories](#testing-which-features-support-which-stories)
  * [Further Testing](#further-testing)
  * [Solved bugs](#solved-bugs)
  * [Known bugs](#known-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Project Goals:
The main objective of this project is to develop a travel blog that offers full CRUD functionality for registered users. This allows users to Create, Read, Update, and Delete their own blog posts and comments directly on the site, without any delays or intermediaries. Users will have complete control over their content, with all changes being immediately reflected on the site.

### Strategy:
An Agile methodology was employed to plan and execute this project. The project management was facilitated through a Kanban board on GitHub Projects, where tasks were organized into three main columns: To Do, In Progress, and Done. This structure ensured a clear visual representation of the project workflow and helped maintain focus on task progression and completion.

To achieve the project goals, the work was divided into 22 distinct parts, each representing a significant component or feature. These parts were tracked through the Kanban board, allowing for efficient prioritization and management of tasks.

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

<img width="593" alt="add_post" src="https://github.com/fh255/solo-travel/assets/34744096/29be7ba9-5846-4563-b186-35eebfb15870">

To submit a post, the following fields are required:
 - Title: A default post title is presented as the headline of the post. The user can choose to change this, but it must be unique.
 - Content: The user is presented with a "What You See Is What You Get" (WYSIWYG) editor and can use the included toolbar to upload photos and change the content.
 - Status: This field must be set to "Published." If not, the post will be saved as a draft.
   
When all fields are completed and the user clicks on "Post," their post will be automatically added to the list of posts, and the user will be redirected to the details page of their blog post.












