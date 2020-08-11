import sqlite3
import numpy as np
import io

class DataBase():
    
    def __init__(self):
        sqlite3.register_adapter(np.ndarray, self.adapt_array)
        sqlite3.register_converter("ARRAY", self.convert_array)
        self.connection = sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES)
        print("Opened database successfully")

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''
            CREATE TABLE users (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                last_name TEXT,
                email TEXT,
                face_encodings ARRAY,
                created_in DATE NOT NULL);
            ''')
        
            self.connection.commit()
            cursor.close()

            return "Table created successfully"
        except:
            return "Table already exist"

    
    def adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)