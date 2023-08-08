<h1> Community Task Board </h1>

Ireland’s community, voluntary and charity sector makes a very substantial contribution to society in general. There are almost 10,000 registered charities and a further 20,000+ organisations in Ireland’s wider nonprofit sector.

This is a simple tool that can be used by groups in the CVC sector to aid in management and administration of tasks assigned to members of the group.

## Table of Contents
  - [About](#about)
  - [Agile Methodology](#agile)
  - [User Experience Design](#user-experience)
    - [Stategy](#strategy)
        - [Owner Goals](#site-owner-goals)
        - [User Goals](#user-goals)
    - [Scope / User Stories](#user-stories)
    - [Structure](#structure)
      - [Database](#database)
    - [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
      - [Website pages](#website-pages)
    - [Surface Design](#design)
        - [Colours](#colours)
        - [Fonts](#fonts)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing of user stories](#manual-testing-of-user-stories)
    - [Automated testing](#automated-testing)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Configuration](#configuration)
    - [Google emails](#google-emails)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

  ### About

This is a simple tool that can be used by groups in the CVC sector to aid in management and administration of tasks assigned to members of the group.  There is no builtin notion of story points so I created custom labels ex 2Points, 4Points, 8Points. I used Project Milestones to determine sprint. As this was a one person project team velocity did not come into play.

### Agile Metodology
Using github to plan sprints is challenging, some workarounds were needed such as using Issues as User Stories. 

## User Experience Design (UXD)

As much as practical I followed the User Centered Design (UCD) process to ensure this app is intuitive and easy to use.

### User Goals

- Be able to enter a task
- Be able to change status on their task 
- View the groups list of tasks

### Site Owner Goals

- Provide an online solution for community groups to view list of tasks whether already done or to be completed
- Create a visually appealing site
- Provide a fully responsive application with straightforward navigation




### Target Audience
- Community groups who want to be more organised with their tasks
- Community groups who want to keep non members informed of work being done by the group
- An online log of all tasks 

### User Requirements and Expectations

- Straightforward navigation
- Easy to use
- A responsive application that allows the user to create a task on any device
- Visually appealing design for any screen size
- Links and functions that work as expected

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


### Configuration

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.
##### Back to [top](#table-of-contents)


### Credits

[Sprint planning](https://codetree.com/guides/sprint-planning-github-issues) Using github to plan sprints is challenging, some aorkarounds were needed such as using 




##### Back to [top](#table-of-contents)

