# Team 12, Deliverable 2 - Part 1

<!--  > _Note:_ This document is meant to be written during (or shortly after) your initial planning meeting.     
 > It does not really make sense for you to edit this document much (if at all) while working on the project - Instead, at the end of the planning phase, you can refer back to this document and decide which parts of your plan you are happy with and which parts you would like to change. -->


## Iteration 02

 * Start date: October 25th, 2019
 * End date: November 12th, 2019

## Process

We are developing a web application that is will allow students to keep track of the dates and deadlines for their homeworks and assignments, while allowing them to leverage information from their Google Classrooms and their personal Google Calendars. They will be able to log in with their TDSB (Gmail) accounts, create new tasks to do, and track their progress as they complete them.

#### Roles & responsibilities

<!-- Describe the different roles on the team and the responsibilities associated with each role.
 * Roles should reflect the structure of your team and be appropriate for your project. Not necessarily one role to one team member. -->
- **Front End**: Work on the VueJs application
    - Add different components for each page for each feature
    - Create Mockups for each page before actual design and implementation
    - Ensure proper functionality of front-end components
    - Connect to proper backend endpoints to make required calls

- **Back End**: Work on the Flask microservices
    - Set up the flask microservices
    - Add appropriate endpoints to ensure proper calling of the backend APIs
    - Add necessary functionality that the frontend can leverage
    - Set up the databases in MongoDB and connect to them via the microservices

- **Full Stack**: Combination of front and back end
    - Ensure that the front and back end calls and behaviour are working as expected

- **Project Manager**: Ensure that the correct communications are being made with the project partner
    - Send appropriate emails to the project partner
    - Set up meetings
    - Promote group discussions on matters
    - Ensure goals are being met
    - Breakdown road blocks

<!-- List each team member and:
 * A description of their role(s) and responsibilities including the components they'll work on and non-software related work
 * 3 technical strengths and weaknesses each (e.g. languages, frameworks, libraries, development methodologies, etc.) -->

 **Members:**

- **Anirudh Baskar**:
    - Role: Back-end (primarily API design)
    - Components:
        - Server-side and databases
        - Database Schemas
        - Features: Setting deadlines, Thesaurus, Notfication Systems
    - Technical strengths:
        - Languages
            - Python, Java, Javascript
        - Backend development and API design:
            - Flask and Node.js
        - Databases
            - MySQL and Firebase
        - Front end development
            - Vue.Js
    - Technical weaknesses:
        - UI design
        - React.JS
        - Software Testing

- **Gazi Jarin**:
    - Role: Full-Stack, Product Management
    - Components
        - Server-side and app design
        - Features: Chatbox, Calendar
        - Task Page
    - Technical strengths:
        - Languages
            - Python, Javascript, Java
        - Backend development:
            - Flask, Node.js
        - Front end development
            - Vue.js, HTML, CSS
        - Other
            - Google Services (Firebase, Dialogflow), AWS server deployment, UI/UX design
    - Technical weaknesses:
        - Software Testing
        - Databases
        - SQL

- **Raiyan Rahman**:
    - Role: Full Stack, Product Management
    - Components:
        - API Design and Implementation
        - UX Design
        - Front-End Design and Implementation
        - Features: Home screen, App Set up
    - Technical strengths:
        - Languages
            - Python, JavaScript, VueJs, Java
        - Backend development and API design:
            - Microservice design
            - Flask
        - Databases
            - Flask's SQLAlchemy, SQL
        - Front end development
            - VueJs
            - Wireframes and Mockups
            - UI/UX Design
    - Technical weaknesses:
        - Databases
        - Integration Testing
        - MongoDB

- **Anusha Fazal**:
    - Role: Full Stack
    - Components:
        - UX Design
        - Front-End Work
        - Back-End API Integration
        - Features: Homework submission, Graphing, Google Calendar/Classroom integration
    - Technical strengths:
        - Languages
            - HTML, CSS, Javascript, Python
        - Backend development and API design:
            - Flask and NodeJS
        - Databases
            - SQL, MongoDb (noSQL)
        - Front end development
            - Vue.Js
            - UI Design
    - Technical weaknesses:
        - Software testing
        - Databases

- **Alex Shang**:
    - Role: Full Stack
    - Components:
        - Serverside application
        - API design
        - Features: Register, Login verification
    - Technical strengths:
        - Languages
            - Python, Javascript, ReactJS, Java
        - Backend development and API design:
            - Flask
        - Databases
            - MongoDB
        - Front end development
            - HTML, CSS, ANT Design
    - Technical weaknesses:        
        - UI design
        - Software testing
        - SQL database

