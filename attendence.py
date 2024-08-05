from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root, current_teacher_id):
        self.current_teacher_id = current_teacher_id
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance")

        #  ======= Varaibles =======
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # ======= Image One =======
        img=Image.open(r"Images\Attendance_pic1.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        s_lbl=Label(self.root,image=self.photoimg)
        s_lbl.place(x=0,y=0,width=700,height=200)

        # ======= Image Two =======
        img1=Image.open(r"Images\Attendance_pic2.jpg")
        img1=img1.resize((700,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        t_lbl=Label(self.root,image=self.photoimg1)
        t_lbl.place(x=700,y=0,width=700,height=200)

        # BackGround Image 
        img3=Image.open(r"Images\Attendance_bg.jpg")
        img3=img3.resize((1366,768),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1366,height=768)

        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="gray",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        mian_frame=Frame(bg_img,bd=2,bg="white")
        mian_frame.place(x=10,y=50,width=1340,height=620)

        # left label frame
        Left_frame=LabelFrame(mian_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=430)

        img_left=Image.open(r"Images\Attendance_pic3.jpg")
        img_left=img_left.resize((650,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=135,width=650,height=270)

        #  ======= Labels and Entry =======

        #  Attendance ID
        attendenceid_label=Label(left_inside_frame,text="Attendance ID:",font="comicsansns 12 bold",bg="white")
        attendenceid_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font="comicsansns 12 bold")
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll No
        rolllabel=Label(left_inside_frame,text="Roll No:",font="comicsansns 12 bold",bg="white")
        rolllabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font="comicsansns 12 bold")
        atten_roll.grid(row=0,column=3,pady=5)

        #  Student Name
        studentName_label=Label(left_inside_frame,text="Student Name:",font="comicsansns 12 bold",bg="white")
        studentName_label.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font="comicsansns 12 bold")
        atten_name.grid(row=1,column=1,pady=8)

        # Department
        depLabel=Label(left_inside_frame,text="Departemnt",bg="white",font="comicsansns 12 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font="comicsansns 12 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        # Time
        timeLabel=Label(left_inside_frame,text="Time",bg="white",font="comicsansns 12 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font="comicsansns 12 bold")
        atten_time.grid(row=2,column=1,pady=8)

        # Date
        dateLabel=Label(left_inside_frame,text="Date",bg="white",font="comicsansns 12 bold")
        dateLabel.grid(row=2,column=2,pady=8)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font="comicsansns 12 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # Attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence",bg="white",font="comicsansns 12 bold")
        attendenceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font="comicsansns 12 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # Button Frame 
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=645,height=35)

        # Create 'export CSV' button

        export_btn=Button(btn_frame,text="Export csv",command=self.export_data,width=20,font=("times new roman",13,"bold"),bg="gray",fg="white")
        export_btn.grid(row=0,column=1,padx=1)

        update_btn=Button(btn_frame,text="Update",width=20,command=self.updateData,font=("times new roman",13,"bold"),bg="gray",fg="white")
        update_btn.grid(row=0,column=2,padx=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("times new roman",13,"bold"),bg="gray",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)

        nbtn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        nbtn_frame.place(x=0,y=210,width=645,height=35)

        newdata_btn=Button(nbtn_frame,text="Add New Data",command=self.addNewData,width=20,font=("times new roman",13,"bold"),bg="gray",fg="white")
        newdata_btn.grid(row=0,column=0,padx=1)

        delete_btn=Button(nbtn_frame,text="Delete Data",command=self.delete_data,width=20,font=("times new roman",13,"bold"),bg="gray",fg="white")
        delete_btn.grid(row=0,column=1,padx=1)

        delete_all_btn=Button(nbtn_frame,text="Delete All Data",command=self.delete_all_data,width=21,font=("times new roman",13,"bold"),bg="gray",fg="white")
        delete_all_btn.grid(row=0,column=2,padx=1)

        # Right label frame
        Right_frame=LabelFrame(mian_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=650,height=430)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=5,width=640,height=397)

        # ======= Scroll Bar =======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","Time","Date","Attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="Attendence ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendence",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendence",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

         # Connect to MySQL database 
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="fras",
            port=3307
        )
        self.cursor = self.db.cursor()

        # Connect to MySQL database
        self.connect_to_database()

        # Fetch data from database and populate the GUI table
        # Call fetch_and_display_data method with current_teacher_id
        self.fetch_and_display_data(current_teacher_id)


    def connect_to_database(self):
        try:
            # Connect to your MySQL database
            self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="fras",
            port=3307
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}",parent=self.root)


    def fetch_and_display_data(self, current_teacher_id):
        try:
            # Retrieve all columns except 'id' dynamically
            self.cursor.execute("SHOW COLUMNS FROM attendance")
            columns = [col[0] for col in self.cursor.fetchall() if col[0].lower() != 'id']
            columns_query = ", ".join(columns)
            
            # Construct the query to fetch only the desired columns
            query = f"SELECT {columns_query} FROM attendance WHERE Teacher_id = %s"
            self.cursor.execute(query, (current_teacher_id,))
            rows = self.cursor.fetchall()
            
            # Clear the table before inserting new data
            self.clear_table()
            
            # Insert the fetched rows into the table
            for row in rows:
                self.AttendanceReportTable.insert("", "end", values=row)
                
        except mysql.connector.Error as err:
            messagebox.showerror("Fetch Error", f"Error fetching data: {err}", parent=self.root)


    def clear_table(self):
        # Clear existing data in the GUI table
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())

    # ======= Fetch Data =======
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def export_data(self):
        try:
            # Execute query to fetch all attendance records from the database
            self.cursor.execute("SELECT * FROM attendance")
            rows = self.cursor.fetchall()

            # Check if there are rows to export
            if not rows:
                messagebox.showinfo("Export", "No data to export",parent=self.root)
                return

            # Ask user to select export location
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")],parent=self.root)

            if file_path:
                # Write fetched data to CSV file
                with open(file_path, "w", newline="") as file:
                    csv_writer = csv.writer(file)
                    # Write header row
                    csv_writer.writerow([i[0] for i in self.cursor.description])
                    # Write data rows
                    csv_writer.writerows(rows)

                messagebox.showinfo("Export", "Data exported successfully!",parent=self.root)
        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting data: {e}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # ======= Reset =======
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

     # Update Data method (new method)
    def updateData(self):
        # Get the selected row's index
        selected_row = self.AttendanceReportTable.focus()

        if selected_row:
            # Get the current values from entry fields
            new_id = self.var_atten_id.get()
            new_roll = self.var_atten_roll.get()
            new_name = self.var_atten_name.get()
            new_dep = self.var_atten_dep.get()
            new_time = self.var_atten_time.get()
            new_date = self.var_atten_date.get()
            new_attendance = self.var_atten_attendance.get()

            # Update the values in the selected row of the table (front-end)
            self.AttendanceReportTable.item(selected_row, values=(new_id, new_roll, new_name, new_dep, new_time, new_date, new_attendance))
            messagebox.showinfo("Success", "Attendance details updated successfully!", parent=self.root)

            try:
                # Update the corresponding row in the database (back-end)
                sql = """
                    UPDATE attendance 
                    SET Roll = %s, Name = %s, Dep = %s, Time = %s, Date = %s, Attendance = %s 
                    WHERE Attendance_Id = %s AND Date = %s
                """
                values = (new_roll, new_name, new_dep, new_time, new_date, new_attendance, new_id, new_date)
                self.cursor.execute(sql, values)
                self.db.commit()  # Commit the transaction
                messagebox.showinfo("Success", "Database updated successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update database: {str(e)}", parent=self.root)


    def addNewData(self):
        new_id = self.var_atten_id.get()
        new_roll = self.var_atten_roll.get()
        new_name = self.var_atten_name.get()
        new_dep = self.var_atten_dep.get()
        new_time = self.var_atten_time.get()
        new_date = self.var_atten_date.get()
        new_attendance = self.var_atten_attendance.get()

        # Validate required fields (e.g., Roll No and Name should not be empty)
        if not new_roll or not new_name:
            messagebox.showerror("Error", "Roll No and Name are required fields", parent=self.root)
            return

        try:
            # Check if the student ID exists in the student table and matches the current teacher ID
            fetch_student_sql = "SELECT teacher_id FROM student WHERE Student_id = %s"
            self.cursor.execute(fetch_student_sql, (new_id,))
            student_record = self.cursor.fetchone()

            if not student_record:
                messagebox.showerror("Error", f"Student ID {new_id} does not exist", parent=self.root)
                return

            teacher_id = student_record[0]

            # Check if the teacher ID matches the current teacher's ID
            if teacher_id != self.current_teacher_id:
                messagebox.showerror("Error", "You do not have permission to add attendance for this student", parent=self.root)
                return

            # Check if the attendance record already exists for the given date
            check_attendance_sql = "SELECT * FROM attendance WHERE Attendance_Id = %s AND Date = %s"
            self.cursor.execute(check_attendance_sql, (new_id, new_date))
            existing_record = self.cursor.fetchone()

            if existing_record:
                messagebox.showerror("Error", f"Attendance record for Student ID {new_id} on {new_date} already exists", parent=self.root)
                return

            # Insert new data into the tkinter table (front-end)
            self.AttendanceReportTable.insert("", END, values=(new_id, new_roll, new_name, new_dep, new_time, new_date, new_attendance))

            # Insert new data into the database table (back-end)
            sql = "INSERT INTO attendance (Attendance_Id, Roll, Name, Dep, Time, Date, Attendance, Teacher_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (new_id, new_roll, new_name, new_dep, new_time, new_date, new_attendance, teacher_id)
            self.cursor.execute(sql, values)
            self.db.commit()  # Commit the transaction
            messagebox.showinfo("Success", "New data added successfully!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add data to database: {str(e)}", parent=self.root)
        

    # store all data from tkinter table into the database
    def storeDataInDatabase(self):
        try:
            # Loop through all items in the AttendanceReportTable
            for child in self.AttendanceReportTable.get_children():
                values = self.AttendanceReportTable.item(child, "values")
                # Insert data into the database table
                sql = "INSERT INTO attendance (Attendance_Id, Roll, Name, Dep, Time, Date, Attendance, Teacher_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql, values)
            self.db.commit()
            messagebox.showinfo("Success", "All data stored in the database successfully!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to store data in the database: {str(e)}", parent=self.root)


    def delete_data(self):
        # Get selected item from the treeview
        selected_item = self.AttendanceReportTable.focus()

        if selected_item:
            try:
                # Get data associated with the selected item
                data = self.AttendanceReportTable.item(selected_item)["values"]
                attendance_id = data[0]  # Assuming ID is the first column in your table
                date = data[5]  # Assuming Date is the 6th column in your table

                # Execute DELETE query to remove data from the database
                delete_query = "DELETE FROM attendance WHERE Attendance_Id = %s AND Date = %s"
                self.cursor.execute(delete_query, (attendance_id, date))
                self.db.commit()  # Commit the transaction

                # Remove selected item from the GUI treeview
                self.AttendanceReportTable.delete(selected_item)

                messagebox.showinfo("Success", "Record deleted successfully!", parent=self.root)

            except mysql.connector.Error as err:
                messagebox.showerror("Delete Error", f"Error deleting record: {err}", parent=self.root)
                print(f"Failed to delete record: {err}")

        else:
            messagebox.showwarning("Delete Error", "Please select a record to delete.", parent=self.root)

            # Add additional debug statements to check selected data
            print(f"Selected Item Data: {data}, Attendance ID: {attendance_id}, Date: {date}")


    def delete_all_data(self):
        # Ask for confirmation using a messagebox
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all your attendance records?", parent=self.root)

        if confirm:
            try:
                teacher_id = self.current_teacher_id  # Get the current teacher's ID

                # Execute DELETE query to remove data where the teacher ID matches
                delete_query = """
                DELETE FROM attendance
                WHERE Teacher_id = %s
                AND Attendance_Id IN (
                    SELECT Student_id FROM student WHERE teacher_id = %s
                )
                """
                self.cursor.execute(delete_query, (teacher_id, teacher_id))
                rows_deleted = self.cursor.rowcount  # Get the number of rows deleted
                self.db.commit()  # Commit the transaction

                # Clear the table in the GUI
                self.clear_table()

                # Show messagebox with the number of records deleted
                messagebox.showinfo("Success", f"{rows_deleted} records deleted successfully!", parent=self.root)

            except mysql.connector.Error as err:
                messagebox.showerror("Delete Error", f"Error deleting records: {err}", parent=self.root)
                print(f"Failed to delete records: {err}")
        else:
            # User clicked No or closed the messagebox
            messagebox.showinfo("Deletion Cancelled", "Deletion operation cancelled.", parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root, current_teacher_id)
    root.mainloop()