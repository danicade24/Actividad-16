class User:
    def __init__(self, user_id, name, email, password, role):
        if role not in ["student", "instructor"]:
            raise ValueError("El rol debe ser 'student' o 'instructor'.")
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.enrolled_courses = set()

    def enroll_course(self, course_id):
        self.enrolled_courses.add(course_id)

    def complete_course(self, course_id):
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)

    def summary(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "enrolled_courses": list(self.enrolled_courses)
        }
