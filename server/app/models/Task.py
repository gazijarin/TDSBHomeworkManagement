import datetime

from app.database import DB
from flask import jsonify, abort


# helper function to create a datetime object
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
    hour = int(time[0][0:2])
    minute = int(time[0][3:])
    date_obj = datetime.datetime(year, month, day, hour, minute)
    return date_obj



class Task(object):

    def insert(self, payload):
        if not DB.find_one("Tasks", {"_id": payload._id}):
            DB.insert(collection='Tasks', data=payload)

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
        task = DB.find_one("Tasks", {"_id": id})
        if task:
            new_deadline = create_date(payload['date'], payload['time'])
            DB.update("Tasks", {"_id": id}, { "$set": {"title": payload.title, "deadline": payload.time, "course": payload.course,
                        "description": payload.description, "attachments": payload.attachments }})
            return jsonify("Task updated")

        return jsonify("No task matching given id")