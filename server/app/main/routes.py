from app.main import bp  # noqa
from bson.objectid import ObjectId
from app.controllers import StudentController, CourseController, TaskController
from flask import jsonify, abort, request, make_response
from app.database import DB
from gridfs.errors import NoFile
import datetime
import requests
import json


# helper function to create a datetime object
def create_date(date, time):
    date = date.split()
    time = time.split()
    month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, 
                    "Apr":4, "May": 5, "June": 6,
                    "July": 7, "Aug": 8, "Sept": 9, 
                    "Oct": 10, "Nov": 11, "Dec": 12}
    day = int(date[0])
    month = month_dict[date[1]]
    year = int(date[2])
    hour = int(time[0][0:2])
    minute = int(time[0][3:])
    date_obj = datetime.datetime(year, month, day, hour, minute)
    return date_obj

@bp.route('/')
def index():
    return 'Hello World!'



@bp.route('/api/students', methods=['POST'])
def post_student():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    image = data['image']
    _id = data['_id']
    courses = data['courses']
    StudentController.post(first_name, last_name, image, email, _id, courses)
    return jsonify("Sucessfully added test student")

# endpoint to get student detail by id
@bp.route('/api/student/<id>', methods=['GET'])
def get_student(id):
    return StudentController.get(id)



# calls external dictionary API for given word
@bp.route('/api/dictionary', methods=['GET'])
def get_dict():
    word = request.args.get('word')
    dict_url = 'https://googledictionaryapi.eu-gb.mybluemix.net/?define=' + word
    result = requests.get(dict_url)
    return result.text

# upload files
@bp.route('/api/file/upload', methods=['POST'])
def post_file():
    uploaded_files = request.files.getlist('file')
    files_result = []
    for file in uploaded_files:
        file_id = DB.save_file(file, file.filename)
        file_obj = {"_id": str(file_id), "filename": file.filename}
        files_result.append(file_obj)
    return json.dumps(files_result)

# get files by id
@bp.route('/api/file/retrieve', methods=['GET'])
def retrieve_file():
    file_id = request.args.get('id')
    try:
        fl = DB.get_file(file_id)
        response = make_response(fl.read())
        return response
    except NoFile:
	    abort(404)



# endpoint to create a task
@bp.route('/api/task', methods=['POST'])
def post_task():
    print(request)
    data = request.get_json(silent=True)
    title = data['title']
    date = data['date']  # should be in the form of "08 Nov 2019"
    time = data['time'] # should be in the form of "12:00 PM"
    course = data['course']
    description = data['description']
    student = data['student'] # student id
    attachments = data['attachments'] # a list of uploaded file returned by the upload api 

    deadline = create_date(date, time)
    
    result = TaskController.post(title, deadline, course, description, attachments, student)

    return result

# endpoint to get a task by id
@bp.route('/api/task', methods=['GET'])
def get_task():
    task_id = request.args.get('id')
    task = DB.find_one("Tasks", {"_id": task_id})
    if task:
        return jsonify(task)
    # no student match
    abort(404)

# endpoint to delete a task by id
@bp.route('/api/task', methods=['DELETE'])
def delete_task():
    task_id = request.args.get('id')
    task = DB.find_one("Tasks", {"_id": task_id})
    if task:
        DB.remove("Tasks", {"_id": task_id})
        return jsonify("Task removed")
    
    return jsonify("No task matching given id")

#endpoint to update task by id
@bp.route('/api/task', methods=['PATCH'])
def upadte_task():
    task_id = request.args.get('id')
    task = DB.find_one("Tasks", {"_id": task_id})
    if task:
        data = request.get_json(silent=True)
        title = data['title']
        date = data['date']
        time = data['time']
        course = data['course']
        description = data['description']
        attachments = data['attachments']

        new_deadline = create_date(date, time)

        DB.update("Tasks", {"_id": task_id}, { "$set": {"title": title, "deadline": new_deadline, "course": course, 
                    "description":description, "attachments": attachments }})
        return jsonify("Task updated")

    return jsonify("No task matching given id")   

# endpoint to get all tasks for a student
@bp.route('/api/task/student', methods=['GET'])
def get_task_by_student():
    student_id = request.args.get('id')
    result = []
    tasks = DB.find("Tasks", {"student": student_id})
    for task in tasks:
        result.append(task)
        
    return jsonify(result)