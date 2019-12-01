from app.models.Student import Student
import uuid


def post(first_name, last_name, image, email, _id, courses):
    student = Student()
    student.insert({"first_name": first_name, 'last_name': last_name,'_id': _id, "image": image,
                    "email": email, "courses": courses})

def get(id):
    student = Student()
    return student.get(id)
