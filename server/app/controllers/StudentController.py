from models.Student import Student
import uuid


def post(first_name, last_name):
    new_student = Student(first_name= first_name, last_name= last_name,_id=str(uuid.uuid4()))
    new_student.insert()
