class Lesson:
    def __init__(self, lesson_id, title, content, duration):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content
        self.duration = duration

    def update_content(self, new_content):
        if not new_content.strip():
            raise ValueError("El contenido no debe estar vacío.")
        self.content = new_content

    def update_duration(self, new_duration):
        if new_duration <= 0:
            raise ValueError("La duración debe ser un valor positivo.")
        self.duration = new_duration

    def summary(self):
        return {
            "lesson_id": self.lesson_id,
            "title": self.title,
            "content": self.content,
            "duration": self.duration
        }
