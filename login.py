from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
import hashlib
import re
import pyttsx3


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
        



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root2=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.var_email=tk.StringVar()
        self.var_password = tk.StringVar()

    
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[1].id)
        
        img_lo = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\log7.jpg")
        img_lo = img_lo.resize((1530, 710), Image.LANCZOS)
        self.photoimg_lo = ImageTk.PhotoImage(img_lo)

        bg_img_lo = Label(self.root, image=self.photoimg_lo)
        bg_img_lo.place(x=0, y=0, width=1530, height=790)
        
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\login4.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
         
        lblimg1 = Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)                 

        get_str=Label(frame,text="Login",font=("georgia", 25, "bold"), bg="white", fg="maroon")
        get_str.place(x=120,y=100)

    #label
    
        username=lbl=Label(frame,text="Username",font=("georgia", 15, "bold"), bg="white", fg="blue")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("courier",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        
        password=lbl=Label(frame,text="Password",font=("georgia", 15, "bold"), bg="white", fg="blue")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("courier",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)
        
        
         # Show/Hide password checkbox
        self.show_password = tk.IntVar()
        self.show_password_check = tk.Checkbutton(
            frame, text="Show Password", variable=self.show_password, 
            command=self.toggle_password, font=("courier", 10, "bold"), bg="white"
        )
        self.show_password_check.place(x=40, y=280)

        
        
        #icon images
        img2=Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\icon3.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
         
        lblimg2 = Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)                 

        
        img3=Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\passicon2.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
         
        lblimg3 = Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)                 

    #login button

        loginbtn=Button(frame,command=self.login,text="Login",font=("courier",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
        loginbtn.place(x=110,y=310,width=120,height=35)
        
        #register button
        
        registerbtn=Button(frame,text="Sign Up",command=self.register_window,font=("courier",12,"bold"),borderwidth=0,fg="black",bg="white",activebackground="green")
        registerbtn.place(x=0,y=350,width=160)

      #forgot password
        forgotbtn=Button(frame,text="Forget Password?",command=self.forgot_password_window,font=("courier",12,"bold"),borderwidth=0,fg="black",bg="white",activebackground="maroon")
        forgotbtn.place(x=10,y=375,width=160)
    
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)  


    def show_message(self, title, message):
        messagebox.showerror(title, message)

        
          
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            self.engine.say("All fields are required")
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields are required!!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                my_cursor = conn.cursor()

                # Fetch the email and password from the database
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))

                row = my_cursor.fetchone()

                if row is None:
                    self.engine.say("Invalid Username or Password")
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    self.engine.say("Welcome to our Facial Recognition Attendance System Software")
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Welcome to our Facial Recognition Attendance System Software!")
                   # Optionally open the main system window after successful login
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)

                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}")

            
    
    def toggle_password(self):
        """Toggle the password visibility."""
        if self.show_password.get():
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    
    
    #forget password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            self.engine.say("Please enter the email address for reset the password")
            self.engine.runAndWait()
            self.show_message("Error","Please enter the email address for reset the password")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
                my_cursor = conn.cursor()    
                query=("select * from register where email=%s")
                value=(self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
            
                if row==None:
                    self.engine.say("Please enter the valid username")
                    self.engine.runAndWait()
                    messagebox.showerror("My Error","Please enter the valid username")
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")    
                    
                    l=Label(self.root2,text="Forget Password !!",font=("georgia", 20, "bold"), bg="white", fg="red")
                    l.place(x=0,y=10,relwidth=1)
                
                
                    security_q=Label(self.root2,text="Select Security Questions:",font=("georgia",13,"bold"),fg="blue")
                    security_q.place(x=50,y=80)
                
                    self.combo_security_q=ttk.Combobox(self.root2,font=("courier",13,"bold"),state="readonly")
                    self.combo_security_q["values"]=("Select","Your Birth Place?","Your Favourite dishes?","Your Favourite Languages?")
                    self.combo_security_q.current(0)
                    self.combo_security_q.place(x=50,y=110,width=250)
                    
                    security_a=Label(self.root2,text="Security Answer:",font=("georgia", 13, "bold"),fg="blue")
                    security_a.place(x=50,y=150)
                    
                    self.txt_security=ttk.Entry(self.root2,font=("georgia",13,"bold"))
                    self.txt_security.place(x=50,y=180,width=250)
                        
                        
                    new_password=Label(self.root2,text="New Password:",font=("georgia", 13, "bold"),fg="blue")
                    new_password.place(x=50,y=220)
                    
                    self.txt_new_password=ttk.Entry(self.root2,font=("georgia",13,"bold"),show="*")
                    self.txt_new_password.place(x=50,y=250,width=250)
                            
                    btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("courier",15,"bold"),fg="white",bg="green")
                    btn.place(x=100,y=290,width=130)
                    
            except Exception as es:
                self.show_message("Error", f"Error Due to: {str(es)}", "error")
        
                
                
            #reset password
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif  self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the Answer",parent=self.root2)  
        elif  self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password!!",parent=self.root2)  
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and security_q=%s and security_a=%s")
            vale = (self.txtuser.get(), self.combo_security_q.get(), self.txt_security.get())
            my_cursor.execute(qury,vale)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter The Correct Answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s") 
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)   
            
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset successfully, Please login with new Password",parent=self.root2)    
                self.root2.destroy()
               
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        #text to speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[1].id)
        
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
        img_down = Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\bg2.jpg")
        img_down = img_down.resize((1530, 710), Image.LANCZOS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        bg_img_down = Label(self.root, image=self.photoimg_down)
        bg_img_down.place(x=0, y=0, width=1530, height=790)
            
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("georgia", 25, "bold"), bg="white", fg="maroon")
        register_lbl.place(x=20,y=20)

        
        #label and entry
