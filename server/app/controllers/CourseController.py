from app.models.Course import Course
import uuid


def post(name, instructor):
    new_course = Course(name=name,instructor=instructor,_id=str(uuid.uuid4()))
    new_course.insert()


