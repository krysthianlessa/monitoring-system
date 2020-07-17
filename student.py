from user import User

class Student(User):

    def __init__(self, name, registration_number, major, face_encodings):
        super().__init__(name, face_encodings)
        self._registration_number = registration_number
        self._major = major
