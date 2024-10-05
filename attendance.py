from tkinter import *
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        
        #variables
        self.var_attend_id=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
        
         # First image
        img1 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\attendance5.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

       
        lbl = Label(self.root, image=self.photoimg1)
        lbl.place(x=0, y=0, width=500, height=130)
        
        
        
         # Second Image
        img2 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\attendance4.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Optionally, you might want to display the image in a label
        lbl = Label(self.root, image=self.photoimg2)
        lbl.place(x=500, y=0, width=500, height=130)
        
        
        
         # Third Image
        img3 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\attendance6.jpg")
        img3 = img3.resize((600, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Optionally, you might want to display the image in a label
        lbl = Label(self.root, image=self.photoimg3)
        lbl.place(x=1000, y=0, width=600, height=130)
        
          # Loading and resizing the image for background images
        img4 = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Background.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Optionally, you might want to display the image in a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img, text="A T T E N D A N C E   M A N A G E M E N T   S Y S T E M",font=("georgia",35,"bold"),bg="#f0f0f0", fg="#4a4a4a")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
         #creating frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=90,width=1480,height=500)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("georgia",12,"bold"))
        Left_frame.place(x=10, y=10, width=730,height=450)
        
        img_left = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\Student4.jpg")
        img_left= img_left.resize((750, 130), Image.LANCZOS)
        self.photoimg_left =ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)
        
        
        #creating frame
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=350)
        
        #labeled entry
         #Attendance ID
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("georgia",13,"bold"),bg="white")
        attendanceId_label.grid(row=0, column=0,padx=10, pady=5, sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_id,font=("courier",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
       
        
         #roll
        rollLabel_label=Label(left_inside_frame,text="Roll No:",font=("comicsansns",13,"bold"),bg="white")
        rollLabel_label.grid(row=0, column=2,padx=4, pady=4)
        
        atten_roll=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_roll,font=("courier",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=5,)
                
       
         #name
        nameLabel=Label(left_inside_frame,text="Name:",font=("georgia",13,"bold"),bg="white")
        nameLabel.grid(row=1, column=0)
        
        atten_name=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_name,font=("courier",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
        
        
        
        
        
        
          #Department
        depLabel=Label(left_inside_frame,text="Department:",font=("georgia",13,"bold"),bg="white")
        depLabel.grid(row=1, column=2,padx=4, pady=8)
        
        atten_dep=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_dep,font=("courier",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        
        
        
         #Time
        timeLabel=Label(left_inside_frame,text="Time:",font=("georgia",13,"bold"),bg="white")
        timeLabel.grid(row=2, column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_time,font=("courier",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
         #Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("georgia",13,"bold"),bg="white")
        dateLabel.grid(row=2, column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_date,font=("courier",12,"bold"))
        atten_date.grid(row=2,column=3,pady=7)
        
        
        #attendance status
        
        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("georgia",13,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)
        
        self.atten_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("courier",12,"bold"),state="readonly",width=20)
        self.atten_combo["values"]=("Status","Present","Absent")
        self.atten_combo.current(0)
        self.atten_combo.grid(row=3,column=1,pady=8)
        
        
        #buttons frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0, y=225, width=750, height=100)
        
        imp_btn=Button(btn_frame, text="Import Csv",command=self.importCsv, width=15,font=("arial",13,"bold"),bg="green",fg="white")
        imp_btn.grid(row=0,padx=10, pady=5,column=0)
       
       
        exp_btn=Button(btn_frame, text="Export Csv",command=self.exportCsv,width=15,font=("arial",13,"bold"),bg="maroon",fg="white")
        exp_btn.grid(row=0,padx=10, pady=6, column=1)
        
       
        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,width=15,font=("arial",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,padx=10, pady=5,column=2)
        
        
        
        #Right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Record",font=("georgia",13,"bold"))
        Right_frame.place(x=750, y=10, width=710,height=580)
        
         
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)
        
        #scroll bar table
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

            

      
      #fetch data
        
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)
        
        #import csv data
    def importCsv(self):
      global mydata
      mydata.clear()
      fln = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Open CSV",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
        parent=self.root
    )
      with open(fln) as myfile:
       csvread=csv.reader(myfile,delimiter=",")
       for i in csvread:
        mydata.append(i)
      self.fetchData(mydata)
      
      #for export csv  data
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No Data found to export",parent=self.root)
          return False
        
        
        fln = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Open CSV",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
        parent=self.root
    )
        with open(fln,mode="w",newline="")as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+ "Successfully")
          
      except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
      
      
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])
        
        
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
          
     
     
     
     

     
     
        
#creating objects

if __name__ == "__main__":
          root = Tk()
          obj = Attendance(root)
          root.mainloop()        
        
