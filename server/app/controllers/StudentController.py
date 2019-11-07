from app.models.Student import Student
import uuid


def post(first_name, last_name, image, email, _id):
    new_student = Student(first_name= first_name, last_name=last_name, _id=_id, image=image, email=email)
    new_student.insert()
