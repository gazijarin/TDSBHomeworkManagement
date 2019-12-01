#!/usr/bin/env python
# coding=utf-8
import datetime

from app.database import DB
from flask import jsonify, abort, request



class Student(object):

    def insert(self, payload):
        if not DB.find_one("Students", {"_id": payload['_id']}):
            DB.insert(collection='Students', data=payload)

    def get(self, id):
        student = DB.find_one("Students", {"_id": id})
        if student:
            return jsonify(student)
        abort(404)

