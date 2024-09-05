from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):        
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Roboto", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Loading and resizing the first image
        img_top = Image.open(r"college_images\FRthird.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Displaying the first image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Loading and resizing the second image
        img_top2 = Image.open(r"college_images\train2.png")
        img_top2 = img_top2.resize((850, 700), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        # Displaying the second image
        f_lbl = Label(self.root, image=self.photoimg_top2)
        f_lbl.place(x=650, y=55, width=850, height=700)

        # Button for face recognition
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("Roboto", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=350, y=600, width=200, height=40)

    # =============Attendance Marking============
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r") as f: 
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",") 
                name_list.append(entry[0])

            # Checking if the person is already marked present
            if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
                now = datetime.now()
                d1 = now.strftime("%D/%M/%Y")
                dtString = now.strftime("%H:%M:%S")
            with open("attendance.csv" "a") as f:
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


                

    

    # =============Face Recognition============
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            features = classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    


            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select id from Student where id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(map(str, i))  # Convert each element of 'i' to a string

                my_cursor.execute("select rollno from Student where id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(map(str, r))

                my_cursor.execute("select name from Student where id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(map(str, n))

                my_cursor.execute("select dep from Student where id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(map(str, d))

                if confidence > 77: 
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)  # Corrected method name

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        #clf = cv2.face.LBPHFaceRecognizer_create()
        clf = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

# Running the application
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
