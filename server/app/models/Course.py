#!/usr/bin/env python
# coding=utf-8
import datetime

from app.database import DB


class Course(object):

    def __init__(self, name, instructor, _id):
        self._id = _id
        self.name= name
        self.instructor = instructor
        self.students = []
        #add attributes

    def insert(self):
        if not DB.find_one("Courses", {"_id": self._id}):
            DB.insert(collection='Courses', data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "instructor": self.instructor,
            "students": self.students           
        }
        