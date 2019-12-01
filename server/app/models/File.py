from app.database import DB
from flask import jsonify

class File(object):

    def upload(self, files):
        files_result = []
        for file in files:
            file_id = DB.save_file(file, file.filename)
            file_obj = {"_id": str(file_id), "filename": file.filename}
            files_result.append(file_obj)
        return jsonify(files_result)

    def get(self, id):
        file = DB.get_file(id)
        return file
