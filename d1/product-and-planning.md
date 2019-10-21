# Team 12
> _Note:_ This document is meant to evolve throughout the planning phase of your project.    
 > That is, it makes sense for you commit regularly to this file while working on the project (especially edits/additions/deletions to the _Highlights_ section).
 > Most importantly, it is a reflection of all the planning you work you've done in the first iteration. 
 > **This document will serve as an agreement between your team and your partner.**

## Product Details
 
#### Q1: What are you planning to build?

<!--  * Short (1 - 2 min' read)
 * Start with a single sentence, high-level description of the product.
 * Be clear - Describe the problem you are solving in simple terms.
 * Be concrete. For example:
    * What are you planning to build? Is it a website, mobile app,
   browser extension, command-line app, etc.?      
    * When describing the problem/need, give concrete examples of common use cases.
 * Focus on *what* your product does, and avoid discussing *how* you're going to implement it.      
   For example: This is not the time or the place to talk about which programming language and/or framework you are planning to use.
 * **Feel free (and very much encouraged) to include useful diagrams, mock-ups and/or links**. -->

The product is a **homework management software** that is accessible via desktop and mobile. It is a **web application** integrable with Google Classroom such that tools like Google Calendar are utilized to maximize student organization. 

The problem that the product is trying to solve is the disorganization of middle to high school students when it comes to schoolwork management. The product aims to motivate the students to create their own form of coordination in order to encourage self-fulfilment and self-learning from a young age. 

The main use case for this product would generally be the same as how Quercus is for students at the University of Toronto. Instead of the aim being at students enrolled in a specific university, this product would serve as a more hands-on version of school management, aiming at all students enrolled under the Toronto District School Board. The product will be an online, multi-functional agenda which holistically combines key functionalities.

Students who use the product will be able to track their own homework progress, set deadlines, and deconstruct large assignments into smaller tasks to complete. 

In addition to the features of scheduling and setting tasks, the student will also have resources built-in to help facilitate learning. These built-ins include a graphing software, a chatbox to discuss with other peers, an image gallery to store useful snippets and a thesaurus. 

Tentative, basic mock-ups:
**Log-in Screen**
![](https://i.imgur.com/2yt5dbH.png)
**Home Screen**
![](https://i.imgur.com/C3UdaKH.png)



#### Q2: Who are your target users? 

<!--  * Short (1 - 2 min' read max)
 * Be specific (e.g. a 'a third-year university student studying Computer Science' and not 'a student')
 * Feel free (but not obligated) to use personas.         
   You can create your personas as part of this Markdown file, or add a link to an external site (for example, [Xtensio](https://xtensio.com/user-persona/)). -->
   
The target users for our product would be students from grade 6-8 as well as their parents and their teachers. The users would in the future expand to all students in the school district (Elementary to High School students)

#### Q3: Why would your users choose your product? What are they using today to solve their problem/need?

<!--  * Short (1 - 2 min' read max)
 * We want you to "connect the dots" for us - Why does your product (as described in your answer to Q1) fits the needs of your users (as described in your answer to Q2)?
 * Explain the benefits of your product explicitly & clearly. For example:
    * Save users time (how much?)
    * Allow users to discover new information (which information? And, why couldn't they discover it before?)
    * Provide users with more accurate and/or informative data (what kind of data? Why is it useful to them?)
    * Does this application exist in another form? If so, how does your differ and provide value to the users?
    * How does this align with your partner's organization's values/mission/mandate? -->

Currently, TDSB students utilize Google Classroom integrated with Google Calendar, as well as agendas distributed by the schools themselves. The Google Classrooms and Calendars are populated with information from the teachers while the agendas are left to be used by the students to plan out and organize their time and work efficiently. This has proved to be a difficult task, especially for young students, as they often simply forget to use these. Many students even choose not to due to the extra hassle of having to further write everything down. They also do not have the added benefit of reminders and integration with the Google Classroom technology so as to easily access the information that is already there to be used.

While there are already an abundance of apps that help with time management, there are very few from the schoolboard itself, making them non-integratable with their Google Classrooms. This added integration will allow students to leverage information already uploaded by teachers, making the process of them organizing tasks more efficient. This will cut down all the time students would otherwise waste on copying information to their scheduling apps, also ensuring that they have the most accurate and up-to-date information, such as grades and due dates. They will have the added benefit of reminders as well as helpful guides to break up large assignments into sizable portions which not many apps provide an interface for. This will make the act of organizing and chunking up assignments into a learning experience that they will be able to apply to other aspects of life, making this product align with the vision that TDSB has for this project.

The most important aspect of our app that differentiates it from other similar applications is the fact that our application promotes learning, and self reflection. It allows students to collaborate with other students, teaches them about organization techniques with how it will guide them in organizing their tasks, and it will also be a platform that enables students to ask themselves and answer self-reflective questions about their progress in school and life, promoting them to aim high and feel proud of their accomplishments.



#### Q4: How will you build it?
<!--  * Short (1-2 min' read max)
 * What is the technology stack? Specify any and all languages, frameworks, libraries, PaaS products or tools. 
 * How will you deploy the application?
 * Describe the architecture - what are the high level components or patterns you will use? Diagrams are useful here. 
 * Will you be using third party applications or APIs? If so, what are they?
 * What is your testing strategy? -->

We will be utilizing a microservice architecture for the project. This will add modularity to the application as well as scalabality and maintainability. An example of the planned design can be seen below:
![Microservice Design](https://i.imgur.com/6gSgGph.jpg)

We will be using the VueJs framework for the front-end and the flask microframework for the back-end, as well as MongoDB for the databases. To integrate with Google Classroom and Google Calendar, we will also make use of the Classroom API and Calendar API. We will deploy the application using the cloud service resources that will be provided by TDSB.

Our development will be very focused on test-driven development. We will ensure that every back-end microservice we write will be properly documented and tested, with the addition of any new features. We will have unit tests and integration tests.


#### Q5: What are the user stories that make up the MVP?
<!--  * At least 5 user stories concerning the main features of the application - note that this can broken down further
 * You must follow proper user story format (as taught in lecture) ```As a <user of the app>, I want to <do something in the app> in order to <accomplish some goal>```
 * If you have a partner, these must be reviewed and accepted by them
 * The user stories should be written in Github and each one must have clear acceptance criteria -->

1. As a student, I want to be able to add my tasks in the app, so I can stay more organized in school.
Acceptance Criteria:
    * Title of task
    * Class of task
    * Description of task
    * Able to attach picture to task
    * Progress bar of completion
    * Input grade for task
    * Reflection questions for task
    * Able to pull task from Google Classroom
    
<!-- 2. As a user, I want to see how many assignments I completed over time and my average in them, so I can see how well I’m doing in school.
Acceptance Criteria:
    * Bar graph of average in each class
    * Line graph of average in one class over time
    * Line graph of how many assignments completed over time -->

2. As a student, I want to set deadlines for schoolwork, so I can plan ahead by seeing when my projects are due on the calendar. 
Acceptance Criteria:
    * Title of project
    * Date of project deadline
    * Time of project deadline
    * Calendar
        1.	Display current year
        2.	Display current month
        3.	Display weeks of current month
        4. Display days per week
        5.	Button to click and set deadline



3. As a student, I want to chat with my classmates in the app, so we can collaborate on how to do our group projects together.
Acceptance Criteria:
    * Chat box for two users
    * Profile picture in chat
    * Name in chat
    * Textbox to enter message to user
    * History of messages sent to each other
    * Users must add each other before they can chat
    

4. As a parent, I want to track homework progress of my child so I can know how my child performs in studies.
Acceptance Criteria:
    * Ability to register and log in as a parent.
    * Ability to connect the parent account to a student account.
    * Ability to browse all existing projects, both completed and in-progress ones, in the connected student account.
    * For each project, provide following information:
        1.	Title of the project
        2.	Class of the project
        3.	Description of the project
        4.	All attached pictures of the project
        5.	For an in-progress project, show the progress bar
        6.	For a completed project, show the grade
        
5. As a student, I want to  track my homework and exam grades so that I can easily assess my academic performance and adjust accordingly.
Acceptance Criteria:
    * Allow students to enter any kind of grade into the system.
    * Any grade must have an accompanying title.
    * Any grade must be in relation to some course.
    * Allow students to add description to grades.
    * Showcase all grades for a course in one pane so it is easy to see all grades in a glance.
    * Incorporate grade weighting feature to calculate predicted final grade.
    * Potential feature: Display graph to showcase grade performance over time for a course.

6. As a student, I want to update existing projects so I can keep track of my progress.
Acceptance Criteria:
    * Ability to show all existing projects.
    * Ability to delete selected project.
    * Ability to modify the project information, including title, class, description, etc.
    * Ability to upload pictures for existing projects.
    * Ability to set milestones for each project.
    * Ability to change the status of each milestone: in progress/completed
    * Ability to change the status of each project: in progress/completed.
    * Ability to input a grade for the project
    * Ability to add/modify a progress bar for each project
    
7. As a teacher, I want to moderate the student inbox so that the students can engage respectfully in a safe environment. 
Acceptance Criteria:
    * Search bar
        1. Search a student by their email
        2. Click on student to redirect to their profile
    * Access student inbox
        1. Display their interactions inside inbox

8. As a student, I want to visualize my completion on specific projects, so I can track and assess my growth in work completion throughout the year.
Acceptance Criteria:
    * Ability to specify the project.
    * Ability to choose the type of graph.
    * Ability to generate a graph based on existing project information (e.g. number of finished/unfinished milestones, grade, average, update frequency, etc.)
    * Ability to change the graph when the information it based on changes.
    * Ability to attach the graph to the project


----

## Process Details



### Roles & responsibilities

<!-- Describe the different roles on the team and the responsibilities associated with each role. 
 * Roles should reflect the structure of your team and be appropriate for your project. Not necessarily one role to one team member. -->
 #### General Roles

- UX designer:
    - Will design detailed prototypes of the application
    
- Front End:
    - Will develop the UI and client side of the application

- Back End (API design): 
    - Handles the server side of the application and primarily focuses on API design and middleware

- Back End (Database and Dev ops):
     - Primarily focuses on designing and integrating the database. Writing queries for the middleware team 
     - Responsible for maintaining the production environment
     
- Product Manager:
    - Responsible for ensuring the project as a whole is meeting client needs
    - Responsible for setting team and client meetings 
    

#### Team Member and their Roles
<!-- 
List each team member and: -->
<!--  * A description of their role(s) and responsibilities including the components they'll work on and non-software related work
 * 3 technical strengths and weaknesses each (e.g. languages, frameworks, libraries, development methodologies, etc.) -->

- **Anirudh Baskar**:
    - Role: Back-end (primarily API design)
    - Components:
        - Server-side and databases
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

- **Raiyan Rahman**:
    - Role: Full Stack, Product Management
    - Components:
        - API Design and Implementation
        - UX Design
        - Front-End Design and Implementation
        - Features: Home screen, Google Calendar/Classroom integration 
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

- **Anusha Fazal**:
    - Role: Full Stack
    - Components:
        - UX Design
        - Front-End Work
        - Back-End API Integration
        - Features: Homework submission, Graphing
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
        - Front end development
            - HTML, CSS
    - Technical weaknesses:        
        - UI design

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
 
- Members are expected to provide weekly updates on their progress on Sunday through Messenger group chat.
- Members are to respond to questions/concerns directed at them within 24 hours
- We will primarily communicate to the partner through email. We have obtained the phone number of our patner and will use it if the partner does not respond within 48 hours
- In addition to our immediate supervisor (Veronica), we have also obtained the email of a TDSB IT department  worker and will use that for technical inquiries
- Extra: We have the emails of all the students in the other group who are also working with us. We will use that to communicate the division of work and ensure that none of our work overlaps, and if it does, to make it very clear so there are no misunderstandings. 

 
Meetings:
<!--  * How are people held accountable for attending meetings, completing action items? Is there a moderator or process? -->
- Members are expected to show up to general meetings set through Messenger group chat. They also have the option of joining in through Skype or Zoom. If they are entirely not able to, they are expected to notify the group within 12 hours and ask about the meetings to stay up-to-date.
- Every week, every member should provide a brief overview about what they have done so far and what they are going to do the next week (online "stand-up" meetings). 
- In addition to the brief overview, they are expected to stay active on Trello and manage their tasks individually. If they are done a specific task within a deadline, they should mark it completed on the taskboard. If not, they should make an issue on the taskboard and try to resolve it by discussing with the group.
 
Conflict Resolution:
<!--  * List at least three team scenarios/conflicts you discussed in lecture and how you decided you will resolve them. Indecisions? Non-responsive team members? Any other scenarios you can think of? -->

Scenario 1: Non-responsive team members 
- If a member fails to respond to questions directed at them within 24 hours or is absent in team meetings without notice, we would call them on their personal phone number and try to approach them in class if possible. If there is no response for a prolonged period (over 5 days), their task will be assigned to other sub team members on a voluntary basis and the TA will be notified.

Scenario 2: Indecision on how to approach a problem/feature 
   - We would employ the strategy discussed in tutorial where each member would rate the difficulty/feasibility of aproaching the problem in a certain way. If everyone's rating is similar, we would move forward with the approach. If not, each member will discuss their viewpoints and we will hold the vote again untill a consensus is reached. 

Scenario 3: A member not meeting their assigned requirements
   - In this case, we will ask the member to reassess their strengths and weaknesses and move them to a feature/team they are more comfortable with working on. They may also be asked to take on more non technical responsibilities. Their role will be taken on by another member on a voluntary basis.    



#### Events

<!-- Describe meetings (and other events) you are planning to have:
 * When and where? Recurring or ad hoc? In-person or online?
 * What's the purpose of each meeting?
 * Other events could be coding sessions, code reviews, quick weekly sync meeting online, etc. -->

The general meetings will take place at 4 pm Fridays in BA2270. The meetings are usually set every two weeks or so, to ensure everyone is on the right level of understanding. These meetings cover the current project progress, as well as resolve any team conflicts if there are any. These general meetings are not required to be in-person, and members can join in with Skype or Zoom if they are not able to in-person.

The "stand up" meetings occur every week, through the Messenger group chat. Everyone in the team must message the group chat on Sunday about what they have done so far and what they are going to do the following week. Although the default setting of those meetings are online, they can also be set online if there is any delay in progress.

In addition, there are also optional code-review meetings which take place during the tutorial timeslot, 12-1 PM Tuesdays in UC244. If the tutorial is not a free work session, then the code review would get moved to the hour after, 1-2 PM. These are only set up if there are outstanding problems with the code base or any small technical difficulties, which could be resolved with the insight and/or help from everyone in the team. Again, these sessions are not required to be in-person, and members can join in with Skype or Zoom if they are not able to in-person.

#### Partner Meetings
<!-- You must have at least 2 meetings with your project partner - an initial planning meeting and a document review meeting. Describe the meetings here:
* When and where?
* What did you discuss during the meeting (**note you must have meeting minutes**)?
* What were the outcomes of each meeting? -->

The meetings took place in Gerstein, room 1200, around 12-1 PM. During the meetings, we introduced ourselves and received feedback on how the product partner wants the web application to be done. The project partner shared her sentiments regarding the project need, which helped us gain understanding about the true nature behind the app. We learned that it is predominantly to motivate students to be administrators of their own academic success by organizing schoolwork in a multi-functional app, instead of mindlessly writing down notes on an agenda. Therefore, this meeting helped us understand *why* we are making the product and made a lot of high-level descriptions of the product clear.

Secondly, the project partner also let us know how to proceed with the user stories. The project partner shared her experience with students and what their needs were. Those insights made us envision an image of the student and specific information regarding the functionality of the application, which helped in writing the user stories from different angles.


#### Artifacts
<!-- List/describe the artifacts you will produce in order to organize your team.       

 * Artifacts can be To-Do lists, Task boards, schedule(s), etc.
 * We want to understand:
   * How do you keep track of what needs to get done?
   * How do you prioritize tasks?
   * How do tasks get assigned to team members? -->

We will be following the traditional agile methodology using a trello board as our primary task board. Here, we will update tasks that are added as needing to be done, those in development, those that are being tested, as well as the tasks we have completed.

We have divided our group into developers that specialize in back-end, front-end, and databases according to our strenghts and previous experience. Although we will primarily stick to these parts of the project, we will definitely be more fluid with these roles and move around to get tasks done and help teammates when they need it.

Teammates will discuss with everyone and pick tasks to complete by assigning it to themselves on the trello board. Tasks will be prioritized with regards to how crucial they are to getting the base application and the MVP running and functioning properly to meet the basic requirements set forth by TDSB.

Our primary source of communication for discussing matters about the project and tasks will be through our facebook messenger group. We answer questions, discuss tasks, and schedule meetings through it. Our group also has scheduling features and reminders which will prove to be useful in ensuring we get tasks done on time.


----
### Highlights
<!-- **Note this section is optional**
YOUR ANSWER GOES HERE ...

Specify 3 - 5 key decisions and/or insights that came up during your meetings
and/or collaborative process.

 * Short (5 min' read max)
 * Decisions can be related to the product and/or the team process.
    * Mention which alternatives you were considering.
    * Present the arguments for each alternative.
    * Explain why the option you decided on makes the most sense for your team/product/users.
 * Essentially, we want to understand how (and why) you ended up with your current product plan. -->


We thought of appraching this project with a "feature-first" mindset where we would just implement and add whatever feature that the parters required. However, our group, through the meetings and discussions with TDSB and amongst ourselves, has decided on a plan to put our design and usability at the forefront. Our target audience for this project consists of students in middle school and high school. With a younger age group such as this, we know to take into account how young technology users are very prone to switching over to applications that are simpler to use and visually and aesthetically pleasing.

We decided to spend extra time to create possible mockups of medium fidelity with wireframes, and conduct interviews with a set of students that would fall inside the group of potential users. We would then proceed with a very user-centric design, to ensure that our product would remain user friendly. Once we have the general layout of our design planned and tested, we would be able to speed up our development process to complete the features that are requred.

We have planned a meeting with the IT head at TDSB to inquire about how much of their existing Google Classroom and Calendar information we would be able to leverage, as this would not only speed up our development but it would also enable us to fully utilize the existing information for the Google APIs to ensure that we are working with meaningful data when developing and testing our product.

We will develop this project using the microservice architecture as it will be easy to scale and maintain. This will also allow us to easily test certain backend functionality and easily add on more functionalities as they become known. This will help us deal with the changing requirements of a project of this type. As our team members all have courses that they must also attend to, this will ensure that our tasks are easy to manage and module in nature. In this way, we will be able to still work separately while collaborating together to achieve the end product.
