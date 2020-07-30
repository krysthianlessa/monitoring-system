class User:

    __slots__ = ['_name', '_last_name', '_email', '_limite']

    def __init__(self, name, last_name, email, face_encodings):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.face_encodings = face_encodings
    