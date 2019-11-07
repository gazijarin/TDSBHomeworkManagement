from app.main import bp  # noqa
from app.controllers import StudentController
from flask import jsonify, abort, request


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

