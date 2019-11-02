#!/usr/bin/env python
# coding=utf-8
import datetime

from app.database import DB


class Student(object):

    def __init__(self, first_name, last_name, _id):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.created_date = datetime.datetime.utcnow()
        #add attributes

    def insert(self):
        if not DB.find_one("Students", {"_id": self._id}):
            DB.insert(collection='Students', data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_date": self.created_date
        }