- **Mozammil Khan**:
    - Role: Full Stack Developer
    - Components:
        - Application Architecture and Implementation
        - Front-End Design and Implementation
    - Technical strengths:
        - Languages
            - Python, JavaScript, Java
        - Backend development and API design:
            - Node.js/Express.js
        - Databases
            - PostgresSQL, MongoDB
        - Front end development
            - React.js/Redux
            - Vanilla Javascript
    - Technical weaknesses:
        - UI Design

- **Michael Katilevsky**:
    - Role: Full Stack
    - Components:
        - UX Design
        - Front-End Implementation
        - Back-End API and Databases
        - Features: User Data, Grades Overview
    - Technical strengths:
        - Languages
            - Java, Python, TypeScript, JavaScript, HTML, CSS
        - Backend development and API design:
            - Express.js, Node.js, Flask
        - Databases
            - MongoDB, PostreSQL
        - Front end development
            - Angular, React.js, UI/UX Design
    - Technical weaknesses:
        - Software Testing


#### Team Rules

<!-- Describe your team's working culture. -->

Communications:
<!--  * What is the expected frequency? What methods/channels are appropriate?
 * If you have a partner project, what is your process (in detail) for communicating with your partner? -->
 * Communication between team members will be conducted in Facebook messenger in our Team's group chat. A discussion will take place with almost everyone present whenever any project-wide decision needed to be made. Communication frequency will be on a per-need basis. Whenever the whole group or a subset of the group decides to work on a certain task or feature, it is expected to get quick responses within a few minutes to ensure accurate and efficient exchange of information.

 * Project partner meetings were not as common anymore as we had been given the necessary information to continue with the development. We, however, did email the project partner with frequent updates such as after mockups were done for comments and review, and the update on beginning the actual implementation of the product. However, the project partner's responses were not frequent at all, even with the numerous attempts at emails, most often not getting replies. These communications were done mostly through emails, and in person meetings are being planned.

Meetings:
<!--  * How are people held accountable for attending meetings, completing action items? Is there a moderator or process? -->
* Team meetings were had mostly in the Facebook Messenger group due to the busy and hectic schedule of everyone in the team. We had short meetings every few days to report our progress, what we were going to tackle next, and brought up any issues if we were stuck on anything. This was expected of each member and the project trello was updated accordingly. The team's project manager is in charge of ensuring that everyone reported to the chat with moderate frequency. Once each task was completed, other team members in charge of similar parts of the overall application were tasked with conducting code reviews to ensure optimal and quality code.

Conflict Resolution:
<!--  * List at least three team scenarios/conflicts you discussed in lecture and how you decided you will resolve them. Indecisions? Non-responsive team members? Any other scenarios you can think of? -->
- Indecisions will be tackled with group discussions, outlining the pros and cons of certain choices. We will discuss through which discussions will yield the highest quality with the limited time we have.
- Non-responsiveness will be dealt by initially attempting to reach the teammate ourselves through their contact information. If that is not possible, we will try to allocate some of the tasks to other members who have completed their own work. If the absence is for too long of a period of time, it will be notified to the TA.
- If a team member is stuck because of a technical issue, they will immediately make it known what the issue is and why they are having it. Team members who are free will attempt to aid them if they have any knowledge regarding the issue, as soon as they are able to.


#### Events

<!-- Describe meetings (and other events) you are planning to have: -->
<!--  * When and where? Recurring or ad hoc? In-person or online?
 * What's the purpose of each meeting?
 * Other events could be coding sessions, code reviews, quick weekly sync meeting online, etc. -->
 * Meetings will take place in person for the first two initial planning meetings. They will take place on Friday, October 25th and November 1st. These will primarily be breaking down the product into components as well as the assignments of group members to certain tasks. The second meeting will be with an update on the tasks as well as confirming a front and backend design after reviewing and deciding on completed mockups.
 * Coding sessions and code reviews mainly be decided by the sub-groups before and after they finish features and tasks.
 * If members are entirely not able to make it, they are expected to notify the group within 12 hours and ask about the meetings to stay up-to-date.


#### Partner Meetings
<!-- You must have at least 2 meetings with your project partner - an initial planning meeting discussing the features you will build this iteration and a sprint demo meeting to review what you've done. Describe the meetings here: -->
<!-- * When and where will you meet?
What do you intend to discuss(**note you will have meeting minutes in the review document**)? -->
- The first partner meeting will take place after the mockups for the front end are complete so we may understand what exactly the vision is for the application. We will also have the partner pick a design that they prefer and think will suit their purpose the best. This will go hand in hand with the planning we will do about the features and other details such as the priority of the tasks, so we may ascertain which needs to be completed first. This will allow us to create a timeline for our sprints.

- The second partner meeting will include review and validation to ensure that the team is headed in the right direction. We will have the initial demo of what we implemented so far. This will also give the project partner an idea of where the product will be headed and what the end product might look like.

#### Artifacts

