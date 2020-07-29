import face_recognition
import cv2
import numpy as np

class Lab:
    __users = []
    __camera = cv2.VideoCapture(0)

    def authenticate(self):
        known_face_encodings = [self._users[0]._face_encodings]
        known_face_names = [self._users[0]._name]

        while True:
            ret, frame = self.camera.read()

            
            rgb_frame = frame[:, :, ::-1]

            
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()

    def to_monitor(self):
        pass
    
    def register_user(self, user):
        self._users.append(user)

    def get_face_encodings(self):
        ret, frame = self.__camera.read()
        face_encodings = face_recognition.face_encodings(frame)[0]
        return face_encodings
    
    def imprime_primeiro(self):
        print(self._users[0]._name)