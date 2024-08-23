
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self, root):         
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")




    #=================variables==================
        self.var_dep=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_teacherName=StringVar()
        self.var_teacherSuject=StringVar()
        self.var_photo=StringVar()
        
    




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


    #Department
        dep_label=Label(current_course_frame,text="Department",font=("Roboto",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

    # Department Combobox
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("roboto", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "BCA", "BSc. CSIT", "BIT")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


    #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("Roboto",13,"bold"),bg="white")
        semester_label.grid(row=0,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Roboto",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","First Semester","Second Semester","Third Semester","Fourth Semester","Fifth Semester","Six Semester","Seven Semester","Eight Semester")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


    #Class Student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("Roboto",13,"bold"),)
        Class_Student_frame.place(x=5, y=220, width=750,height=320)


    #Student id
        studentId_label=Label(Class_Student_frame,text="Student_ID :",font=("roboto",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_id,width=20,font=("roboto",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
    

    #Student name
        studentName_label=Label(Class_Student_frame,text="Student Name :",font=("roboto",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_name,width=20,font=("roboto",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


    #Student roll no
        roll_no_label=Label(Class_Student_frame,text="Roll No :",font=("roboto",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_rollno,width=20,font=("roboto",13,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


    #Student Date of Birth
        dob_label=Label(Class_Student_frame,text="Date Of Birth :",font=("roboto",13,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("roboto",13,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)



    #Gender Of student
        gender_label=Label(Class_Student_frame,text="Gender :",font=("roboto",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

    #making choosing like options
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Here:","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
    #Address Of student
        address_label=Label(Class_Student_frame,text="Address :",font=("roboto",13,"bold"),bg="white")
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("roboto",13,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


    #Contact Number
        contactNo_label=Label(Class_Student_frame,text="Contact :",font=("roboto",13,"bold"),bg="white")
        contactNo_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        contacNo_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_contact,width=20,font=("roboto",13,"bold"))
        contacNo_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


    #student E-mail:
        email_label=Label(Class_Student_frame,text="E-mail :",font=("roboto",13,"bold"),bg="white")
        email_label.grid(row=3, column=2,padx=10, pady=5, sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
 

    #Teacher name:
        teacherName_label=Label(Class_Student_frame,text="Teacher Name :",font=("roboto",13,"bold"),bg="white")
        teacherName_label.grid(row=4, column=0,padx=10, pady=5, sticky=W)

        teacherName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacherName,width=20,font=("times new roman",13,"bold"))
        teacherName_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
    

    #Teacher subject name:
        teacher_subject_label=Label(Class_Student_frame,text="Teacher's subject Name :",font=("roboto",13,"bold"),bg="white")
        teacher_subject_label.grid(row=4, column=2,padx=10, pady=5, sticky=W)

        teacher_subject_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacherSuject,width=20,font=("times new roman",13,"bold"))
        teacher_subject_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


    #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_photo,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,padx=5,pady=5,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_photo,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,padx=5,pady=5,column=1)


    # Buttons Frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=760, height=130)


    # Row 1Buttons
        save_btn = Button(btn_frame, command=self.add_data, text="Save",cursor="hand2", width=15, font=("times new roman", 13, "bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=5)
       
        update_btn = Button(btn_frame, text="Update",command=self.Update_data,cursor="hand2", width=15, font=("times new roman", 13, "bold"), bg="yellow", fg="black")
        update_btn.grid(row=0, column=1, padx=5, pady=5)
       
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,cursor="hand2", width=15, font=("times new roman", 13, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=5)
       
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,cursor="hand2", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)
    
     # Row 2 Buttons
        take_photo_btn = Button(btn_frame, text="Take Photo Sample",cursor="hand2", width=20, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
       
        update_photo_btn = Button(btn_frame, text="Update Photo Sample",cursor="hand2", width=20, font=("times new roman", 13, "bold"), bg="blue", fg="white")
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
    
        search_btn = Button(Search_frame, text="Search", cursor="hand2",width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4, pady=5)

        showAll_btn = Button(Search_frame, text="Show All", cursor="hand2", width=12, font=("times new roman", 13, "bold"), bg="green", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4, pady=5)



    #=========== table frame===========


        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5, y=210, width=670,height=350)


    #creating scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","sem","id","name","rollno","dob","gender","address","email","contact","teacher","teacherSubject","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

     # Define column headers
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("teacherSubject", text="Teacher's Subject Name")
        self.student_table.heading("photo", text="photo")
        self.student_table["show"]="headings"   
    
    # Set column widths
        self.student_table.column("dep", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("teacherSubject", width=100)
        self.student_table.column("photo", width=150)


    # Pack Treeview to ensure it fits correctly with the scrollbars
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #=============== function declaration =======
    # Function declaration within the Student class
    def add_data(self):
            if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
    # Additional logic can be added here to store data
                    conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                    """INSERT INTO student (dep, semester, id, name, rollno, dob, gender, address, email, contact, teacherName, teacherSubject, photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_rollno.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.var_teacherName.get(),
                    self.var_teacherSuject.get(),
                    self.var_photo.get()
                         ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details have been added successfully")
                except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #===========fetch data==============

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #==============get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_semester.set(data[1]),
        self.var_id.set(data[2]),
        self.var_name.set(data[3]),
        self.var_rollno.set(data[4]),
        self.var_dob.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_address.set(data[7]),
        self.var_email.set(data[8]),
        self.var_contact.set(data[9]),
        self.var_teacherName.set(data[10]),
        self.var_teacherSuject.set(data[11]),
        self.var_radio1.set(data[12])

        

    #=====update function=============
    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update?",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,semester=%s,name=%s,rollno=%s,dob=%s,gender=%s,address=%s,email=%s,contact=%s,teacherName=%s,teacherSubject=%s,photo=%s where id=%s",(
                    
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_rollno.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.var_teacherName.get(),
                    self.var_teacherSuject.get(),
                    self.var_radio1.get(),
                    self.var_id.get()
                         ))



                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Students details successfully update Completed",parent=self.root)        
                conn.commit()
                self.fetch_data()
                conn.close()


            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



#==========delete function========
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student ",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            


    #============reset function========
    def reset_data(self):
        self.var_dep.set("Selecct Department")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_rollno.set("")
        self.var_dob.set("")
        self.var_gender.set("Male")
        self.var_address.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_teacherName.set("")
        self.var_teacherSuject.set("")
        self.var_photo.set("")
        self.var_radio1.set("")
    



   
        #creating object

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
