from app.main import bp  # noqa
from app.controllers import StudentController
from flask import jsonify, abort, request
from app.database import DB


@bp.route('/')
def index():
    return 'Hello World!'

#sample

# endpoint to create a new student
@bp.route('/api/student', methods=['POST'])
def post_student():
    email = request.args.get('email')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    StudentController.post(email, first_name, last_name)
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
        return "Student removed"

    return "No student matching given id"
        

# endpoint to upadte student information by id
@bp.route('/api/student/<id>', methods=['PUT'])
def update_student(id):
    student = DB.find_one("Students", {"_id": id})
    if student:
        email = request.args.get('email')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        DB.update("Students", {"_id": id}, { "$set": {"email": email, "first_name":first_name, "last_name":last_name}})
        return "Successfully upadted the studetn information"

    return "No student matching given id"







@bp.route('/login', methods=['POST'])
def login():
    return
