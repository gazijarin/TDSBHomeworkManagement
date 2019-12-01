from app.models.Task import Task
from flask import jsonify
import uuid


def post(title, deadline, course, description, attachments, student):
    new_task = Task(title=title,deadline=deadline, course=course, description=description, attachments=attachments, student=student, _id=str(uuid.uuid4()))
    new_task.insert()
    return new_task.json()