from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):         #using constructor
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")

        # first Loading and resizing the image
        img1 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Second.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        #  to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
         # second Loading and resizing the image
        img2 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\First.jpg")
        img2= img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
         #third Loading and resizing the image
        img3 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Second.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)
        
        
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
