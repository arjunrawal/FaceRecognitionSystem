from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  # You are importing this but not using it in this class
import cv2  # Similarly, you import cv2 but don't use it here

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        
        # Title
        title_lbl = Label(self.root, text="H E L P   D E S K", font=("Georgia", 35, "bold"), bg="#f0f0f0", fg="#4a4a4a")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # First image
        img_top = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\help.png")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
       
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        help_label1 = Label(f_lbl, text="E-mail: rabinbhattarai44@gmail.com", font=("Georgia", 20, "bold"), bg="white", fg="blue")
        help_label1.place(x=530, y=645)
        
        help_label2 = Label(f_lbl, text="E-mail: arjunrawal67890@gmail.com", font=("Georgia", 20, "bold"), bg="white", fg="blue")
        help_label2.place(x=530, y=680)

# Creating objects
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
