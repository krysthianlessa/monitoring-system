from data_base import DataBase

class User:

    __slots__ = ['_name', '_last_name', '_email', '_limite', '_face_encodings']

    def __init__(self, name, last_name, email, face_encodings):
        self._name = name
        self._last_name = last_name
        self._email = email
        self._face_encodings = face_encodings
    
    def insert_user(self):
        from datetime import datetime

        data_base = DataBase()
        try:

            cursor = data_base.connection.cursor()

            cursor.execute(
                """INSERT INTO users (name, last_name, email, face_encodings, created_in) 
                VALUES (?,?,?,?,?)""", 
                (self._name, self._last_name, self._email, self._face_encodings, datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
            )

            data_base.connection.commit()
            cursor.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"