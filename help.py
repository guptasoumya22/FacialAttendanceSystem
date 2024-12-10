from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help")
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
        title_lbl = Label(self.root, text="Student Management System", 
                          font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
        title_lbl.place(x=0, y=140, width=1366, height=70)

        # Background Frame 
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=220, width=1300, height=500)


        # Help Desk Content
        help_lbl = Label(main_frame, text="How can we assist you?", 
                         font=("times new roman", 25, "bold"), bg="white", fg="#003366")
        help_lbl.place(x=20, y=20)

        help_content = """If you're facing issues or have queries regarding the Facial Attendance System, 
please feel free to contact us. Our team is here to assist you with any technical or general inquiries.
            
Reach out to us at:
Email: group47@gmail.com
"""
        content_lbl = Label(main_frame, text=help_content, 
                            font=("times new roman", 18), bg="white", fg="black", justify=LEFT)
        content_lbl.place(x=20, y=80)

        # Footer
        footer_lbl = Label(self.root, text="Thank you for using our service!", 
                           font=("times new roman", 18, "italic"), bg="white", fg="black")
        footer_lbl.place(x=0, y=730, width=1366, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
