# Team 12, Deliverable 2 - Part 2

<!--  > _Note:_ This document is meant to be written during (or shortly after) your review meeting, which should happen fairly close to the due date.      
 >      
 > _Suggestion:_ Have your review meeting a day or two before the due date. This way you will have some time to go over (and edit) this document, and all team members should have a chance to make their contribution. -->


## Iteration 02 - Review & Retrospect

 * When: Saturday, November 9th
 * Where: Online

## Process - Reflection

Beginning with the mockups, we have implemented the basic design and highest priority features of the front-end as well as set up the basic back-end, as well as the databases. We have added integration with the Google APIs as well included an interface which will allow users to log in with their TDSB accounts.

#### Decisions that turned out well

<!-- List process-related (i.e. team organization) decisions that, in retrospect, turned out to be successful.


 * 2 - 4 decisions.
 * Ordered from most to least important.
 * Explain why (i.e. give a supporting argument) you consider a decision to be successful.
 * Feel free to refer/link to process artifact(s). -->
 
 - Our decision to do the mockups and front end initially at the beginning of the project helped to pave the way for the design and tasks of the overall application. We had a very good general idea of what the different functionalities would look like and how we would go about implementing them. The mockups could be found here: https://trello.com/c/x8RTRyLu/7-ux-mockups-prototype
 - We split the team up into different development groups, dealing with the front-end, back-end, databases, mockups, etc. Having teams specifically focusing on the different areas ensured that the same task was not being done by multiple people, and that people could shoulder responsibility and that motivated everyone to contribute. This also made sure that no redundant work was being done, resulting in an efficient development process.
 - The trello proved to be a more concrete form of task tracking and management than just discussing and assigning tasks in the Facebook group chat. We also used it as a reference hub for all the decisions made and the features requested by the project partner. This allowed group members to quickly find references to mockups and links to external sites and resources which they found useful and were able to leverage in completing the deliverable. The entire trello taskboard can be found here: https://trello.com/b/68RfNTky/term-project

#### Decisions that did not turn out as well as we hoped

