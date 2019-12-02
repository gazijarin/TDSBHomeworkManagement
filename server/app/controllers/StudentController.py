from app.models.Student import Student
import uuid
import datetime

student = Student()

def post(first_name, last_name, image, email, _id, courses):
    payload = {"first_name": first_name, 'last_name': last_name,'_id': _id, "image": image,
                    "email": email, "courses": courses, "created": datetime.datetime.utcnow()}
    payload["last_sync_date"] = payload["created"]
    student.insert(payload)

def get(_id):
    return student.get(_id)
