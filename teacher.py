from user import User

class Teacher(User):
    
    def __init__(self, name, department, face_encodings):
        super().__init__(name, face_encodings)
        self._department = department
    