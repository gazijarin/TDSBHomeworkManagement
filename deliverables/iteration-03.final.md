# Team 12 Final Iteration

## Final Iteration

 * Start date: Monday, Nov 18th
 * End date: Monday, Dec 2nd

### Changes from you `product.md`
List the most significant changes you made to your product (if any). It's normal to change features mid-project or reduce the scope to meet timelines. 

 * Start with the most significant change
 * Identify either a change in features or a reduction of your original scope
 * For each change, explain why you are making it and what you are hoping to achieve from it

 > *Note:* If you are not making (or haven't made) any changes to your product, it means you successfully scoped, planned and executed the development of your application.This is a very rare occurrence - describe what you believed enabled your team to do so and why. 
 >  -->
1. The most significant reduction that we did was not include a chat system for this application. We initially thought that we would develop the chat system by this iteration, but then we were unable to foresee the amount of time and effort that is needed to develop a well-rounded chat system that was secure, well-designed and distributed across all users. Since our project partner was not there to provide feedback and explain what the exact requirements of the chat system were, we were left with very vague details. We were unsure of how to proceed and that hindered our progress. Therefore, we decided to focus more on the other features and improve their quality, since we had a better idea of them.
2. The other significant change that we did was re-design how students organize their tasks. At first, we were told to create an image gallery for each user to store pictures of their assignments/tasks. However, as we proceeded to make the application, we realized that the choice was redundant and that each user should be able to attach specific image files to a task instead of going to a separate gallery to upload images. Since we did not receive a response from our project partner regarding the change, we decided to pursue it as it not only made the application much more cohesive but it was also more user-friendly. It allowed the user to individualize their tasks in order to organize better. 

### Handoff Plan

<!-- Describe your plan for handing off your product and all technical assets to your partner

 * Will you have a handoff meeting? If so, what will be discussed?
 * What assets/artifacts will you be handing off to your partner (e.g. codebase, deployment tools, running application, task tracker, etc.)? 
 * How will you hand off these assets/artifacts?
 * Does your partner have the technical capacity to manage/maintain/develop your product? How will that impact how you handoff the product? -->

Our team was in the unique circumstance of having an absentee project partner that did not reciprocate communication with the team after the first week of November. Due to this unfortunate situation, we were forced to work with the initial project proposal that was submitted by TDSB, and the information garnered during the project partner meetings we had upto the last time we communicated via email. This resulted in the team taking the majority, if not all, of the crucial decisions without being able to confirm whether or not it was in-line with the project partner's vision.

We continued with decisions regarding the initial mockups which we attempted to confirm with the partner, and moved with what we decided to be the most user friendly and in-line with core UX design principles. We then came up with the plans for the sprints and promptly completed the front-end in VueJs, the back-end in Flask, and the databases in MongoDB. The trello of our sprint decisions and team management as well as task assignments can be found at our Trello at https://trello.com/b/68RfNTky/term-project. The codebase was committed at equally frequent development intervals to our team's github repository at https://github.com/csc301-fall-2019/team-project-tdsb-team-2. To ensure we had a presentable demo and that our application was usable, we deployed a build of it to heroku at https://tdsb-app.herokuapp.com/. As our project partner has nor replied to set up any meetings for a potential handoff we are currently not able to perform a project handoff of these artifacts.

Our team has taken steps to ensure that the application is easily scalable and maintainable. We have followed modularity techniques as shown in lecture as well as microservice based architecture. This makes sure that any new features and functionalities may be added to the application with ease. We also modularized many components of the front-end to ensure reusability and maintainability. As our project partner seemed very non-technical and as it was made known that the application would not be able to be maintained by very technically savvy developers, we made sure to incorporate sufficient amounts of documentation to enable readability of the different code we added during development. We hope that if any potential project partner or team wishes to continue working on this, they will be able to do so with ease and get familiar with the codebase in as little time as possible and be able to start making meaningful changes right away.


<!-- > *Note:* This is one of the most important aspects of the project. Please consult with your partner, your TA and the instructors on how to successfully execute this.  -->
