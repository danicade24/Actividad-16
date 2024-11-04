class Course:
    def __init__(self, course_id, title, description, instructor):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.lessons = []
        self.enrolled_students = set()

    def add_lesson(self, lesson):
        if lesson.lesson_id in [l.lesson_id for l in self.lessons]:
            raise ValueError("Lección con ID ya existente.")
        self.lessons.append(lesson)

    def remove_lesson(self, lesson_id):
        self.lessons = [l for l in self.lessons if l.lesson_id != lesson_id]

    def enroll_student(self, student_id):
        self.enrolled_students.add(student_id)

    def unenroll_student(self, student_id):
        self.enrolled_students.discard(student_id)

    def summary(self):
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "lessons": [l.summary() for l in self.lessons],
            "enrolled_students": list(self.enrolled_students)
        }