<!-- List/describe the artifacts you will produce in order to organize your team.        -->
- We will be following the traditional agile methodology using a trello board as our primary task board. Here, we will update tasks that are added as needing to be done, those in development, those that are being tested, as well as the tasks we have completed.
- Overview of Tasks can be found on Trello: https://trello.com/invite/b/68RfNTky/7bf7c72f2b6a52990927cfb8dc48d44c/term-project

- We have divided our group into developers that specialize in back-end, front-end, and databases according to our strengths and previous experience. Although we will primarily stick to these parts of the project, we will definitely be more fluid with these roles and move around to get tasks done and help teammates when they need it.

- Teammates will discuss with everyone and pick tasks to complete by assigning it to themselves on the trello board. Tasks will be prioritized with regards to how crucial they are to getting the base application and the MVP running and functioning properly to meet the basic requirements set forth by TDSB.

- Our primary source of communication for discussing matters about the project and tasks will be through our facebook messenger group. We answer questions, discuss tasks, and schedule meetings through it. Our group also has scheduling features and reminders which will prove to be useful in ensuring we get tasks done on time.



#### Deployment and Github Workflow

<!-- Describe your Git / GitHub workflow. Essentially, we want to understand how your team members shares a codebase, avoid conflicts and deploys the application.

 * Be concise, yet precise. For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Describe your overall deployment process from writing code to viewing a live application
 * What deployment tool(s) are you using and why
 * Don't forget to **explain why** you chose this workflow or particular aspects of it! -->

We will have the basic application set up initially on the master branch. Once that is complete, each task and feature will have its own separate branch to ensure that conflicts are at a minimum, promoting modularity. This will ensure that if the code from any feature does cause problems, we will easily able to revert changes and quickly fix problems. Each branch will be named by the feature that will be implemented in it. This will allow easy identification of what the use of the branch is.

Once features are done, we will have pull requests that will be followed by code reviews of the code written in the branch with the pull request. If the code is seen to be good with no issues, it will then be merged to the master branch.

Once a working prototype is functioning with the minimum number of high priority requested features, we will have a discussion with the project partners about preferred cloud providers, whether or not they already have resources, and whether they would give us options to pay for specific cloud providers; we would then host it to that preferred place. A likely solution could be hosting it using Google Cloud as we are provided with free credits by the CSC301 class and opening an account with the Google Cloud platform provides $300 of free credits. We would utilize Docker in the hosting of the application. We would build our app to host it. Once our build has been finished, we would create a docker image for it and test out to see if it can be run locally. Once this verification is complete, we will push a tag of our docker image to the Google Container Registry which is a built-in registry support for images in the Google Cloud. Once this is done, we will then deploy our image to a Google Cloud GCE (Google Compute Engine) VM.




## Product

#### Goals and tasks
<!--
 * Describe your goals for this iteration and the tasks that you will have to complete in order to achieve these goals.
 * Order the items from most to least important.
 * Feel free (but not obligated) to specify some/all tasks as user stories.
 -->

Overview of Tasks can be found on Trello: https://trello.com/invite/b/68RfNTky/7bf7c72f2b6a52990927cfb8dc48d44c/term-project

For this iteration, we aim to get most of the main pages for the website done as well as set up a preliminary server and database for user registration.

Concisely, for the front-end, we have the task of replicating the mock-ups for web-pages such as the home-screen, log-in, addTask screen, and the calendar screen. For the back-end, we have the task of proper user registration from the log-in page and storing vital information about the users in the database.

1. **Server and Database Set-Up (Priority: High)**
    Assigned to Anirudh Baskar, Alex Shang and Samin Khan
    * Initialize Flask app to run a server on localhost (for now)
    * Initialize an instance of MondoDB with the necessary URI and create static methods to control data (insert and modify)



2. **Basic Front-End Set-Up (Priority: High)**
    Assigned to Raiyan Rahman
    * Integrate basic Vue.js template to include the main window, navigation bar, account menu and background.

3. **Home-Screen (Priority: High)**
    Assigned to Raiyan Rahman, Gazi Jarin, Anusha Fazal
    * Replicate basic mock-up of home screen to create a static webpage.
    * Features include: static toolbar (Home, Profile, ourses, Tasks, Gallery, Tools), overview window to store recent activity, side calendar and task-list.

4. **Log-in and Registration (Priority: High)**
    Assigned to Anirudh Baskar, Alex Shang, Samin Khan, and Michael Katilevsky
    * Replicate basic mock-up of log-in to create a static webpage.
    * Features include: form input (name, password) and the ability to log-in with a Google account.
    * Create APIs to insert, modify and update student information such as courses, name, and user id.

5. **AddTask Screen (Priority: Medium)**
    Assigned to Gazi Jarin
    * Replicate basic mock-up of addTask to create a static modal using Bootstrap elements (b-button and b-modal) in the Tasks page.
    * Features include: form input (title), date and time picker, description text editor box, and attachment box.

