from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class student:
    def __init__(self,root,teacher_id):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")
        self.current_teacher_id = teacher_id  # Assign the teacher_id to an instance variable

        # ======= Variables =======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # BackGround Image 
        img3=Image.open(r"Images\Student_bg.jpg")
        img3=img3.resize((1366,768),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="gray",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        mian_frame=Frame(bg_img,bd=2,bg="white")
        mian_frame.place(x=5,y=55,width=1350,height=620)

        # left label frame
        Left_frame=LabelFrame(mian_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=585)

        img_left=Image.open(r"Images\Student_info1.jpg")
        img_left=img_left.resize((650,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=130)

        # Current Course information
        Current_Course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_Course_frame.place(x=5,y=130,width=645,height=115)

        # Department
        dep_lbl =Label(Current_Course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        dep_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Civil", "SE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky="w")
        dep_combo.bind("<<ComboboxSelected>>", self.update_course_options)  # Bind department selection event

        # semester
        semester_label = Label(Current_Course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        semester_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        semester_combo.current(0)
        semester_combo.grid(row=0, column=3, padx=2, pady=10, sticky="w")
        semester_combo.bind("<<ComboboxSelected>>", self.update_course_options)  # Bind semester selection event


        #  Year update Now its Session
        year_label=Label(Current_Course_frame,text="Session",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Session","2020-2024","2021-2025","2022-2026"," 2023-2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Course
        self.course_label=Label(Current_Course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        self.course_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.course_combo = ttk.Combobox(Current_Course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.course_combo.grid(row=1, column=3, padx=5, pady=10, sticky="w")


        # Class Student  information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=645,height=300)

        #  Student ID
        studentid_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #  Student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class Section
        class_div_label=Label(class_student_frame,text="Class Section:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        class_div_combo["values"]=("Select Section","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date of Birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone
        phone_label=Label(class_student_frame,text="Phone:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address 
        adress_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        adress_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value= YES)
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value= NO)
        radiobutton2.grid(row=6,column=1)

        # Button Frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=640,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="gray",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=15,font=("times new roman",13,"bold"),bg="gray",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=15,font=("times new roman",13,"bold"),bg="gray",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=15,font=("times new roman",13,"bold"),bg="gray",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=640,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_data,text="Take Photo Sample",width=32,font=("times new roman",13,"bold"),bg="gray",fg="white")
        take_photo_btn.grid(row=0,column=0)

        delete_photo_btn=Button(btn_frame1,text="Delete Photo Sample",command=self.on_delete_button_click,width=32,font=("times new roman",13,"bold"),bg="gray",fg="white")
        delete_photo_btn.grid(row=0,column=1)


        # Right label frame
        Right_frame=LabelFrame(mian_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=585)

        img_right=Image.open(r"Images\Student_info2.jpg")
        img_right=img_right.resize((650,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=130)

        # ======= Search SYSTEM =======
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=650,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        self.var_combo_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combo_search,font=("times new roman",12,"bold"),state="readonly",width=17)
        search_combo["values"]=("Select","Roll","Name","Student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",12,"bold"),bg="gray",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showall_btn=Button(search_frame,text="Show All",command=self.fetch_data,width=12,font=("times new roman",12,"bold"),bg="gray",fg="white")
        showall_btn.grid(row=0,column=4,padx=3)

        # ======= Table Frame =======
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photosamplestatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=120)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ======= DEP , SEM AND Course Selection =======
    def update_course_options(self, event=None):
        selected_department = self.var_dep.get()
        selected_semester = self.var_semester.get()

        if selected_department and selected_semester:
            courses = self.get_courses_for_department_and_semester(selected_department, selected_semester)

            if courses:
            # Update course combo box with the retrieved courses
                self.course_combo["values"] = ["Select Course"] + courses
                self.course_combo.current(0)  # Select "Select Course" by default
            else:
            # If no courses are available for the selected department and semester
                self.course_combo["values"] = ["Select Course"]
                self.course_combo.current(0)  # Select "Select Course" by default
        else:
        # Reset course combo box if department or semester is not selected
            self.course_combo["values"] = ["Select Department First"]
            self.course_combo.current(0)  # Select "Select Department First" by default

    def get_courses_for_department_and_semester(self, department, semester):
        # Define course mappings based on department and semester
        course_map = {
            "Computer Science": {
                "1st": ["AAF-302-FA", "CSI-321-ItA", "ENG-322-ECAC", "ISL-321-IS", "MTH-323-CAAG", "PST-321-PS"],
                "2nd": ["CSI-301-PF", "CSI-405-DS", "ECO-408-ItPE", "ELE-401-DLD", "ENG-422-TW", "MTH-324-M-vC"],
                "3rd": ["CSI-302-OOP", "CSI-401-DSaA", "CSI-504-CN", "MTH-423-DE", "PHY-323-BE", "STA-321-ItST"],
                "4th": ["CSI-403-COaAL", "CSI-406-DS", "CSI-418-WC", "CSI-505-NC", "SWE-401-ItSE"],
                "5th": ["CSI-404-ToA", "CSI-407-PP", "CSI-503-OS", "ENG-421-CS", "MTH-424-LA"],
                "6th": ["CSI-402-DaAoA", "CSI-502-AI", "CSI-506-WDaD", "CSI-508-FoDM", "CSI-602-DDS"],
                "7th": [""]
            },
            "IT": {
                "1st": ["CSI-302 Object ", "ENG-421 Communication ", "CSI-405 Discrete "],
                "2nd": ["CSI-402 Operat", "CSI-619 Information ", "CSI-512 Computer "]
            },
            "Civil": {},  # Add courses for Civil department
            "SE": {}      # Add courses for SE department
        }

        return course_map.get(department, {}).get(semester, [])


    # ======= Function Decreation =======

    # ======= Add Data =======
    
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            return
      
        try:
            print(f"Adding student with teacher_id: {self.current_teacher_id}")  # Debugging line
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)
            my_cursor = conn.cursor()

            # Check if a student with the same ID and teacher ID already exists
            check_query = "SELECT * FROM student WHERE Student_id = %s AND teacher_id = %s"
            my_cursor.execute(check_query, (self.var_std_id.get(), self.current_teacher_id))
            student_record = my_cursor.fetchone()

            if student_record:
                messagebox.showerror("Error", "Student with this ID already exists for this teacher.", parent=self.root)
                conn.close()
                return

            # Check if the student_id exists with a different teacher_id
            check_query_all = "SELECT * FROM student WHERE Student_id = %s"
            my_cursor.execute(check_query_all, (self.var_std_id.get(),))
            student_record_all = my_cursor.fetchone()

            if student_record_all:
                # Ask the user for confirmation
                confirm = messagebox.askyesno("Confirm Add", "Student ID already exists for a different teacher. Do you want to add this student for the current teacher?", parent=self.root)
                if not confirm:
                    conn.close()
                    return

            # Insert new student data
            insert_query = """
            INSERT INTO student (Dep, Course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample, teacher_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.current_teacher_id
            )
            my_cursor.execute(insert_query, values)
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add student: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras", port=3307)
            my_cursor = conn.cursor()
            
            # Get the column names, excluding the 'id' column
            my_cursor.execute("SHOW COLUMNS FROM student")
            columns = [col[0] for col in my_cursor.fetchall() if col[0] != 'id']
            columns_query = ", ".join(columns)

            # Use current_teacher_id to filter students, excluding the `id` column
            query = f"SELECT {columns_query} FROM student WHERE teacher_id = %s"
            my_cursor.execute(query, (self.current_teacher_id,))
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



    #  ======= Get Cursor =======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        

        selected_department = self.var_dep.get()
        selected_semester = self.var_semester.get()

        if selected_department and selected_semester:
            courses = self.get_courses_for_department_and_semester(selected_department, selected_semester)

            if courses:
            # Update course combo box with the retrieved courses
                self.course_combo["values"] = ["Select Course"] + courses
                if self.var_course.get() in courses:
                    self.course_combo.set(self.var_course.get())  # Set the current course if it's in the courses list
                else:
                    self.course_combo.current(0)  # Select "Select Course" by default if current course is not in the list
            else:
            # If no courses are available for the selected department and semester
                self.course_combo["values"] = ["Select Course"]
                self.course_combo.current(0)  # Select "Select Course" by default
        else:
        # Reset course combo box if department or semester is not selected
            self.course_combo["values"] = ["Select Department First"]
            self.course_combo.current(0)  # Select "Select Department First" by defaul


    #  ======= UPDATE FUNTION =======
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)
                my_cursor = conn.cursor()

                # Check if the student ID exists in the student table
                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (self.var_std_id.get(),))
                student_record = my_cursor.fetchone()

                # If the student ID does not exist, show an error message
                if not student_record:
                    messagebox.showerror("Error", "Student not found. Please save the data first.", parent=self.root)
                    conn.close()
                    return

                # Here, fetch the original student ID from the database to compare
                original_student_id = student_record[0]

                # If the current student ID does not match the original, show an error message
                if self.var_std_id.get() != original_student_id:
                    messagebox.showerror("Error", "Student ID cannot be changed.", parent=self.root)
                    conn.close()
                    return

                update = messagebox.askyesno("Update", "Do you want to update your details?", parent=self.root)
                if update:
                    my_cursor.execute("""
                        UPDATE student 
                        SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # ======= Delete Function =======
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do u want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)   
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","STudent Details Delete Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Duo To :{str(es)}",parent=self.root)

    # ======= Reset ========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ======= Generate Data Sample or Take Photo Sample ======= 
    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                student_id = self.var_std_id.get()
                id=0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s,Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                    self.var_std_id.get()==id+1                
                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()            

           
                # ======= Load predefined data on face frontals from opencv =======

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # Minimum Neighbor=5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(1)

                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(70,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Corpped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Duo To :{str(es)}",parent=self.root)


    def delete_student_photos(self, student_id):
        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras",port=3307)
            my_cursor = conn.cursor()

            # Retrieve the student's photo file names
            my_cursor.execute("SELECT PhotoSample FROM student WHERE Student_id = %s", (student_id,))
            photo_results = my_cursor.fetchall()

            # Close database connection
            conn.close()

            # Delete each photo file associated with the student ID
            for img_id in range(1, 101):  # Assuming image IDs range from 1 to 100
                photo_file_path = f"data/user.{student_id}.{img_id}.jpg"
                print("Deleting photo:", photo_file_path)  # Debug print statement
                if os.path.exists(photo_file_path):
                    os.remove(photo_file_path)
                    print("Photo deleted successfully")  # Debug print statement
                else:
                    print("Photo file does not exist")  # Debug print statement

            messagebox.showinfo("Success", "All student photos have been deleted successfully", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Failed to delete student photos due to: {str(es)}", parent=self.root)

    def on_delete_button_click(self):
        # Get the selected student ID from your variable (var_std_id)
        student_id = self.var_std_id.get()

        if student_id == "":
            messagebox.showerror("Error", "Please select a student ID", parent=self.root)
            return

        # Call the method to delete student photos
        self.delete_student_photos(student_id)

    # ======= Search OPtion =======
    def search_data(self):
        if self.var_combo_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select an option and enter a search query.", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras", port=3307)
            my_cursor = conn.cursor()

            search_field = self.var_combo_search.get()
            search_value = self.var_search.get()

            # Validate search_field to prevent SQL injection
            valid_fields = ("Roll", "Name", "Student_id")  # Adjust based on your valid field names
            if search_field not in valid_fields:
                messagebox.showerror("Error", "Invalid search field.", parent=self.root)
                conn.close()
                return

            # Retrieve all columns except 'id' dynamically
            my_cursor.execute("SHOW COLUMNS FROM student")
            columns = [col[0] for col in my_cursor.fetchall() if col[0].lower() != 'id']
            columns_query = ", ".join(columns)

            # Construct the SQL query with teacher ID condition using parameterized query to avoid SQL injection
            query = f"SELECT {columns_query} FROM student WHERE {search_field} LIKE %s AND teacher_id = %s"
            my_cursor.execute(query, (f"%{search_value}%", self.current_teacher_id))

            data = my_cursor.fetchall()
            if data:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", "end", values=i)
            else:
                messagebox.showinfo("No Results", "No records found matching the search criteria.", parent=self.root)

            conn.commit()
            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Database error: {e}", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"An unexpected error occurred: {es}", parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()