<h1> Community Task Board </h1>

Ireland’s community, voluntary and charity sector makes a very substantial contribution to society in general, There are almost 10,000 registered charities and a further 20,000+ organisations in Ireland’s wider nonprofit sector. This app is a simple tool that can be used by groups in this sector to aid in management and administration of tasks assigned to members of the group.

<!-- TOC -->

[Table of Contents](#table-of-contents)
- [About](#about)
- [Agile Metodology](#agile-metodology)
  - [Sprints](#sprints)
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
    - [Gotchas](#gotchas)
        - [database  v's one](#database--vs-one)
        - [sqlite3 deployed on 1st deployment](#sqlite3-deployed-on-1st-deployment)
    - [Configuration](#configuration)
                - [Back to top](#back-to-top)
    - [Credits](#credits)
                - [Back to top](#back-to-top)

<!-- /TOC -->

## About

This is a simple tool that can be used by groups in the CVC sector to aid in management and administration of tasks assigned to members of the group. 

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

   # firstname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    # surname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])

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
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Bootstrap v5.1.3](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Pagination, Navbar)
- [Canva](https://www.canva.com/) was used to create a background image
- [Cloudinary](https://cloudinary.com/) to store static files
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Font Awesome](https://fontawesome.com/) - Icons from Font Awesome were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/)
- [Render Platform](https://render.com) was used to deploy the project into live environment
- [jQuery](https://jquery.com) was used for drop-down exercises filters on smaller screens
- [Postgres](https://www.postgresql.org/) – deployed project on Render uses a Postgres database
- [Remove.bg](https://www.remove.bg/) was used to remove background on home page images & 404 page image
- [Summernote](https://summernote.org/) - editor used for exercise description field in Admin page
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/) - code editor used to write this project
- Validation:
  - [WC3 Validator](https://validator.w3.org/) was used to validate the html in the project
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) to validate the css in the project
  - [JShint](https://jshint.com/) for JavaScript quality
  - [PEP8](http://pep8online.com/) to check code against Python conventions
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for performance, accessibility, progressive web apps, SEO analysis of the project code
  - [Wave Validator](https://wave.webaim.org/) to evaluate accessibility

## Features

## Validation

## Testing
### Manual testing of user stories
### Automated testing
### Performing tests on various devices
### Browser compatibility

## Bugs

#### Delete User on_delete option
I intended that if a use was deleted all associated tasks should be re-assigned to admin user but I could nto get it to work, I can try get_sentinal_user example from django doc but leaving for moment as trying to reach MVP

Error image on C:\Users\User\OneDrive\CI\PP4\snips\delete-user-SET-failed

 class Task(models.Model):
    description = models.CharField(max_length=120, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=120, unique=True)
<code>    created_by = models.ForeignKey(User, on_delete=models.SET('admin'), related_name='tasks')</code>
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)   

#### 'django.db.utils.DataError'
 This error occurred during migration after I changed the max_length of slug field to less characters than the prepopulated field (ie 50 instead of 120) & despite correcting the max_length the smaller value of 50 persisted somewhere deep in the SQL & so I was unable to clear this error. I  found it necessary to go back about 4 migrations to be able to move forward. I learned a lot about migrations.  When time allows I would recreate this issue in a test environment & spend more time investigating the cause.
 
<code> django.db.utils.DataError: value too long for type character varying(50)</code>

#### Djanjo : Related Field got invalid lookup: icontains

I got the above FieldError when testing the search bar of the taskapp Admin panel.  It was caused by fact that I had 'created_by' field included in the search fields :

<code>search_fields = ['completed', 'description', 'status', 'created_by', 'category']</code>

 This 'created_by' field has a Foreign Key and that is what is throwing this error. I removed the created_by field from the search fields and that clearerd the error.  It seems the way around this is to use double underscore on the FK for example
<code>search_fields = ['created_by__User']</code>

 but time did not allow me to test this out.

 ### User & Profile [View this BUG which has been tracked in Siobhans CTB Project](https://github.com/siobhain/ctb/issues/20)
It took me a long time to get both User & Profile models to work together, I messed up the db when using a customform for the signup, In the heel of the hunt it was that I had save functions for Profile in both the formerly and model so was getting error 'user_id already exists'. Simply removing the save in the model solved the problem but it took me over 36 hours and thoughts of giving up on the Profile altogether to get to that stage. In hindsight I don't know why I did not cop this earlier, I went down rabbit hole after hole with database inconsistency, redoing models and finally retired, resigned to fact that I'd need to start afresh & use only default user model.  The penny droppped the following day after a few hours kip & on reading [stackoverflow](https://stackoverflow.com/questions/50929110/django-cannot-assign-profile-profile-objinect-none-profile-user-must-be) & the problem was solved in a few minutes. I know this pheomena is common and its not the 1st & probably not the last time it will happen to be but just wanted to log it here as it ate much precious time at crucial stage meaning styling of my frontend will have to be completed in a hurry.  Its probably a skill that comes with experience to know best when to give up & start afresh or keep trying to solve the issue - beating the dead horse senario.

![Sample Duplicate Key Error screenshot](https://user-images.githubusercontent.com/44432977/261859495-f8b76c56-e233-4a92-bbac-5f31c6c0abda.JPG)

![Sample integrity error Screenshot](https://user-images.githubusercontent.com/44432977/261859546-c6e47665-32a0-4f5d-891a-6f4f68b9ce70.JPG)

## Gotchas

### 2 database  v's one
I intended having 2 databases, the default Django `SQLite` for development and a `Postgres` instance for production, & use environment variables coupled with `if/else` statements in `settings.py` to distinguish which db was to be used.  However, since there were a couple of false starts & with the deadline looming I decided it was a prudent option for me in this position to reduce to the one database & use an ElephantSQL Postgres instance for both development and production.  I realise this would not be acceptable in the real db. as best pratice dictates development work would never be carried out on a production database.

### sqlite3 deployed on 1st deployment
Since I am using only one db for both development & production I should have added `db.sqlite3` to `.gitignore` prior to 1st gitpod commit (labelled "Empty Deployment"). I subsequently updated `.gitignore`, adding `*.sqlite3` to the list (after the empty deployment commit), thinking `sqlite` would be removed from repository after the next commit but it was persisent. As I learn more about the git process it seems I need to run `git rm`` to remove  'db.sqlite3'.  This is one case of "NINTH" that I will eventually get round to but perhaps not before final submission. I'm still learning about git and its power and don't want to loose the HEAD or mess up with deadline looming.



 <code>    created_by = models.ForeignKey(User, on_delete=models.SET('admin'), related_name='tasks') </code> 
 <code> slug max length 50 </code>

## Configuration

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.
##### Back to [top](#table-of-contents)


## Credits

[Sprint planning](https://codetree.com/guides/sprint-planning-github-issues)

[Revert Django Migrations](https://awstip.com/a-guide-to-reverting-migrations-in-django-c091bef62d34) 

[Django FKey on_delete options](https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4)

[Django Slug Tutorial](https://www.procoding.org/django-slug-tutorial-adding-slug-field-in-a-django-model/)

[Django Search Field Error](https://bugshare.io/exceptions/15/field-error-related-field-got-invalid-lookup-icontains)

[Custom Signup Form](https://stackoverflow.com/questions/70809519/how-do-i-customize-django-allauth-sign-up-forms-to-look-the-way-i-want)

##### Back to [top](#table-of-contents)

