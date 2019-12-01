from app.models.Task import Task
from flask import jsonify
import uuid

task = Task()

def post(title, deadline, course_id, description, attachments, student):
    task.insert({"title":title,"deadline":deadline, "course_id": course_id,
         "description": description, "attachments":attachments,"student": student, "_id":str(uuid.uuid4())})

def get(id):
    return task.get(id)

def delete(id):
    return task.delete(id)

def update(title, deadline, course_id, description, attachments, student, _id):
    return task.update(_id, {"title": title, "deadline": deadline, "course_id": course_id,
                 "description": description, "attachments": attachments, "student": student, "_id": _id})