<!-- List process-related (i.e. team organization) decisions that, in retrospect, were not as successful as you thought they would be.

 * 2 - 4 decisions.
 * Ordered from most to least important.
 * Feel free to refer/link to process artifact(s). -->
 - The project partner was absent throughout the majority of the development process. She was not responsive to emails to set up meetings, validate our updated user stories and acceptance criteria, conduct user interviews and select mockups, and attend a demo. Therefore, we could not interact with the intended userbase (students from middle to high school) as well as we had hoped. This resulted in us having to make many decisions ourselves on how we would approach the project requrements, and much of how the end product will look like. We, however, still attempted to follow the requirements set forth initially to the best of our abilities and always factored them in to our development plan and decisions.
 - We initially attempted to allow users to create their own accounts in the product. However, this was not necessary as the students had their own TDSB accounts (Gmail) that they could use to log in to the application. Therefore, all that was needed is a sign-in redirection that led to the Google sign-in page. Thus, this resulted in some redundant work which we were fortunately able to turn around quickly after reviewing the requested requirements. Log-in with Google can be found in the github repository ( https://github.com/csc301-fall-2019/team-project-tdsb-team-2), under `/commit/76f741178bfc115caae711d8f15a12a937ae95b2`.
 - We also attempted to incorporate branching for different features into our development process. However, more often than not, we ended up committing to master which did not follow the suggested development practices from the course. As members ended up working on very separate aspects of the application, we ended up not needing to branch for every feature since there were almost always no conflicts.


#### Planned changes

<!-- List any process-related changes you are planning to make (if there are any)

 * Ordered from most to least important.
 * Explain why you are making a change. -->
 
 - Our application deployment plan was changed to be done in Heroku. We still utilized the docker image which helped in the deployment process. It proved to also be beneficial as the change allowed for a much simpler deployment with easily updateable builds.
 - As we were not able to get in contact with the project partner to obtain some test Google Classrooms and test student accounts, the majority of the development was done with mock data created by us to simulate real student accounts, Google Classrooms, and Google Calendars. This helped substantially to make the data we were working with concrete so we could move on with the development process rather than having to wait for any data. This also allowed us to simultaneously develop front and back end components of our application while following a specified JSON contract.


## Product - Review

#### Goals and/or tasks that were met/completed:

Overview of Tasks can be found on Trello: https://trello.com/invite/b/68RfNTky/7bf7c72f2b6a52990927cfb8dc48d44c/term-project

<!--  * From most to least important.
 * Refer/link to artifact(s) that show that a goal/task was met/completed.
 * If a goal/task was not part of the original iteration plan, please mention it. -->

1. **Server and Database Set-Up (Priority: High)**
    Assigned to Anirudh Baskar, Alex Shang and Samin Khan
    * Initialize Flask app to run a server on localhost (for now)
    * Initialize an instance of MondoDB with the necessary URI and create static methods to control data (insert and modify)

    Proof (Github: https://github.com/csc301-fall-2019/team-project-tdsb-team-2):
      * Initial server set up: `/commit/21917a160e30ce10abc465ca4ca74a80c707b64e`


2. **Basic Front-End Set-Up (Priority: High)**
    Assigned to Raiyan Rahman
    * Integrate basic Vue.js template to include the main window, navigation bar, account menu and background.
    
    Proof (Github: https://github.com/csc301-fall-2019/team-project-tdsb-team-2):
      * Preliminary front-end files: `/commit/d840b2541c1e8b0bc163df448caa19dab114dc8b`

3. **Home-Screen (Priority: High)**
    Assigned to Raiyan Rahman, Gazi Jarin, Anusha Fazal
    * Replicate basic mock-up of home screen to create a static webpage.
    * Features include: static toolbar (Home, Profile, ourses, Tasks, Gallery, Tools), overview window to store recent activity, side calendar and task-list.
    
   Proof (Github: https://github.com/csc301-fall-2019/team-project-tdsb-team-2):
      * Static background: `/commit/d840b2541c1e8b0bc163df448caa19dab114dc8b`
      * Fixed navigation bar: `/commit/2a8a97cba1c4c57a0353073b8fe6174c610ad8ba`
      * Home-page elements: `/commit/702e4316eb77131cec3e0b5f8dc5483bf53ccdd4`
      * Tasks page: `/commit/2cf447366c86b610f7946e92f037b6ee5c9723e5`
      * Search bar and addTask button: `/commit/5d75025d52fae3132b46ec7e7e066be0517f1fc3`
      * Icons: `/commit/2c3dbc76093497de865cbca7d1984faf175940b6`
     
     ![](https://i.imgur.com/uZL2JkI.png)




4. **Log-in and Registration (Priority: High)**
    Assigned to Anirudh Baskar, Alex Shang, Samin Khan, and Michael Katilevsky
    * Replicate basic mock-up of log-in to create a static webpage.
    * Features include: form input (name, password) and the ability to log-in with a Google account.
    * Create APIs to insert, modify and update student information such as courses, name, and user id.

       Proof (Github: https://github.com/csc301-fall-2019/team-project-tdsb-team-2):
      * Log-in page: `/commit/76f741178bfc115caae711d8f15a12a937ae95b2`
      * Log-in with Google: `/commit/76f741178bfc115caae711d8f15a12a937ae95b2`

    ![](https://i.imgur.com/8IzJw8w.png)



    

5. **AddTask Screen (Priority: Medium)**
    Assigned to Gazi Jarin, Raiyan Rahman
    * Replicate basic mock-up of addTask to create a static modal using Bootstrap elements (b-button and b-modal) in the Tasks page.
    * Features include: form input (title), date and time picker, description text editor box, and attachment box.
    
       Proof (Github: https://github.com/csc301-fall-2019/team-project-tdsb-team-2):
      * Title, description, course selection, date and time picker, attachment: `/commit/a7efd2b6e29c5d3c57f2804709fa3d7bb2728a11`
      * Implemented full modality of AddTask: `/commit/5bb000e28db0def8ab4bd0321a5f84123e83ed1e`
      * Edited time picker: `/commit/4d69037fac314036fe9e652723de040818d6cd4b`

    ![](https://i.imgur.com/7YUTMY8.png)



6. **Calendar Integration (Priority: Medium)**
    Assigned to Anusha Fazal
    * Display Calendar in the Tasks page where the tasks will appear as they are added in.
    * Get tasks from user's Google Calendar via the Google API and display it on the Calendar in the Tasks page.

    Proof (Github: https://github.com/csc301-fall-2019/team-project-tdsb-team-2):
      * Static calendar: `/commit/7843777a460e80a556419f3dbf65a64a3a250485`
      * Calendar library: `/commit/38b9baa8a591975f4063d19b66712a4f73859416`
      * Get Google Events: `/commit/853b7849e8751c184b047dd1f1907124e1a2988d`

    
    ![](https://i.imgur.com/cgMBREg.png)



#### Goals and/or tasks that were planned but not met/completed:

<!--  * From most to least important.
 * For each goal/task, explain why it was not met/completed.      
   e.g. Did you change your mind, or did you just not get to it yet? -->
   
1. **Graphing Software (Priority: Low)**
    Assigned to Gazi Jarin, Anusha Fazal
    
    Uncompleted: Did not allocate much time for this feature since it was low priority, predominantly because we only n the main features up and then we wanted to move forward with the extra features. Therefore, it should be completed for the next version where we fully implement the back-end for the main features and move on to the front-end for the less important features.

2. **Dictionary/Thesaurus Integration (Priority: Low)**
    Assigned to Alex Shang, Gazi Jarin
    
    Uncompleted: Same argument as the Graphing Software task. Dictionary integration was only a side feature in the main application so less time was allocated for it. We aim to have it done after we have completed all the more important features.

#### How was your product demo?
<!--  * How did you prepare your demo?
 * What did you manage to demo to your partner?
 * Did your partner accept the features?
 * Were there change requests?
 * What did you learn from the demo from either a process or product perspective? -->

* We took preparations for the demo by compiling all the mock-ups that we did before-hand, as well as the front-end prototypes to display our current efforts in re-creating the vision of the TDSB app. We each had prepared our section of the talk by relating it to the tasks we have completed under the Goals and Tasks section.
* The demo would consist of three parts - one part would be displaying the mock-ups that we had made, another part would be allowing the partner to interact with the application by herself to get a feel for it (live demo of the front-end prototypes), and last part would be talking about our future steps with the application. Throughout the demo, we hope to get an insight on how we are doing and to adjust our product accordingly to reflect the vision of the partner and her organization.
* Important: We did not get a chance to demo yet due to our partner being unresponsive. We have sent our partner the initial blueprints and mock-up for the project through e-mail, as well as attempted to set up an in person meeting to update her on our progress, but we have received no response as of yet.

## Meeting Highlights

<!-- Going into the next iteration, our main insights are:

 * 2 - 4 items
 * Short (no more than one short paragraph per item)
 * High-level concepts that should guide your work for the next iteration.
 * These concepts should help you decide on where to focus your efforts.
 * Can be related to product and/or process. -->
 * The Google API integration has simplified a lot of development, allowing us to leverage existing technologies to get calendars and classroom information, giving us time to focus more on the requested features by project partners.
 * Student accounts must be created the first time they log in to the application. This way, we may use existing information for this, and we can store their events and calendar information in the MongoDB databases for easy retrieval by the backend.
 * The initial demo and prototype has been created with a lot of mock data. To ensure that the data sent by the backend is of the same nature, we will have to create a JSON schema for the backend to follow so that the data that the front-end receives from the back-end is of the same structure, allowing it to be used with only minimal changes.
