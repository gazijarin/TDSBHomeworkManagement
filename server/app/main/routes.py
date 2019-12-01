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