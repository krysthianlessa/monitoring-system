from user import User

class Teacher(User):
    
    def __init__(self, name, department, photos):
        super().__init__(name, photos)
        self._department = department
    