from user import User

class Student(User):

    def __init__(self, name, registration_number, major, photos):
        super().__init__(name, photos)
        self._registration_number = registration_number
        self._major = major
