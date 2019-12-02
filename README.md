# TDSB Homework Management System

<!-- > _Note:_ This document is intended to be relatively short. Be concise and precise. Assume the reader has no prior knowledge of your application and is non-technical.  -->

## Description
<!--  * Provide a high-level description of your application and it's value from an end-user's perspective
 * What is the problem you're trying to solve?
 * Is there any context required to understand **why** the application solves this problem? -->
 Our application allows Toronto School Board District students to manage all of their school work and to use various tools aimed to improve their school performance.

Students can create 'tasks' which are added to their calendars; tasks can range from any simple chore, to assignments and exams. Creating such tasks allows students to easily see and manage all of their various workload. Tasks have deadlines and are conveniently inserted into their Google Calendar so that it is organized and easily accessible.

Students can also keep track of their performance in multiple ways. For one, they can keep track of all of their grades by inputting their assignment and exam results into the app. Students can also set weights to every assignment and exam and see their current average grade for any course. Most importantly, students can get truly useful insight about their performance by using the 'Graphing' tool of our app, which showcases their grades and tasks completion over time for a course, which is a great way to gauge how well they're keeping up with the material and whether they should adjust the amount of effort they should be putting into said course.

There are many problems this app is trying to solve. For one, there is a lack of planning features available in TDSB's current system as the current system doesn't allow students to view and plan their work in a comprehensive and exhaustive manner, which leaves gaps in the planning process and can hinder students' success. Additionally, students currently have no way to easily see their performance and evaluate themselves, which TDSB considers vital for its students. Lastly, TDSB's current system relies entirely on a third party, so TDSB would like to have their own platform for more flexibility and control over the system, effectively allowing them to tailor the system for their students.

## Key Features
<!--  * Described the key features in the application that the user can access
 * Feel free to provide a breakdown or detail for each feature that is most appropriate for your application -->
 
 * Log In 
      - Upon entering the application, a user must log-in before they can access the features on the website.
    - Since the whole application is based on Google services such as Google Calendar and Google Classroom, they need to log-in with their Google account and then they are validated through OAuth.
    - Once they login, an account is setup for them in the database, and they are ready to use the application.
* Home Screen 
     - The first page is the home page which contains a general overview of their school work.
     - The navigation bar contains five hyperlinks to different sections of the application (Home, Courses, Tasks, Progress and Tools).
     - The drop-down menu on the right side is an account-specific menu which contains the option to log-out and also to view the current account settings.
     - There is a "Today" window which contains all the tasks and assignments that are due today.
     - There is a Feed window which contains all the recent activities of the user (i.e. addition of a new task, progress update, etc).
     - There is a Calendar window where the users can see all the tasks and assignments displayed according to their deadlines. 
* Courses
    - The user can see an overview of the courses that they are currently enrolled in this semester. Each course has specific information attached such as the instructor, the grades, and other metadata.
* Tasks
    - This page enables the user to add tasks, delete tasks and view all tasks that are both uncompleted or completed.
    - When they click add a task, they are taken to a pop-up modal where they can enter the title, select a due date with a date-picker, select a course, write a description and upload attachments for the task. The task is then added to the list of tasks.
    - There is a calendar window where they can see all the current tasks sorted by their deadlines in month/week/day or list format. All the tasks either added manually or retrieved from Google Calendar are displayed here.
    - Users can also search and filter through their tasks.
    - There is a window for them to conveniently see all the tasks that are due soon.
* Progress 
    - The application will allow the users to see their progress in a visual format.
    - For each course, the user can self-input the main assignments and the deadlines. For each assignment, they can input the current completion percentage if uncompleted or the grade if it is completed.
    - The result is a graph which shows the user's progress over time as well as the averages in all the courses obtained from the main assignments. 
* Tools
    - Users will be able to access a dictionary from the application to assist them with their homework.
    - Other tools can be added to the tools page if necessary. 
* Account Settings
    - The account settings displays the current configuration of the user's profile. They can edit their settings if applicable.

## Instructions
 
 * Users can log in the website by clicking the button on the login page where the app starts. It requires a pre-created Google account (We are using Google account because TDSB is using Google account). After login user will be directed to the homescreen. If users want to logout they can click the icon on the top right corner and click sign out. For user profile click the "Profile" above the "Sign out". Users can also use the Google account "tdsb301@gmail.com" with password "csc301csc301" to log in and experience the app, the account has a few courses enrolled in the google classroom for demonstration purposes.
 * On the homescreen users can view their tasks and assignments that due today and also recent activities. A calendar is shown in the right and users can switch the month using the two buttons on it. Activity information is shown on the calendar
 * Users can go to the course page by clicking "course" on the top navigation bar. Information about all enrolled courses will be displayed on the page. 
 * Users can go to the task page by clicking "Task" on the top navigation bar. The "Due soon" window on the right shows all upcoming tasks with a close deadline. Users can interact with the calendar on the left. By clicking "Sync with Google" button users can retrieve all tasks from their google calendar. In order to add more tasks, users can click the "Add Task" button on the top right corner of the calendar. Then they can input task information in the pop-up window then submit it to create a new task. All tasks can be displayed in both calendar and list views, users can choose the way they prefer by clicking the "month/list" switch button. To change the month use the pair of "<"">" button on the left. Also the "today" button is used to highlight all tasks due today. 
 * Users can go to the progress page by clicking "Progress" on the top navigation bar. The page shows their progress in assignments and tasks by using graphs. For showing the progress for a specific course, use the selector on the right. After a course is chosen, click the "Assignment" button for adding and editing assignments. For adding assignments, click "Add assignment" and input assignment information in the pop-up window then submit. Use the edit and delete button for each assignment to make changes. For showing the grade of each assignment, click "Grades" and input the grades.
 * Clicking "Tools" on the top navigation bar for additional tools like dictionaries.
 ## Development requirements
<!--  * If a developer were to set this up on their machine or a remote server, what are the technical requirements (e.g. OS, libraries, etc.)?
 * Briefly describe instructions for setting up and running the application (think a true README). -->
 The application is deployed on https://tdsb-app.herokuapp.com/. If the developer wants to run and revise the source code, then the following steps are necessary:  
### Technical Requirements
    - Languages: Python (3.0+) and JavaScript
    - Frameworks: Flask, Vue.js, Bootstrap
### Running the Application

    git clone https://github.com/csc301-fall-2019/team-project-tdsb-team-2.git`

* Front End
    - `cd front-end` to access front-end elements
    - `npm install` to install front-end dependencies
    - `npm run serve` to start the front-end on `http://localhost:8080/`
* Server
    - `cd server` to access the server folder
    - `pip install -r requirements.txt` to install back-end dependencies
    - `python -m venv .venv` to initialize a virtual machine
    - `export FLASK_APP=app.run.py` to set app.run.py as the entry point
    - `python -m flask run` to start the server

        


 ## Licenses

<!--  Keep this section as brief as possible. You may read this [GitHub article](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository) for a start.

 * What type of license will you apply to your codebase?
 * What effect does it have on the development and use of your codebase?
 * Why did you or your partner make this choice? -->
We decided to apply an MIT license to our codebase, which would most likely not affect the development of our code, but it does allow anyone to use or contribute to the code, so maybe we will see some pull-requests on our repository!
Unfortunately, our partner has become unresponsive, so we couldn't demo our app to them, let alone determine what license would best tailor their needs. However, it would be a shame for our efforts to go to waste, so we decided to simply make the code open-source and available for all since there is nothing proprietary in our code, but many cool and useful features. Another reason why the MIT license is a suitable option is its "as-is" approach, which wouldn't hold us accountable for any possible bugs or mistakes in our code.
