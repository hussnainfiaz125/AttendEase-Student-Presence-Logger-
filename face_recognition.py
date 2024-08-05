import mysql.connector
from mysql.connector import Error
import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

class Face_Recognition:
    def __init__(self, root, current_teacher_id):
        self.root = root
        self.current_teacher_id = current_teacher_id  # Store current_teacher_id
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="gray", fg="white")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # Load images
        img_top = Image.open(r"Images\Face_pic1.jpg")
        img_top = img_top.resize((600, 650), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=600, height=650)

        img_bottom = Image.open(r"Images\Face_pic2.png")
        img_bottom = img_bottom.resize((900, 650), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=600, y=45, width=900, height=650)

        # Button for face recognition
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="gray", fg="white")
        b1_1.place(x=350, y=575, width=200, height=40)

        # Bind window closing event
        root.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def mark_attendance(self, student_id, roll, name, department):
        try:
            teacher_id = self.current_teacher_id
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras", port=3307)
            cursor = conn.cursor()

            # Fetch the student's assigned teacher ID
            sql_teacher_check = "SELECT teacher_id FROM student WHERE Student_id = %s"
            cursor.execute(sql_teacher_check, (student_id,))
            student_teacher_id = cursor.fetchone()

            if student_teacher_id and student_teacher_id[0] == teacher_id:
                current_date = datetime.now().strftime("%Y-%m-%d")

                # Check if attendance record for today already exists
                sql_check = "SELECT * FROM attendance WHERE Attendance_Id = %s AND Date = %s"
                cursor.execute(sql_check, (student_id, current_date))
                existing_record = cursor.fetchone()

                if existing_record:
                    print("Attendance already marked for today. No update allowed.")
                else:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    # Insert new attendance record
                    sql_insert = """
                        INSERT INTO attendance (Attendance_Id, Roll, Name, Dep, Time, Date, Attendance, Teacher_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    insert_values = (student_id, roll, name, department, current_time, current_date, "Present", teacher_id)
                    cursor.execute(sql_insert, insert_values)
                    conn.commit()
            else:
                print("The student's teacher ID does not match the current teacher ID. Attendance not marked.")

        except mysql.connector.Error as error:
            if error.errno == 1062:
                print("Duplicate entry error: Record already exists for today.")
            else:
                print(f"Failed to insert/update record into MySQL table: {error}")

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


    def mark_remaining_absent(self, current_teacher_id):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras", port=3307)
            cursor = conn.cursor()

            current_date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")

            # Fetch all student IDs who are not marked as present today and have the same teacher ID
            sql_absent = """
                SELECT Student_id, Name, Roll, Dep 
                FROM student 
                WHERE teacher_id = %s 
                AND Student_id NOT IN (
                    SELECT DISTINCT Attendance_Id 
                    FROM attendance 
                    WHERE Date = %s 
                    AND Attendance = 'Present'
                    AND Teacher_id = %s
                )
            """
            cursor.execute(sql_absent, (current_teacher_id, current_date, current_teacher_id))
            absent_students = cursor.fetchall()

            for student in absent_students:
                student_id = student[0]
                student_name = student[1]
                roll_number = student[2]
                department = student[3]

                # Check if absent record for this student on this date already exists
                cursor.execute("SELECT * FROM attendance WHERE Attendance_Id = %s AND Date = %s AND Teacher_id = %s", (student_id, current_date, current_teacher_id))
                existing_record = cursor.fetchone()

                if not existing_record:
                    # Insert absent record for the student (if it doesn't already exist)
                    cursor.execute("""
                        INSERT INTO attendance 
                        (Attendance_Id, Roll, Name, Dep, Time, Date, Attendance, Teacher_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (student_id, roll_number, student_name, department, current_time, current_date, "Absent", current_teacher_id))
                    conn.commit()

        except mysql.connector.Error as error:
            print(f"Failed to mark remaining students as absent: {error}")

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, conn, cursor):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 79:
                    cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id = %s", (id,))
                    result = cursor.fetchone()
                    if result:
                        name = result[0]
                        roll = result[1]
                        dep = result[2]
                        cv2.putText(img, f"ID:{id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll:{roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(id, roll, name, dep)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        def recognize(img, clf, faceCascade, conn, cursor):
            draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf, conn, cursor)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="fras", port="3307")
            cursor = conn.cursor()

            while True:
                ret, img = video_cap.read()
                img = recognize(img, clf, faceCascade, conn, cursor)
                cv2.imshow("Welcome To Face Recognition", img)

                key = cv2.waitKey(1)
                if key == 27 or key == 13:
                    break

        finally:
            video_cap.release()
            cv2.destroyAllWindows()
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


    def on_window_close(self):
        try:
            # Call the method to mark remaining students as absent
            self.mark_remaining_absent(self.current_teacher_id)

        except Exception as e:
            print(f"Error marking remaining students as absent: {e}")
        finally:
            self.root.destroy()  

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root, current_teacher_id)
    root.mainloop()
