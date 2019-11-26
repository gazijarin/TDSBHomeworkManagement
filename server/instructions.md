App Structure:

requirements.txt holds all the dependencies that needs to be installed to run the app

inside app folder:

    __init__.py holds the starter code when the server is run (run this to start the app)

    database.py holds the starter code for the database when the server starts (database methods are defined here)

    ./main./routes file stores all the API endpoints for the server


    ./controllers folder stores all the intermediary methods between the front end and backend

    ./models folder stores all the information about our Database objects


Steps for running the server

    1) cd into server

    2) py -m venv .venv

    3) py -m pip install dnspython

    4) py -m pip install requests

    5) export FLASK_APP=app.run.py (For windows: set FLASK_APP=app.run.py)

    6) py -m flask run

API Testing URLs examples:

    * All ids are just placeholders, may or may not work.

    Create a new student: /api/studen?first_name=Jane&last_name=Doe&email=1223213124566@gmail.com [POST]

    Get stduent information: /api/student/b9663d09-1576-4562-a852-76d7342faf26 [GET]

    Delete a student:  /api/student/b9663d09-1576-4562-a852-76d7342faf26 [DELETE]

    Update student information: /api/student/b9663d09-1576-4562-a852-76d7342faf26?first_name=Jane&last_name=Doe&email=000@gmail.com [PATCH]

    Enroll student in a course:/api/student/enroll?student=b9663d09-1576-4562-a852-76d7342faf26&course=2553e83a-8054-4e9c-b8d8-457e8a456287 [PATCH]

    Drop student from a course: /api/student/drop?student=b9663d09-1576-4562-a852-76d7342faf26&course=2553e83a-8054-4e9c-b8d8-457e8a456287 [DELETE]

    Input grade for a course: /api/student/grade?student=b9663d09-1576-4562-a852-76d7342faf26&course=2553e83a-8054-4e9c-b8d8-457e8a456287&grade=85 [PATCH]

    Get information for all enrolled courses: /api/student/courses?id=0110415d-0050-47ae-9f8b-7ad21582b4e0 [GET]

    Create a new course: /api/course?name=CSC10000000&instructor=Foxtrot [POST]

    Get course information: /api/course?id=2553e83a-8054-4e9c-b8d8-457e8a456287 [GET]

    Delete a course: /api/course?id=2553e83a-8054-4e9c-b8d8-457e8a456287 [DELETE]

    Update course information: /api/course?id=f02b40bb-1a9b-44d8-8905-d96a504e1bc7&name=CSC386&instructor=Jason [PATCH]

    Get information for all enrolled students: /api/course/students?id=2553e83a-8054-4e9c-b8d8-457e8a456287 [GET]

    Dictionary: /api/dictionary?word=hello [GET]


MongoDB Information:
    database Name: TDSB
    url: "mongodb+srv://TDSB301:csc301csc301@tdsb-x6zvw.mongodb.net/test?retryWrites=true&w=majority"
    user: TDSB301
    Password: csc301csc301