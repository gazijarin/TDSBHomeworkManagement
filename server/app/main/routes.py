from app.main import bp  # noqa
from app.controllers import StudentController
from flask import jsonify, abort, request


@bp.route('/')
def index():
    return 'Hello World!'

#sample

@bp.route('/api/students', methods=['POST'])
def post_student():
    first_name = request.args.get('first_name')
    #last_name = request.args.get['last_name']

    StudentController.post(first_name, "last_name")
    return jsonify("Sucessfully added test student")

