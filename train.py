
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self, root):        
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")


        #Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Roboto", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # top Loading and resizing the image
        img_top1 = Image.open(r"college_images\train1.jpg")
        img_top1 = img_top1.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)


        #to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        #button betwn to images
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)
        


        # top 2nd Loading and resizing the image
        img_top2 = Image.open(r"college_images\train2.png")
        img_top2 = img_top2.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)


        #to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg_top2)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    #trainnning data
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
#numpy gives 88% performance for converting to array

        #================tain the classifier and save=======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Traning datasets completed!!!")

       

       



# Running the application
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
