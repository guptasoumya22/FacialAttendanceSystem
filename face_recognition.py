# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import mysql.connector
# import cv2
# from datetime import datetime


# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition System")
#         self.root.configure(bg="white")

#         # Header Image
#         img1= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\header1.webp").resize((500,130), Image.Resampling.LANCZOS)
#         img2= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\fas3.png").resize((500,130), Image.Resampling.LANCZOS)
#         img3= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\header3.jpg").resize((500,130), Image.Resampling.LANCZOS)
#         combined_width = img1.width + img2.width + img3.width
#         combined_height = img1.height
#         combined_img = Image.new('RGB', (combined_width, combined_height))
#         combined_img.paste(img1, (0, 0))
#         combined_img.paste(img2, (img1.width, 0))
#         combined_img.paste(img3, (img1.width + img2.width, 0))
#         self.photoimg = ImageTk.PhotoImage(combined_img)
#         f_lbl = Label(self.root, image=self.photoimg, bd=0)
#         f_lbl.place(x=20, y=20, width=combined_width, height=130)


#         # Title Label 
#         title_lbl = Label(self.root, text="Face Recognition", 
#                           font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
#         title_lbl.place(x=0, y=140, width=1366, height=70)

#         # Background Frame 
#         main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
#         main_frame.place(x=30, y=220, width=1300, height=500)


#         bg_image = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\face.jpg").resize((1300, 500), Image.Resampling.LANCZOS)
#         self.bg_photo = ImageTk.PhotoImage(bg_image)
#         bg_label = Label(main_frame, image=self.bg_photo)
#         bg_label.place(x=0, y=0, width=1300, height=500)

#         # Footer
#         footer_lbl = Label(self.root, text="Developed by Team-47", font=("Helvetica", 15), bg="#003366", fg="white", bd=0)
#         footer_lbl.place(x=0, y=760, width=1366, height=30)

#         # Button Styling
#         btn_style = {
#             'font': ("times new roman", 20, "bold"),
#             'bg': "#003366",
#             'fg': "white",
#             'relief': RIDGE,
#             'bd': 10,
#         }

#         # Face Recognition Button
#         face_recognition_btn = Button(main_frame, text="Face Recognition", **btn_style, command=self.face_recog)
#         face_recognition_btn.place(x=50, y=200, width=300, height=100)

#     # Mark Attendance
#     def mark_attendance(self, r, n, d):
#         with open("group47.csv", "r+", newline="\n") as f:
#             data = f.readlines()
#             names = [line.split(",")[0] for line in data]
#             if r not in names:
#                 now = datetime.now()
#                 date = now.strftime("%d/%m/%Y")
#                 time = now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{r},{n},{d},{time},{date},Present")

#     # Face Recognition Logic
#     def face_recog(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
#             coord = []

#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
#                 id, predict = clf.predict(gray[y:y + h, x:x + w])
#                 confidence = int((100 * (1 - predict / 300)))

#                 try:
#                     conn = mysql.connector.connect(
#                         host="localhost", username="root", password="Happysql@22", database="face_recognition"
#                     )
#                     cursor = conn.cursor()
#                     cursor.execute("SELECT name, Enroll, Dep FROM student WHERE Enroll = %s", (id,))
#                     result = cursor.fetchone()

#                     if result and confidence > 70:
#                         name, enroll, dep = result
#                         cv2.putText(img, f"Name: {name}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                         cv2.putText(img, f"Enroll: {enroll}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                         self.mark_attendance(enroll, name, dep)
#                     else:
#                         cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

#                 except mysql.connector.Error as e:
#                     messagebox.showerror("Database Error", str(e))

#             return coord

#         def recognize(img, clf, face_cascade):
#             draw_boundary(img, face_cascade, 1.1, 10, (255, 255, 255), "Face", clf)
#             return img

#         face_cascade = cv2.CascadeClassifier(r"C:\Users\hp\Desktop\FacialAttendanceSystem\haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read(r"C:\Users\hp\Desktop\FacialAttendanceSystem\classifier.xml")

#         video_capture = cv2.VideoCapture(0)
#         while True:
#             ret, img = video_capture.read()
#             if not ret:
#                 break
#             img = recognize(img, clf, face_cascade)
#             cv2.imshow("Face Recognition", img)

#             if cv2.waitKey(1) == 13:  # Press Enter to exit
#                 break

#         video_capture.release()
#         cv2.destroyAllWindows()


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()


import cv2
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="white")

        # Header Image
        img1= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\header1.webp").resize((500,130), Image.Resampling.LANCZOS)
        img2= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\fas3.png").resize((500,130), Image.Resampling.LANCZOS)
        img3= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\header3.jpg").resize((500,130), Image.Resampling.LANCZOS)
        combined_width = img1.width + img2.width + img3.width
        combined_height = img1.height
        combined_img = Image.new('RGB', (combined_width, combined_height))
        combined_img.paste(img1, (0, 0))
        combined_img.paste(img2, (img1.width, 0))
        combined_img.paste(img3, (img1.width + img2.width, 0))
        self.photoimg = ImageTk.PhotoImage(combined_img)
        f_lbl = Label(self.root, image=self.photoimg, bd=0)
        f_lbl.place(x=20, y=20, width=combined_width, height=130)

        # Title Label 
        title_lbl = Label(self.root, text="Face Recognition", 
                          font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
        title_lbl.place(x=0, y=140, width=1366, height=70)

        # Background Frame 
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=220, width=1300, height=500)

        bg_image = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\face.jpg").resize((1300, 500), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(main_frame, image=self.bg_photo)
        bg_label.place(x=0, y=0, width=1300, height=500)

        # Footer
        footer_lbl = Label(self.root, text="Developed by Team-47", font=("Helvetica", 15), bg="#003366", fg="white", bd=0)
        footer_lbl.place(x=0, y=760, width=1366, height=30)

        # Button Styling
        btn_style = {
            'font': ("times new roman", 20, "bold"),
            'bg': "#003366",
            'fg': "white",
            'relief': RIDGE,
            'bd': 10,
        }

        # Face Recognition Button
        face_recognition_btn = Button(main_frame, text="Face Recognition", **btn_style, command=self.face_recog)
        face_recognition_btn.place(x=50, y=200, width=300, height=100)

    # Mark Attendance
    def mark_attendance(self, r, n, d):
        with open("group47.csv", "r+", newline="\n") as f:
            data = f.readlines()
            names = [line.split(",")[0] for line in data]
            if r not in names:
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{time},{date},Present")

    # Face Recognition Logic
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Happysql@22", database="face_recognition"
                    )
                    cursor = conn.cursor()
                    cursor.execute("SELECT name, Enroll, Dep FROM student WHERE Enroll = %s", (id,))
                    result = cursor.fetchone()

                    if result and confidence > 70:
                        name, enroll, dep = result
                        cv2.putText(img, f"Name: {name}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Enroll: {enroll}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        self.mark_attendance(enroll, name, dep)
                    else:
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", str(e))

            return coord

        def recognize(img, clf, face_cascade):
            draw_boundary(img, face_cascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        face_cascade = cv2.CascadeClassifier(r"C:\Users\hp\Desktop\FacialAttendanceSystem\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\hp\Desktop\FacialAttendanceSystem\classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            if not ret:
                break
            img = recognize(img, clf, face_cascade)
            cv2.imshow("Face Recognition", img)

            key = cv2.waitKey(1) & 0xFF  # Capture keypress event
            if key == 13:  # Enter key (13)
                print("Enter key pressed. Closing window.")
                break

        video_capture.release()  # Release video capture device
        cv2.destroyAllWindows()  # Close OpenCV windows

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
