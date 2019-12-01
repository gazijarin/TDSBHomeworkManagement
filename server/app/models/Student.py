#!/usr/bin/env python
# coding=utf-8
import datetime

from app.database import DB


class Student(object):

    def __init__(self, first_name, last_name, image, email, _id):
        self._id = _id
        self.first_name = first_name
        self.image = image
        self.email = email
        self.last_name = last_name
        self.created_date = datetime.datetime.utcnow()
        self.last_sync_date = self.created_date
        self.courses = []

    def insert(self):
        if not DB.find_one("Students", {"_id": self._id}):
            DB.insert(collection='Students', data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "image": self.image,
            "created_date": self.created_date,
            "last_sync_date": self.last_sync_date,
            "courses": self.courses
        }
