
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Button
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        
        #variables
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()
        
        
        #bg img
        img_down = Image.open(r"college_images\bg2.jpg")
        img_down = img_down.resize((1530, 710), Image.LANCZOS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        bg_img_down = Label(self.root, image=self.photoimg_down)
        bg_img_down.place(x=0, y=0, width=1530, height=790)
            
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("georgia", 25, "bold"), bg="white", fg="maroon")
        register_lbl.place(x=20,y=20)

        
        #label and entry
        fname=Label(frame,text="First Name:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("courier",15,"bold"))
        fname_entry.place(x=50, y=130,width=250)
        
        
        l_name=Label(frame,text="Last Name:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("courier",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        
        contact=Label(frame,text="Contact:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("courier",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="E-mail:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("courier",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        
        security_q=Label(frame,text="Select Security Questions:",font=("georgia",13,"bold"),bg="white",fg="blue")
        security_q.place(x=50,y=240)
        
        self_combo_security_q=ttk.Combobox(frame,textvariable=self.var_security_q,font=("courier",12,"bold"),state="readonly")
        self_combo_security_q["values"]=("Select","Your Birth Place?","Your Favourite dishes?","Your Favourite Languages?")
        self_combo_security_q.place(x=50,y=270,width=250)
        self_combo_security_q.current(0)
        
        security_a=Label(frame,text="Security Answer:",font=("georgia", 15, "bold"),bg="white",fg="blue")
        security_a.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_a,font=("georgia",13,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        password=Label(frame,text="Password:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        password.place(x=50,y=310)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("courier",15,"bold"))
        self.txt_password.place(x=50,y=340,width=250)
        
        
        confirm_password=Label(frame,text="Confirm Password:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        confirm_password.place(x=370,y=310)
        
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("courier",15,"bold"))
        self.txt_confirm_password.place(x=370,y=340,width=250)
        
        
        #check button
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("courier",12,"bold"),bg="white", fg="blue",onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=390)
        
        #button
        img=Image.open(r"college_images\register1.jpg")
        img=img.resize((200,80),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=0,y=420,width=200)
        
        
        
        img_login=Image.open(r"college_images\loginn.jpg")
        img_login=img_login.resize((200,80),Image.LANCZOS)
        self.photoimage_login=ImageTk.PhotoImage(img_login)
        b1=Button(frame,image=self.photoimage_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
        
        
#function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password and Confirm Password must be same!!")
            
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions!!")    
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist. Please try another email address.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    
                    
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_q.get(),
                    self.var_security_a.get(),
                    self.var_password.get()
                   
                       
                ))
       
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully!!")
       
       
       
       
       
        #creating objects

if __name__ == "__main__":
          root = Tk()
          obj = Register(root)
          root.mainloop()
        