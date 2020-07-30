class User:

    __slots__ = ['_name', '_last_name', '_email', '_limite', '_face_encodings']

    def __init__(self, name, last_name, email, face_encodings):
        self._name = name
        self._last_name = last_name
        self._email = email
        self._face_encodings = face_encodings
    