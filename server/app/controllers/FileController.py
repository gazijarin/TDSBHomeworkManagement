from app.database import DB
from flask import jsonify, make_response
from app.models.File import File

file_hanlder = File()

def upload_files(files):
    result = file_hanlder.upload(files)
    return result

def get_file(id):
    result = file_hanlder.get(id)
    return result


