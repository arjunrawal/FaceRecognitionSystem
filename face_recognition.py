
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
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("Roboto", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=350, y=600, width=200, height=40)

















# Running the application
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
