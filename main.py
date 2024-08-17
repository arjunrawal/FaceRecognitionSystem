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

        # background to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=550, height=130)

          #background Loading and resizing the image
        img4 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Background.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # to display the image in a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSYTEM SOFTWARE",font=("Roboto",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

          #Student button
        img5 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button1.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Student Details",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)

        #Detecting face
        img6 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button2.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Face Detector",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Attendance Face button
        img7 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button3.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img, image=self.photoimg7,cursor="hand2")
        b1.place(x=850,y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Attendance",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=850,y=300,width=220,height=40)


         #Help Desk  face button 
        img8 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button4.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img, image=self.photoimg8,cursor="hand2")
        b1.place(x=1200,y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Help Desk",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1200,y=300,width=220,height=40)


        #Train Data 
        img9 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button5.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img, image=self.photoimg9,cursor="hand2")
        b1.place(x=100,y=400,width=220,height=220)

        b1_1=Button(bg_img, text="Train Data",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=600,width=220,height=40)


        #Photos
        img10 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button6.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img, image=self.photoimg10,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img, text="Photos",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)


        #Developer Button
        img12 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button7.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1=Button(bg_img, image=self.photoimg12,cursor="hand2")
        b1.place(x=850,y=400,width=220,height=220)

        b1_1=Button(bg_img, text="Developer",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=850,y=600,width=220,height=40)

        #Exit 
        img11 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Button8.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img, image=self.photoimg11,cursor="hand2")
        b1.place(x=1200,y=400,width=220,height=220)

        b1_1=Button(bg_img, text="Exit",cursor="hand2",font=("Roboto",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1200,y=600,width=220,height=40)

        


        
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
