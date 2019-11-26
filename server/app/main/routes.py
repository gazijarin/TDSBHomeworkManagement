from app.main import bp  # noqa
from app.controllers import StudentController, CourseController
from flask import jsonify, abort, request
from app.database import DB
import requests


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
    StudentController.post(first_name, last_name, image, email, _id)
    return jsonify("Sucessfully added test student")

# endpoint to get student detail by id
@bp.route('/api/student/<id>', methods=['GET'])
def get_student(id):
    student = DB.find_one("Students", {"_id": id})
    if student:
        return jsonify(student)
    # no student match
    abort(404)

# endpoint to delete student by id
@bp.route('/api/student/<id>', methods=['DELETE'])
def delete_student(id):
    student = DB.find_one("Students", {"_id": id})
    if student:
        DB.remove("Students", {"_id": id})
        return jsonify("Student removed")

    return jsonify("No student matching given id")
        

# endpoint to upadte student information by id
@bp.route('/api/student/<id>', methods=['PATCH'])
def update_student(id):
    student = DB.find_one("Students", {"_id": id})
    if student:
        email = request.args.get('email')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        DB.update("Students", {"_id": id}, { "$set": {"email": email, "first_name":first_name, "last_name":last_name}})
        return jsonify("Successfully upadted the studetn information")

    return jsonify("No student matching given id")

# enroll student to a course
@bp.route('/api/student/enroll', methods=['PATCH'])
def enroll_student():
    student_id = request.args.get('student')
    student = DB.find_one("Students", {"_id": student_id})
    if student:
        course_id = request.args.get('course')
        course = DB.find_one("Courses", {"_id": course_id})
        if not course:
            return jsonify("No course matching given id")
        for enrolled in student["courses"]:
            if enrolled["_id"] == course_id:
                return jsonify("Student already enrolled in the course")

        DB.update("Students", {"_id": student_id}, { "$push": {"courses": {"_id": course_id,"name":course["name"], "grade": "N/A"}}})
        DB.update("Courses", {"_id": course_id}, { "$push": {"students": {"_id":student_id,"name":student["first_name"] + ' ' + student["last_name"], "grade": "N/A"}}})
        return jsonify("Successfully enrolled the studetn into the course")
    return jsonify("No student matching given id")


# drop student from a course
@bp.route('/api/student/drop', methods=['DELETE'])
def drop_student():
    student_id = request.args.get('student')
    student = DB.find_one("Students", {"_id": student_id})
    if student:
        course_id = request.args.get('course')
        course = DB.find_one("Courses", {"_id": course_id})
        if not course:
            return jsonify("No course matching given id")
        DB.update("Students", {"_id": student_id}, { "$pull": {"courses": {"_id": course_id}}})
        DB.update("Courses", {"_id": course_id}, { "$pull": {"students": {"_id": student_id}}})
        return jsonify("Student dropped the course")
    return jsonify("No student matching given id")

# Input grade for a course
@bp.route('/api/student/grade', methods=['PATCH'])
def upadte_grade():
    student_id = request.args.get('student')
    student = DB.find_one("Students", {"_id": student_id})
    if student:
        course_id = request.args.get('course')
        course = DB.find_one("Courses", {"_id": course_id})
        if not course:
            return jsonify("No course matching given id")
        enrolled = False
        for enrolled_course in student["courses"]:
            if enrolled_course["_id"] == course_id:
                enrolled = True
        if not enrolled:
            return jsonify("Student not enrolled in the course")
        grade = int(request.args.get('grade'))
        DB.update("Students", {"_id": student_id, "courses._id":course_id},{"$set" : {"courses.$.grade": grade}})
        DB.update("Courses", {"_id": course_id, "students._id":student_id},{"$set" : {"students.$.grade": grade}})
        return ("Successfully update the grade")

    return jsonify("No student matching given id")

# get information for all enrolled courses
@bp.route('/api/student/courses', methods=['GET'])
def get_courses():
    student_id = request.args.get('id')
    student = DB.find_one("Students", {"_id": student_id})
    if student:
        if student["courses"]:
            return jsonify(student["courses"])
        return jsonify("The student is not erolled in any course")

    return jsonify("No student matching given id")

# endpoint to create a new course
@bp.route('/api/course', methods=['POST'])
def post_course():
    name = request.args.get('name')
    instructor = request.args.get('instructor')
    CourseController.post(name, instructor)

    return jsonify("Sucessfully added test course")

# endpoint to get course detail by id
@bp.route('/api/course', methods=['GET'])
def get_course():
    course_id = request.args.get('id')
    course = DB.find_one("Courses", {"_id": course_id})
    if course:
        return jsonify(course)
    # no course match
    abort(404)

# endpoint to delete course by id
@bp.route('/api/course', methods=['DELETE'])
def delete_course():
    course_id = request.args.get('id')
    course = DB.find_one("Courses", {"_id": course_id})
    if course:
        DB.remove("Courses", {"_id": course_id})
        return jsonify("Course removed")
    
    return jsonify("No course matching given id")

# endpoint to update course information by id
@bp.route('/api/course', methods=['PATCH'])
def update_course():
    course_id = request.args.get('id')
    course = DB.find_one("Courses", {"_id": course_id})
    if course:
        name = request.args.get('name')
        instructor = request.args.get('instructor')
        DB.update("Courses", {"_id": course_id}, { "$set": {"name": name, "instructor":instructor}})
        return jsonify("Successfully upadted the studetn information")

    return jsonify("No course matching given id")

# get information for all enrolled students
@bp.route('/api/course/students', methods=['GET'])
def get_students():
    course_id = request.args.get('id')
    course = DB.find_one("Courses", {"_id": course_id})
    if course:
        if(course["students"]):
            return jsonify(course["students"])
        return jsonify("No student enrolled in the course")
    return jsonify("No course matching given id")

# calls external dictionary API for given word
@bp.route('/api/dictionary', methods=['GET'])
def get_dict():
    word = request.args.get('word')
    dict_url = 'https://googledictionaryapi.eu-gb.mybluemix.net/?define=' + word
    result = requests.get(dict_url)
    return result.text