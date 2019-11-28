# Team 12 - TDSB Application

<!-- > _Note:_ This document is intended to be relatively short. Be concise and precise. Assume the reader has no prior knowledge of your application and is non-technical.  -->

## Description 
<!--  * Provide a high-level description of your application and its value from an end-user's perspective
 * What is the problem you're trying to solve?
 * Is there any context required to understand **why** the application solves this problem? -->
Our application allows Toronto School Board District students to manage all of their school work and to use various tools aimed to improve their school performance.

Students can create 'tasks' which are added to their calendars; tasks can range from any simple chore, to assignments and exams. Creating such tasks allows students to easily see and manage all of their various workload. Tasks have deadlines and are conveniently inserted into their Google Calendar so that it is organized and easily accessible.

Students can also keep track of their performance in multiple ways. For one, they can keep track of all of their grades by inputting their assignment and exam results into the app. Students can also set weights to every assignment and exam and see their current average grade for any course. Most importantly, students can get truly useful insight about their performance by using the 'Graphing' tool of our app, which showcases their grades and tasks completion over time for a course, which is a great way to gauge how well they're keeping up with the material and whether they should adjust the amount of effort they should be putting into said course.

There are many problems this app is trying to solve. For one, there is a lack of planning features available in TDSB's current system as the current system doesn't allow students to view and plan their work in a comprehensive and exhaustive manner, which leaves gaps in the planning process and can hinder students' success. Additionally, students currently have no way to easily see their performance and evaluate themselves, which TDSB considers vital for its students. Lastly, TDSB's current system relies entirely on a third party, so TDSB would like to have their own platform for more flexibility and control over the system, effectively allowing them to tailor the system for their students.


## Key Features
<!--  * Described the key features in the application that the user can access
 * Feel free to provide a breakdown or detail for each feature that is most appropriate for your application -->
 
 * **Log In** [User authentication, database structure and front-end completed]
A user must login first before they can access the features on the website.
    * They login with their Google Account and are validated through OAuth.
    * Once they login, an account is setup for them for the application.
    
 * **Home Screen** [Front-end completed]
 Users can see a general overview of their school work on the home page. 
    * There is a section where users can see all the tasks they have due today.
    * There is also a feed section where they can see recent updates to their courses.
    * A small  monthly calendar is there for them to see dates when tasks are due.
    * Users can also view a section for a summary of their tasks due this week and how far along completed they are.
    
 * **Tasks** [Front-end completed]
 For this feature, users can view all their tasks. They can also add, modify or delete their tasks.
     * They can view their tasks in both a calendar (month, week, day) or list format.
     * When they click add a task, they can enter the title, select a due date with a date-picker, select a course, write a description and upload attachments for it.
     * Users can view their tasks from their Google Calendar on this page.
     * Users can also search and filter through their tasks.
     * There is a section for them to conveniently see all the tasks that are due soon.
     * On the same page, there is also a section for them to see all the classes they are currently taking.
     
 * **Graphing** [Not completed for this iteration]
 The application will allow the users to see their progress in a visual format. 
 * **Dictionary/Thesaurus** [Not completed for this iteration]
 Users will be able to access a dictionary from the application to assist them with their homework. 

## Instructions
The fully deployed application on Heroku for this iteration can be found here: https://tdsb-app.herokuapp.com/
<!--  * Clear instructions for how to use the application from the end-user's perspective
 * How do you access it? Are accounts pre-created or does a user register? Where do you start? etc. 
 * Provide clear steps for using each feature described above
 * If you cannot deploy your application for technical reasons, please let your TA know at the beginning of the iteration. You will need to demo the application to your partner either way. -->

- Students from TDSB have their school accounts linked to Gmail so they directly log and get authenticated with Google. Sample account for testing is tdsb301@gmail.com with password csc301csc301. [Completed]
- Once they log in, the home page will show a brief overview of assessments with due dates and their self inputted completion on each assessment. [Completed]
- They will be able to see detailed information on each of their courses in the courses page (details include teacher, coursework, grades and ongoing assignments). [Not completed for this iteration]
- In the Tasks page, they will be able to see a detailed calendar showing when tasks are due. Tasks are assesment deadlines from Google Classroom and self inputted objectives for completion. Students chunk their assesments into mini tasks themselves, manually set a deadline for it and are given notification reminders (email and in app) on these tasks.
- Also in the Tasks page, students can click the AddTask button to add a new task. They can input the title, description and other related factors to the task. [Front-end completed]
- The next option in the navigation bar is Progress. In this section, the student can get an overview on their grades and task completion overtime to track progress. [Not completed for this iteration]
- The next option is the Tools page. As a significant of homework relies on using the dictionary for these students, they will have access to a TDSB approved dictionary.  
- In the Profile page (accessed from the drop-down menu on the very right), they are able to see and edit their information, such as timezone settings, password reset, etc.  [Not completed for this iteration]
- They can sign-out in the Profile drop-down menu to exit the application. [Completed]
