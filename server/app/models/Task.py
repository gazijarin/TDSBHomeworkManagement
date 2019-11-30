import datetime

from app.database import DB


class Task(object):

    def __init__(self, title, deadline, course, description, attachments, student, _id):
        self._id = _id
        self.title= title
        self.deadline = deadline
        self.course = course
        self.description = description
        self.attachments = attachments
        self.student = student


    def insert(self):
        if not DB.find_one("Tasks", {"_id": self._id}):
            DB.insert(collection='Tasks', data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "deadline": self.deadline,
            "course": self.course,
            "description": self.description,
            "attachments": self.attachments,
            "student": self.student
        }