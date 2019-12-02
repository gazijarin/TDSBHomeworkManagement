from app.models.Task import Task
from flask import jsonify
import uuid
import datetime

task = Task()

def create_date(date, time):
    date = date.split()
    time = time.split()
    month_dict = {"Jan": 1, "Feb": 2, "Mar": 3,
                    "Apr":4, "May": 5, "June": 6,
                    "July": 7, "Aug": 8, "Sept": 9,
                    "Oct": 10, "Nov": 11, "Dec": 12}
    day = int(date[0])
    month = month_dict[date[1]]
    year = int(date[2])
    if time[0] == '0:00':
        hour = 0
        minute = 0
    else:
        hour = int(time[0][0:2])
        minute = int(time[0][3:])
    date_obj = datetime.datetime(year, month, day, hour, minute)
    return date_obj

def post(title, deadline, course_id, description, attachments, student, grade, progress):
    result = task.insert({"title":title,"deadline":deadline, "course_id": course_id,
         "description": description, "attachments":attachments,"student": student, "_id":str(uuid.uuid4()),
                          "created": datetime.datetime.utcnow(), "grade": grade, "progress": progress})

    return result

def get(id):
    return task.get(id)

def delete(id):
    return task.delete(id)

def update(title, date, time, course_id, description, attachments, _id, grade, progress):
    deadline = create_date(date, time)
    return task.update(_id, {"title": title, "deadline": deadline, "course_id": course_id,
                 "description": description, "attachments": attachments, "_id": _id,
                  "grade": grade, "progress": progress})

def get_by_student(id):
    return task.find_by_student(id)

def get_by_student_and_course(student, course):
    return task.find_by_student_and_course(student,course)