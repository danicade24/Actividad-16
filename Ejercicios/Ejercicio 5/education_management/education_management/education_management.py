from course import Course
from lesson import Lesson
from user import User

class EducationManagement:
    def __init__(self):
        self.courses = {}
        self.users = {}

    def manage_courses(self, action, course=None):
        if action == "add" and course:
            self.courses[course.course_id] = course
        elif action == "delete" and course:
            self.courses.pop(course.course_id, None)

    def manage_users(self, action, user=None):
        if action == "add" and user:
            self.users[user.user_id] = user

    def generate_reports(self):
        return {
            "total_courses": len(self.courses),
            "total_users": len(self.users)
        }
