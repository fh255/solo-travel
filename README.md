# Solo Travel - Traveling Blog

This is my fourth milestone project with Code Institute. Solo Travel is a Django-based blog application designed for travel enthusiasts, especially those who love exploring Switzerland.

The site allows users to share their travel stories, upload photos from their journeys, and interact with other posts by commenting, liking, and disliking the liked comments.

[View the live project here.](https://fishtales-mittnamnkenny.herokuapp.com/)

![Mockup](documentation/amiresponsive.jpg)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
  * [Project Goals:](#project-goals)
  * [Strategy:](#strategy)
  * [User stories:](#user-stories)
* [Features](#features)
  * [Existing Features](#existing-features)
    * [Navigation bar:](#navigation-bar)
    * [Home page:](#home-page)
    * [Blog page:](#blog-page)
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
   