#label and entry
        fname=Label(frame,text="First Name:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("courier",15,"bold"))
        fname_entry.place(x=50, y=130,width=250)

        #bind and validation register
        validate_name=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_name,'%P'))

        l_name=Label(frame,text="Last Name:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        l_name.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("courier",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)


        #callback and validation register
        validate_name=self.root.register(self.checkname)
        lname_entry.config(validate='key',validatecommand=(validate_name,'%P'))


        contact=Label(frame,text="Contact:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        contact.place(x=50,y=170)

        entry_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("courier",15,"bold"))

        #callback and validation register
        validate_contact = self.root.register(self.checkcontact)
        entry_contact.config(validate='key', validatecommand=(validate_contact, '%P'))
        entry_contact.place(x=50, y=200, width=250)

        
        email=Label(frame,text="E-mail:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        email.place(x=370,y=170)
        
        txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("courier",15,"bold"))
        txt_email.place(x=370,y=200,width=250)
        
        
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
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("courier",15,"bold"),show="*")
        self.txt_password.place(x=50,y=340,width=250)
        
        
        confirm_password=Label(frame,text="Confirm Password:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        confirm_password.place(x=370,y=310)
        
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("courier",15,"bold"),show="*")
        self.txt_confirm_password.place(x=370,y=340,width=250)
        
        
        #check button
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("courier",12,"bold"),bg="white", fg="blue",onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=390)
        
        #button
        img=Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\register1.jpg")
        img=img.resize((200,80),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=0,y=420,width=200)
        
        
        
        img_login=Image.open(r"C:\Users\aaaar\Desktop\FaceRecognitionSystem\college_images\loginn.jpg")
        img_login=img_login.resize((200,80),Image.LANCZOS)
        self.photoimage_login=ImageTk.PhotoImage(img_login)
        b1=Button(frame,image=self.photoimage_login,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
        
        
#fun declaration
    def register_data(self):
        conn=None
        try:
             # Validate required fields
            if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_q.get() == "Select":
                
                self.engine.say("All fields are required")
                self.engine.runAndWait()
                messagebox.showerror("Error", "All fields are required!")
                return
              # Validate password matching
            password = self.var_password.get()
            confirm_password = self.var_confirm_password.get()
            if password != confirm_password:
                self.engine.say("Password and Confirm Password must be the same")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Password and Confirm Password must be the same!")
                return  # Keep the form open for correction
        
        # Validate terms and conditions checkbox
            if self.var_check.get() == 0:
                self.engine.say("Please agree to the terms & conditions")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please agree to the terms & conditions!")
                return
        
        # Validate email and password using your helper methods
            if not self.checkemail(self.var_email.get()) or not self.checkpassword(self.var_password.get()):
                
                return
        
           # Final contact validation in the register_data method
            if not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Invalid Entry", "Contact number must be numeric and must be 10 digits!!")
                return
            

            conn=mysql.connector.connect(host="localhost", username="root", password="sql123", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist. Please try another email address.")
                return
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
            messagebox.showinfo("Success", "Registered Successfully!")
            
            self.root.destroy()  # Close the registration window after successful registration
            
          
        
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {str(err)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")    
            
        finally:
            if conn is not None and conn.is_connected():    
                conn.close()
                
                
                
    def validate_signup(self):
        try:
            # Example of checking if all fields are filled
            if not self.username_entry.get() or not self.password_entry.get() or not self.email_entry.get():
                raise ValueError("All fields are required")
            
            # Example of checking email validity
            if "@" not in self.email_entry.get():
                raise ValueError("Invalid email format")
            
            # Add more validation logic as needed

            # If everything is correct, proceed with the signup logic
            self.signup_user()

        except ValueError as ve:
            messagebox.showerror("Validation Error", str(ve))
        
        except Exception as e:
            # Catch other unexpected errors
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))

    def signup_user(self):
        # Code for handling signup (database insertion etc.)
        pass

    def signup_button_clicked(self):
        self.validate_signup()

   
    #validation for fname and last name
    def checkname(self,name):
        if name.isalpha():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror("Invalid",'Not Allowed'+name[-1])
            
     #check contact validation
    # Contact validation - restrict to digits and allow backspace
    def checkcontact(self, contact):
        if contact.isdigit() or contact == "":
            return True
        else:
            return False  # Prevent entry of non-digit characters

     
      #check password validation
    def checkpassword(self,password):
        if len(password)>=6 and len(password)<=21:
            if re.match(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{6,21}$", password):
    
                return True
            else:
                messagebox.showinfo("invalid","Enter Valid Password(Example:Hari@5432#)")
                return False
        else:
            messagebox.showerror("Invalid","Minimum 6 character required")
            return False
        
        
      #check password validation
    def checkemail(self,email):
        if len(email)>7:
            if re.match(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):

                return True
            else:
                messagebox.showwarning("Alert","Invalid email Please enter Valid emailaddress(Example:rabinbhattarai44@gmail.com)")
                return False
        else:
            messagebox.showinfo("Invalid","Email length is too small please enter a valid email address(Example:rabinbhattarai44@gmail.com)")
            return False 
        
    def clear_form(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_security_q.set("")
        self.var_security_a.set("")
        self.var_password.set("")
        self.var_confirm_password.set("")
        self.var_check.set(0)



   



    def return_login(self):
        self.root.destroy()
    
            
            
            
    
    
    
        
        
        
        
#creating objects

if __name__ == "__main__":
    main()