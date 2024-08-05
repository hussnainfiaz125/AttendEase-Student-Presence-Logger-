from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk ,ImageFilter
from tkinter import messagebox
import tkinter
import random
import time
import datetime
import mysql.connector
import os
from student import student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
import uuid

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Login")

        self.bg = ImageTk.PhotoImage(file=r"Images\login_bg.jpg") 
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open(r"Images\1_btn.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.Photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.Photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=180,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=120)

        # label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=165)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        username_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=235)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)

        #  ======= Icon Images =======
        img2=Image.open(r"Images\2_btn.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.Photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.Photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=550,y=333,width=25,height=25)

        img3=Image.open(r"Images\3_btn.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.Photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.Photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=550,y=405,width=25,height=25)

        # LoginButton
        img5=Image.open(r"images\login_btn.png")
        img5=img5.resize((120,35),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        loginbtn=Button(frame,image=self.photoimg5,cursor="hand2",command=self.login,borderwidth=0,activebackground="black",bg="black")
        loginbtn.place(x=110,y=310,width=120,height=35)

        # RegisterButton
        registerbtn=Button(frame,text="New User Register",cursor="hand2",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=360,width=160)

        # ForgetPassBtn
        forgetpassbtn=Button(frame,text="Forget Password",cursor="hand2",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=383,width=160 )

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)
                my_cursor = conn.cursor()
                
                query = "SELECT * FROM register WHERE email=%s AND password=%s"
                values = (self.txtuser.get(), self.txtpass.get())
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid User Name And Password")
                else:
                    open_main = messagebox.showinfo("Welcome", "Welcome To Face Recognition Attendance System")
                    if open_main:
                        # Capture the teacher_id
                        self.current_teacher_id = row[my_cursor.column_names.index('teacher_id')]
                        # Close the current login window
                        self.root.destroy()
                        # Pass current_teacher_id to open_face_recognition_system
                        self.open_face_recognition_system(self.current_teacher_id)

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            

    # ======= Reset Password =======
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","select security  question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="fras",port=3307)
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)
                self.root2.destroy()

    # ======= Forget Password Window =======
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="fras",port=3307)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)                     

            if row==None:
                messagebox.showerror("Error","Please Enter the valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgte Password")
                self.root2.geometry("340x450+510+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",17,"bold"),fg="#e90b13",bg="#99978f")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"))
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your BirthDay","Your Birth Place ","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
            
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password ",font=("times new roman",15,"bold"))
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                img7=Image.open(r"images\Reset_btn.png")
                img7=img7.resize((175,50),Image.LANCZOS)
                self.photoimg7=ImageTk.PhotoImage(img7)

                btn=Button(self.root2,image=self.photoimg7,cursor="hand2",command=self.reset_pass,borderwidth=0)
                btn.place(x=70,y=290)

    def open_face_recognition_system(self, current_teacher_id):
        # Create a new Tkinter window for the face recognition system
        root = Tk()
        app = Face_Recognition_System(root, current_teacher_id)
        root.mainloop()


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Form")
        self.root.geometry("1550x800+0+0")

        # ======= Varibles =======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # ======= BG Image =======
        self.bg=ImageTk.PhotoImage(file=r"Images\register_bg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ======= BG Image =======
        self.bg1=ImageTk.PhotoImage(file=r"Images\register_pic.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # ======= Main Frame =======
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=50,y=20)

        # =======Label And Entry =======

        # -------- Row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # ------- Row 2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # ------- Row 3 

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your BirthDay","Your Birth Place ","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",17,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # -------Row 4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,show="*",textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        conf_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        conf_pswd.place(x=370,y=310)

        self.txt_conf_pswd=ttk.Entry(frame,show="*",textvariable=self.var_confpass,font=("times new roman ",15,"bold"))
        self.txt_conf_pswd.place(x=370,y=340,width=250)

        # ======= CHECK BUTTON=======
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term And Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=50,y=380)

        # ======= Button =======
        img=Image.open(r"Images\Register_btn.png")
        img=img.resize((175,50))
        self.PhotoImage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.PhotoImage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=45,y=420,width=175)

    # ======= Function Declaration =======

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "select":
            messagebox.showerror("Error", "All Fields Required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password And Confirm Password Must Be Same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree to our Terms And Conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    teacher_id = str(uuid.uuid4())  # Generate a unique UUID for the teacher
                    my_cursor.execute("insert into register (fname, lname, contact, email, securityQ, securityA, password, teacher_id) values (%s, %s, %s, %s, %s, %s, %s, %s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get(),
                        teacher_id
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully")
                    self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


class Face_Recognition_System:
    def __init__(self, root, current_teacher_id):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.current_teacher_id = current_teacher_id
        
        # ======= Image One =======
        img=Image.open(r"Images\1_pic.jpg")
        img=img.resize((465,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        s_lbl=Label(self.root,image=self.photoimg)
        s_lbl.place(x=0,y=0,width=465,height=130)

        # ======= Image Two =======
        img1=Image.open(r"Images\2_pic.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        t_lbl=Label(self.root,image=self.photoimg1)
        t_lbl.place(x=465,y=0,width=465,height=130)

        # =======Image Third =======
        img2=Image.open(r"Images\3_pic.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=930,y=0,width=465,height=130)

        # BackGround Image 
        img3=Image.open(r"Images\Main_bg.jpg")
        img3=img3.resize((1366,768),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=768)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSYTEM",font=("times new roman",30,"bold"),bg="gray",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        # Student Button 
        img4=Image.open(r"Images\Student_details_btn.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2",borderwidth=0)
        b1.place(x=200,y=55,width=220,height=220)

        b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="white")
        b1_1.place(x=200,y=255,width=220,height=40)

        # Detect Face Button 
        img5=Image.open(r"Images\Face_Detector_btn.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data,borderwidth=0)
        b1.place(x=550,y=55,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="gray",fg="white")
        b1_1.place(x=550,y=255,width=220,height=40)

        # Attendance Face Button 
        img6=Image.open(r"Images\Attendance-btn.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data,borderwidth=0)
        b1.place(x=880,y=55,width=220,height=220)

        b1_1=Button(bg_img,text=" Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="gray",fg="white")
        b1_1.place(x=880,y=255,width=220,height=40)

        # Train Button 
        img8=Image.open(r"Images\Train-btn.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data,borderwidth=0)
        b1.place(x=200,y=310,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="gray",fg="white")
        b1_1.place(x=200,y=525,width=220,height=40)

        # Photos Face Button 
        img9=Image.open(r"Images\photos.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img,borderwidth=0)
        b1.place(x=550,y=310,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="gray",fg="white")
        b1_1.place(x=550,y=525,width=220,height=40)

        # Exit Button 
        img11=Image.open(r"Images\Exit-btn.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",borderwidth=0,command=self.iexit)
        b1.place(x=880,y=310,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg="gray",fg="white")
        b1_1.place(x=880,y=525,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    # ======= Function Button =======

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window, self.current_teacher_id)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window, self.current_teacher_id)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window, self.current_teacher_id)  


if __name__ == "__main__":
    main()
