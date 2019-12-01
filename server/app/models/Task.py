import datetime

from app.database import DB
from flask import jsonify, abort

class Task(object):

    def insert(self, payload):
        DB.insert(collection='Tasks', data=payload)
        return payload
            
            
    def get(self, id):
        task = DB.find_one("Tasks", {"_id": id})
        if task:
            return jsonify(task)
        abort(404)

    def delete(self, id):
        task = DB.find_one("Tasks", {"_id": id})
        if task:
            DB.remove("Tasks", {"_id": id})
            return jsonify("Task removed")

        return jsonify("No task matching given id")

    def update(self, id, payload):
        print(payload)
        task = DB.find_one("Tasks", {"_id": id})
        if task:
            DB.update("Tasks", {"_id": id}, { "$set": {"title": payload['title'], "deadline": payload['deadline'], "course_d": payload['course_id'],
                        "description": payload['description'], "attachments": payload['attachments'] }})
            return jsonify("Task updated")

        return jsonify("No task matching given id")

    def find_by_student(self, student_id):
        result = []
        tasks = DB.find("Tasks", {"student": student_id}).sort("created", -1)  
        for task in tasks:
            result.append(task)
        return jsonify(result)
    
    def find_by_student_and_course(self, student, course):
        result = []
        tasks = DB.find("Tasks", {"student": student, "course_id": course})
        for task in tasks:
            result.append(task)
        return jsonify(result)