6. **Calendar Integration (Priority: Medium)**
    Assigned to Anusha Fazal
    * Display Calendar in the Tasks page where the tasks will appear as they are added in.
    * Get tasks from user's Google Calendar via the Google API and display it on the Calendar in the Tasks page.

7. **Graphing Software (Priority: Low)**
    Assigned to Gazi Jarin, Anusha Fazal
    * Display the static webpage of graphing software under the Tools/Progress section.
    * The user will be able to log in completed tasks related to an assignment in a course
    * The user will be able to see their progress in percentage of each assignment yet to be finished/due
    * The user will see a list of all completed projects under each course
    * The user will see a graphical demonstration of their progress: # of completions over time.

8. **Dictionary/Thesaurus Integration (Priority: Low)**
    Assigned to Alex Shang, Gazi Jarin
    * Display a dictionary window under the Tools section.
    * Fetch data from an open-source dictionary API to display results.
    * User will be able to type in a word in a form input, and get the corresponding meaning, synonyms and word usage.





#### Artifacts

<!-- List/describe the artifacts you will produce in order to present your project idea.

 * Artifacts can be text, code, images, videos, interactive mock-ups and/or any other useful artifact you can think of.
 * Make sure to explain the purpose of each artifact (i.e. Why is it on your to-do list? Why is it useful for your team?)
 * Be concise, yet precise.         
   For example: "Build the website" is not precise at all, but "Build a static home page and upload it somewhere, so that it is publicly accessible" is much clearer. -->

1. Mock-Ups (Done)
   Purpose: Ensure the right kind of user experience and usability when it comes to interacting with the web application. This gives us a preliminary plan on what to base the actual front-end on.
    * Home Screen
        * Header: Title (TDSB App)
        * Navigation Bar: Hyperlinks to Home, Courses, Tasks, Tools
        * Profile Drop-Down: Hyperlinks to Logout, Account Settings
        * Activity Section: Recent updates on adding tasks, update on completing or starting new assignments, etc.
        * Calendar Section: Displays tasks, assignments and deadlines
        * Deadline Section: Displays upcoming due dates for all courses and the corresponding progress

    ![](https://i.imgur.com/LnOHYYP.png)


    * Log-in
        * Header: Title (TDSB App)
        * Form Input: Username and Password
        * Links: Forgot Password, sign in with Google

    ![](https://i.imgur.com/QazGsPj.jpg)

    * AddTask
        * Header: Title (TDSB App)
        * Navigation Bar: Hyperlinks to Home, Courses, Tasks, Tools
        * Profile Drop-Down: Hyperlinks to Logout, Account Settings
        * Form Input: Title
        * Options Menu: Courses
        * Date and Time Picker
        * Text Editor: Description Box
        * Upload Attachment

    ![](https://i.imgur.com/MxdG0JM.png)

    * Account Settings
        * Header: Title (TDSB App)
        * Navigation Bar: Hyperlinks to Home, Courses, Tasks, Tools
        * Profile Drop-Down: Hyperlinks to Logout, Account Settings
        * Profile Avatar
        * Edit Container: Name, Username, Language, Timezone

    ![](https://i.imgur.com/Q8HsnhW.png)

    * Calendar Screen
        * Header: Title (TDSB App)
        * Navigation Bar: Hyperlinks to Home, Courses, Tasks, Tools
        * Profile Drop-Down: Hyperlinks to Logout, Account Settings
        * Calendar: Display current month, scheduled tasks, deadlines

    ![](https://i.imgur.com/T2bGH4e.png)


    * Graphing Software    
        * Header: Title (TDSB App)
        * Navigation Bar: Hyperlinks to Home, Courses, Tasks, Tools
        * Profile Drop-Down: Hyperlinks to Logout, Account Settings
        * In-Progress Window: Displays the current assignments in progress and the percentage of completion
        * Completed Window: Displays the courses and the projects completed for each
        * Graph: Displays a graph showing the # of completed assignments over time

    ![](https://i.imgur.com/NhyocxP.png)



2. Front-end Prototype
    Purpose: Ensure final touches to the web application design and have a preliminary set-up so that the user can actually use the application to get a feel of what the end product is.
    * Static Home Screen with Mock Data
    * Log-in Registration to Static Home Page
    * Static AddTask
    * Static Calendar Screen with Mock Data

3. Code
    Purpose: Ensure the proper foundation for the back-end with MongoDB and Google Classroom API and Google Calendar API.
    * Database set-up
        * Create database schemas modelling the student accounts, their events, and calendars to properly store them.
    * Google API Integration
        * Allow the use of Google Classrooms and Google Calendars for students to utilize for their task tracking.
