<h1> Community Task Board </h1>

Ireland’s community, voluntary and charity sector makes a very substantial contribution to society in general. This app is a simple tool that can be used by groups in this sector to aid in management and administration of tasks assigned to voluntary members of the group.

<!-- TOC -->

- [About](#about)
- [Agile Metodology](#agile-metodology)
    - [Sprints](#sprints)
    - [<u>Milestone Sprints screenshot at 3rd Sprint</u>](#umilestone-sprints-screenshot-at-3rd-sprintu)
    - [US & EPICS](#us--epics)
    - [Velocity & Story Points](#velocity--story-points)
- [User Experience Design UXD](#user-experience-design-uxd)
    - [Stategy](#stategy)
        - [Owner Goals](#owner-goals)
        - [User Goals](#user-goals)
        - [Target Audience](#target-audience)
        - [User Requirements and Expectations](#user-requirements-and-expectations)
        - [Scope / User Stories#user-stories](#scope--user-storiesuser-stories)
    - [Structure](#structure)
        - [Database](#database)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  
        - [Skeleton](#skeleton)
            - [Wireframes](#wireframes)
            - [Pages](#pages)
        - [Surface Design](#surface-design)
            - [Colours](#colours)
            - [Fonts](#fonts)
                - [Back to top](#back-to-top)
    - [Technologies Used](#technologies-used)
        - [Languages & Frameworks](#languages--frameworks)
        - [Libraries & Tools](#libraries--tools)
    - [Features](#features)
    - [Validation](#validation)
    - [Testing](#testing)
        - [Manual testing of user stories](#manual-testing-of-user-stories)
        - [Automated testing](#automated-testing)
        - [Performing tests on various devices](#performing-tests-on-various-devices)
        - [Browser compatibility](#browser-compatibility)
    - [Bugs](#bugs)
            - [Delete User on_delete option](#delete-user-on_delete-option)
            - ['django.db.utils.DataError'](#djangodbutilsdataerror)
            - [Djanjo : Related Field got invalid lookup: icontains](#djanjo--related-field-got-invalid-lookup-icontains)
        - [User & Profile View this BUG which has been tracked in Siobhans CTB Project](#user--profile-view-this-bug-which-has-been-tracked-in-siobhans-ctb-project)
        - [Email](#email)
    - [Gotchas](#gotchas)
        - [Two Database v's one](#two-database-vs-one)
        - [sqlite3 deployed on 1st/Empty Deployment](#sqlite3-deployed-on-1stempty-deployment)
        - [Move Task.created_by to admin if user instance is deleted](#move-taskcreated_by-to-admin-if-user-instance-is-deleted)
        - [Removing Change Email option for authenticated user](#removing-change-email-option-for-authenticated-user)
        - [@login_required Decorator on Class Based View : function object has no attribute as_view](#login_required-decorator-on-class-based-view--function-object-has-no-attribute-as_view)
        - [Defensive programming on edit task](#defensive-programming-on-edit-task)
    - [Configuration](#configuration)
                - [Back to top](#back-to-top)
    - [Credits](#credits)
                - [Back to top](#back-to-top)




## About

This is a simple tool that can be used by groups in the CVC sector to aid in management and administration of tasks assigned to members of the group. I have been involved in voluntary greoup and committes for many years and see a problem with managing volunteer tasks between monthly meetings.  I need a solution that would keep the group abreast of development on tasks and up to date on progress in that time between monthly meetings.  This app invites Guests to have a look at the kind of Tasks the group in involved with ^ register if they feel they would like to help.  It is a tool that can aid in the magagement and admin, it can never replace monthly meetings nor is it menat to.  Over time there can be severla years of takss build up in the database and new committees can look back and find out who had area of expertise in certain areas. The are 4 main data presentations 

### Guest visiting the site Recently Completed List
Guests will be presented with 10 of the most recently modified & completed (done) Tasks, Date Description & Category

### Members visiting the site Shared Task Board
Members will be presented with the most important board, the Shared Task board for the group, this is sorted by date reverse createdon, firstname and surename of user who created the Task, completed is False & Task is publihsed by the Admin

### Members viewing their own Todo Board
Again sorted by reverse date, the user can see all their own tasks which are not completed, its lists Draft and Live, & Draft Tasks are hightlighted in grey color

### Members viewing Full Task Board
All tasks both completed and not completed (but not Draft) since the databse started


Also unfortunatley Pagination not yet implemented, sorry

## Agile Metodology

Find my GitHub Project called  `@siobhain's CTB project`  [here](https://github.com/users/siobhain/projects/9)

Initally I found using GitHub to create user stories, plan sprints etc challenging, workarounds were needed such as creating US (user story) & EPIC templates from Github Issues. It seemed more trouble that it was worth for a one person project.  I believed in the Agile methodology but trying to mould GitHub to convey adopting this methodology for PP4 was frustrating.  In addition while the Agile methodology sounds good in theory & I so wanted to adhere to it, having the discipline to follow it under a deadline challenged me on manys the occasion. As PP4 progressed, my attempts with using GitHub Project improved -  as with anything the more you play around with it the better you understand! Below I describe my PP4 journey & adapting GitHub to track progress in what I hope is an Agile manner.

### Sprints
I started by using Project Milestones to determine sprint but found it somewhat lacking especially as I could not find a way to display milestone on kanban boards.  Sometime into the PP4, during time of 2nd Sprint, I created an iteration field to determine sprint.  I setup 4 sprints of one week duration each.  Hence to anyone but myself the [Roadmap View](https://github.com/users/siobhain/projects/9/views/10) must look very confusing having both milestone & iteration determining Sprints.  In future I would just use Iterations but I had started with Milestones & well you learn as you go so I was able to use both in a kind of a "In Theory" (Iterations) & "In Reality" (Milestones) that probably only has meaning to myself.  Also during the PP4 I did find a way to display milestones in the US on the Kanban so it was useful to me but perhaps not to the casual observer. It may help the reader to know that the Milestone sprints are named as First Sprint, 2nd Sprint, 3rd Sprint... & the Iteration sprints are labelled Sprint 1, Sprint 2, Sprint 3 etc.  Of coarse I could have tidied it up and removed the milestones but wanted to show the learning process.

### <u>Milestone Sprints screenshot at 3rd Sprint</u>

![Milestone Sprints screenshot at 3rd Sprint](https://user-images.githubusercontent.com/44432977/261867099-c6ee0f81-de80-4585-b710-4495cf7d6cd7.JPG)

### US & EPICS
I created Issue templates for both Epics and User Stories (title prefixed with US) with each individual instance automatically assigned an Issue number,  hence Epic numbers are not in chronological order as would normally be expected.  I tried as best & where possible to automatically close/resolve US's & EPIC's via commit message keywords. However when a commit message solved more than one US I found that not all issues were automatically set to closed and moved to the Done column and some had to be manually changed. Its a learning process & no doubt given time and experience with GitHub I will come to an acceptable & consisent way of using it for planning and tracking work. Each US was given a labed according to Mo

### Velocity & Story Points
As this was a one person project team velocity did not come into play. There are no built in story points so I tried my best,  when &where possible to give story points to US in the form of these color coded size options : X-Large, Large, Medium, Small, Tiny

-  ![size options](https://user-images.githubusercontent.com/44432977/261864807-1118bb34-3d1d-47f6-8fd4-eb4f89f03ded.png)


## User Experience Design (UXD)
### Stategy

As much as practical I followed the User Centered Design (UCD) process to ensure the app is intuitive and easy to use.
#### Owner Goals
- Provide an online solution for community groups to view list of tasks whether already done or to be completed
- Create a visually appealing site
- Provide a fully responsive application with straightforward navigation

#### User Goals
- Be able to enter a task
- Be able to change status on their task 
- View the groups list of tasks

#### Target Audience
- Community groups who want to be more organised with their tasks
- Community groups who want to keep non members informed of work being done by the group
- An online log of all tasks

#### User Requirements and Expectations

- Straightforward navigation
- Easy to use
- A responsive application that allows the user to create a task on any device
- Visually appealing design for any screen size
- Links and functions that work as expected

#### Scope / User Stories(#user-stories)

### Structure
#### Database

* **Models**

Models created for this application:

1. **Profile Model**

A user profile model to hold firstname, surname, mobile & a default gate code which in future version will be set by a security system via API

| **PK** | **id** (unique) | Type | Notes |
| --- | --- | --- | --- |
| **FK** | user | OneToOne | FK to **User** model, cascade ondelete |
|  | firstname | CharField | max_length=15, Used to personalise UX|
|  | surname | CharField | max_length=15, Used in Task Board for better UX
|  | mobile_prefix | CharField | choices 083, 085, 086, 087, possible prefeix in republic of Ireland|
|  | mobile_number | CharField| 7 digits, regular expression enforces this |
|  | gate_code | CharField | default='1234', to be used in future as unique code to gain access|


2. **Task Model**

Task model for holding details of each task, The last 3 fields slug, likes & attachedimage are for future use as their functionality did not get implemented in this first version, It is also possible I made a rookey mistake in making the description field unique as this may cause a problem as databse fills up and some tasks may be repeated, in hindsight I should have made description and createdon as the UNIQUE combination.

| **PK** | **id** (unique) | Type | Notes |
| --- | --- | --- | --- |
| **FK** | created_by | ForeignKey | FK to **User** model |
|  | description | TextField | 120 characters max, UNIQUE, May need to change UNIQUE in future|
|  | slug | SlugField | 120 characters max, UNIQUE, for future use|
|  | created_on | DateTimeField | created timestamp |
!  | modified_on | DateTimeField | timestamp when there are any changes|
|  | category | IntegerField | choices Manual, Admin, Campaign, Other|
|  | completed | BooleanField | default is false|
|  | status | IntegerField | choices Draft or Live, default Draft|
|  | slug | SlugField | 120 characters max, UNIQUE, for future use|
|  | likes | ManyToMany | M2M to AllAuth **User** model, for future use |
|  | attached_image | CloudinaryField | default placeholder, for future use |



### Skeleton
#### Wireframes
#### Pages

### Surface Design
#### Colours
#### Fonts

##### Back to [top](#table-of-contents)

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python 3.10.2
- Django 3.2


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was used to create the multi-device mock-ups
- [Bootstrap v5.1.3](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Pagination, Navbar)
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Font Awesome](https://fontawesome.com/) - Icons from Font Awesome were used throughout the site

- [Git](https://git-scm.com/) for version control in GitPod to push the code to GitHub
- [GitHub](https://github.com/) a remote repository to store project code
- [GitHub Projects](https://github.com/users/siobhain/projects/9) To track & manage the PP4 in Agile manner

- [Google Fonts](https://fonts.google.com/)
- [Summernote](https://summernote.org/) - installed even though it6 is not used in this first version


## Features

### Pages

The website is comprised 8 pages which are extended from a base template.

1. **Home Page Guest or Member** 

 The Home page is the landing page when guest users arrive at the site for the first time, It is a list of recently completed tasks or if they are already logged in they are presented with the Shared Group Task board. As guest they are invited to register, as member they can chose to add new, view their own todo board, view the full board of all Tasks, or signout

2. **Sing Up Page**

The user can create an account for themselves by entering their chosen username, firstname, surname, mobile number & password

3. **Sign In Page**

The registered user can log in with their username and password. 


4. **Sign Out Page**

When the user wants to finish their session and logout, they can do so from the nav menu. When a user clicks the logout button they're met with a page asking them to confirm they want to log out. 

5. **Add New Task**
New tasks all in Draft status until changed by admin to Live status, then all members can see the Task, When in Draft status only createdby user and admin see the Task
6. **Update Task**
7. **Delete Task button**
8. **View my own ToDo Board**
9. **View all the Task (Full) Board**


## Validation

Please see [TESTME.md](TESTME.md) for details of tests performed
- - -


## Deployment 

You will need an account on Heroku and setup a databse instance on somewhere like elephant sql, Create an app instance on Heroku and deploy the CBT repo from Github, There are some envuironment variables to setup to connect to your databse instance, for cloudinary also even thought it is not used in this first verison:


##### Back to [top](#table-of-contents)


## Credits

from (https://www.w3schools.com/bootstrap5/bootstrap_tooltip)

[Sprint planning](https://codetree.com/guides/sprint-planning-github-issues)

[Revert Django Migrations](https://awstip.com/a-guide-to-reverting-migrations-in-django-c091bef62d34) 

[Django FKey on_delete options](https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4)

[Django Slug Tutorial](https://www.procoding.org/django-slug-tutorial-adding-slug-field-in-a-django-model/)

[Django Search Field Error](https://bugshare.io/exceptions/15/field-error-related-field-got-invalid-lookup-icontains)

[Custom Signup Form](https://stackoverflow.com/questions/70809519/how-do-i-customize-django-allauth-sign-up-forms-to-look-the-way-i-want)

[Form : multi line input field](https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets#google_vignette)

##### Back to [top](#table-of-contents)

