
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Face_Recognition:
    def __init__(self, root):        
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")


        #Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Roboto", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # second Loading and resizing the image
        img_top = Image.open(r"college_images\FRthird.jpg")
        img_top= img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)


        # to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        
        # top 2nd Loading and resizing the image
        img_top2 = Image.open(r"college_images\train2.png")
        img_top2 = img_top2.resize((950, 700), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)


        #to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg_top2)
        f_lbl.place(x=650, y=55, width=850, height=700)


        #button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog,cursor="hand2", font=("Roboto", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=350, y=600, width=200, height=40)


    #=============face recognition========
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from Student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollno from Student where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from Student where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence > 77: 
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face:",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



# Running the application
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
