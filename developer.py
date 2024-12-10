from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("About Us")
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
        title_lbl = Label(self.root, text="About Us", 
                          font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
        title_lbl.place(x=0, y=140, width=1366, height=70)

        # Background Frame 
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=220, width=1300, height=500)


        # Project Description
        description = """Welcome to the Facial Attendance System project!
This application leverages advanced machine learning algorithms like Haar Cascade and LBPH 
to provide an efficient and automated attendance tracking solution. 
Our goal is to simplify the attendance management process, ensuring accuracy and time savings.
"""
        project_label = Label(main_frame, text=description, font=("times new roman", 15, "bold"), 
                              bg="white", fg="#003366", justify=LEFT, wraplength=1400)
        project_label.place(x=10, y=10)

        # Team Section
        team_label = Label(main_frame, text="Meet the Team", font=("times new roman", 20, "bold"), bg="white", fg="#003366")
        team_label.place(x=10, y=140)

        # Team Member Details
        members = [
            "1. Name: Soumya Gupta, Enrolment No.: 211b317",
            "2. Name: Vaishnavi Sahu, Enrolment No.: 211b338",
            "3. Name: Vanshika Singh, Enrolment No.: 211b339",
        ]
        y_offset = 180
        for member in members:
            member_label = Label(main_frame, text=member, font=("times new roman", 15), bg="white", fg="black", anchor="w")
            member_label.place(x=20, y=y_offset)
            y_offset += 30


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
