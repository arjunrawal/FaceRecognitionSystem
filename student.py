
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):         #using constructor
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")


    # first Loading and resizing the image
        img1 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Student1.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

    #  to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
    # second Loading and resizing the image
        img2 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Student1.jpg")
        img2= img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

    # to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
     #third Loading and resizing the image
        img3 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Student1.jpg")
        img3 = img3.resize((600, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

    # to display the image in a label
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=600, height=130)

    #background Loading and resizing the image
        img4 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Background.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

    # to display the image in a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Roboto",35,"bold"),bg="dark blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    #creating frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
     #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Roboto",12,"bold"))
        Left_frame.place(x=10, y=10, width=760,height=580)

     #loading and resizing the image in left label
        img_left = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Student4.jpg")
        img_left = img_left.resize((750, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

    #to display the image in a left label
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=750, height=130)


    #Current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information ",font=("Roboto",12,"bold"),)
        current_course_frame.place(x=5, y=135, width=750,height=80)

        dep_label=Label(current_course_frame,text="Department",font=("Roboto",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("roboto",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","BCA","Bsc.Csit","Bit")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


    #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("Roboto",13,"bold"),bg="white")
        semester_label.grid(row=0,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,font=("Roboto",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","First Semester","Second Semester","Third Semester","Fourth Semester","Fifth Semester","Six Semester","Seven Semester","Eight Semester")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    #Class Student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("Roboto",13,"bold"),)
        Class_Student_frame.place(x=5, y=220, width=750,height=320)

    #Student id
        studentId_label=Label(Class_Student_frame,text="Student_ID :",font=("roboto",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_Student_frame,width=20,font=("roboto",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
    
    #Student name
        studentName_label=Label(Class_Student_frame,text="Student Name :",font=("roboto",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_Student_frame,width=20,font=("roboto",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #Student roll no
        roll_no_label=Label(Class_Student_frame,text="Roll No :",font=("roboto",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,width=20,font=("roboto",13,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

    #Student Date of Birth
        dob_label=Label(Class_Student_frame,text="Date Of Birth :",font=("roboto",13,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,width=20,font=("roboto",13,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Gender Of student
        gender_label=Label(Class_Student_frame,text="Gender :",font=("roboto",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

    #making choosing like options
        gender_combo=ttk.Combobox(Class_Student_frame,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Here:","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
    #Address Of student
        address_label=Label(Class_Student_frame,text="Address :",font=("roboto",13,"bold"),bg="white")
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,width=20,font=("roboto",13,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    #Contact Number
        contactNo_label=Label(Class_Student_frame,text="Contact :",font=("roboto",13,"bold"),bg="white")
        contactNo_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        contacNo_entry=ttk.Entry(Class_Student_frame,width=20,font=("roboto",13,"bold"))
        contacNo_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #student E-mail:
        email_label=Label(Class_Student_frame,text="E-mail :",font=("roboto",13,"bold"),bg="white")
        email_label.grid(row=3, column=2,padx=10, pady=5, sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
 
    #Teacher name:
        teacherName_label=Label(Class_Student_frame,text="Teacher Name :",font=("roboto",13,"bold"),bg="white")
        teacherName_label.grid(row=4, column=0,padx=10, pady=5, sticky=W)

        teacherName_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        teacherName_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
    
    #Teacher subject name:
        teacher_subject_label=Label(Class_Student_frame,text="Teacher's subject Name :",font=("roboto",13,"bold"),bg="white")
        teacher_subject_label.grid(row=4, column=2,padx=10, pady=5, sticky=W)

        teacher_subject_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        teacher_subject_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


    #radio button
        radiobtn1=ttk.Radiobutton(Class_Student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,padx=5,pady=0,column=0)

        radiobtn2=ttk.Radiobutton(Class_Student_frame,text="No Photo Sample")
        radiobtn2.grid(row=6,padx=5,pady=0,column=1)

    # Buttons Frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=760, height=130)

    # Row 1Buttons
        save_btn = Button(btn_frame, text="Save", width=15, font=("times new roman", 13, "bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=5)
       
        update_btn = Button(btn_frame, text="Update", width=15, font=("times new roman", 13, "bold"), bg="yellow", fg="black")
        update_btn.grid(row=0, column=1, padx=5, pady=5)
       
        delete_btn = Button(btn_frame, text="Delete", width=15, font=("times new roman", 13, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=5)
       
        reset_btn = Button(btn_frame, text="Reset", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)
    
     # Row 2 Buttons
        take_photo_btn = Button(btn_frame, text="Take Photo Sample", width=20, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
       
        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=20, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=2, columnspan=2, padx=5, pady=5)



#==========End of left side================



     #Right label frame  
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Roboto",12,"bold"))
        Right_frame.place(x=780, y=10, width=680,height=580)

        
     #loading and resizing the image of right frame
        img_Right = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Right1.jpg")
        img_Right = img_Right.resize((750, 130), Image.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

    #to display the image in a  right label
        Right_lbl = Label(Right_frame, image=self.photoimg_Right)
        Right_lbl.place(x=1, y=0, width=680, height=130)


    #=====Searching System=============


        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System ",font=("Roboto",13,"bold"),)
        Search_frame.place(x=5, y=135, width=710,height=70)


        search_label=Label(Search_frame,text="Search By :",font=("roboto",13,"bold"),bg="yellow",fg="blue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(Search_frame,font=("Roboto",12,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select ","Roll No ","Phone Number","StudentID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=4,sticky=W)
    
        search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4, pady=5)

        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 13, "bold"), bg="green", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4, pady=5)
        #=========== table frame===========


        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5, y=210, width=680,height=250)


        #creating scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","rollno","gender","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        



















   
        #creating object

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
