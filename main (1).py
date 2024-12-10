from tkinter import *
import subprocess
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from attendance import Attendance
from developer import Developer
from face_recognition import Face_Recognition
from help import Help

class Facial_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")
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
        title_lbl = Label(self.root, text="Facial Attendance System", 
                          font=("Helvetica", 40, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
        title_lbl.place(x=0, y=150, width=1530, height=80)

        # Background Frame
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=250, width=1410, height=500)

        # Load Images
        student_details_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\mark.jpg")
        student_details_img = student_details_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.student_details_photo = ImageTk.PhotoImage(student_details_img)

        view_att_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\view_attendance.png")
        view_att_img = view_att_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.view_att_photo = ImageTk.PhotoImage(view_att_img)

        exit_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\exit.jpg")
        exit_img = exit_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.exit_photo = ImageTk.PhotoImage(exit_img)

        help_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\help.png")
        help_img = help_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.help_photo = ImageTk.PhotoImage(help_img)

        traindata_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\trainh.webp")
        traindata_img = traindata_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.traindata_photo = ImageTk.PhotoImage(traindata_img)

        photo_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\photos.png")
        photo_img = photo_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.photo_photo = ImageTk.PhotoImage(photo_img)

        facedetect_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\face.png")
        facedetect_img = facedetect_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.facedetect_photo = ImageTk.PhotoImage(facedetect_img)

        developer_img = Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\dev.png")
        developer_img = developer_img.resize((100, 100), Image.Resampling.LANCZOS)
        self.developer_photo = ImageTk.PhotoImage(developer_img)


        # Button Style 
        btn_style = {"font": ("Helvetica", 20, "bold"), "bg": "#0055cc",  
                     "activebackground": "#003399", "activeforeground": "white", "bd": 3}
        
        
        button_width = 11

        # Student Details 
        student_details_label = Label(main_frame, image=self.student_details_photo, bg="white")
        student_details_label.grid(row=0, column=0, padx=60, pady=32)
        btn1 = Button(main_frame, text="Student Details", **btn_style, width=button_width, command=self.student_details)
        btn1.grid(row=1, column=0, padx=60, pady=10, ipadx=30, ipady=10)

        # Attendance 
        view_att_label = Label(main_frame, image=self.view_att_photo, bg="white")
        view_att_label.grid(row=0, column=1, padx=60, pady=32)
        btn2 = Button(main_frame, text="Attendance", **btn_style,width=button_width,  command=self.view_attendance)
        btn2.grid(row=1, column=1, padx=60, pady=10, ipadx=30, ipady=10)

        # Exit 
        exit_label = Label(main_frame, image=self.exit_photo, bg="white")
        exit_label.grid(row=0, column=2, padx=60, pady=32)
        btn3 = Button(main_frame, text="Exit", **btn_style,width=button_width,  command=self.iexit)
        btn3.grid(row=1, column=3, padx=60, pady=10, ipadx=30, ipady=10)
        
        # Help Desk 
        help_label = Label(main_frame, image=self.help_photo, bg="white")
        help_label.grid(row=0, column=3, padx=60, pady=32)
        btn4 = Button(main_frame,  text="Help Desk", **btn_style, width=button_width ,command=self.help)
        btn4.grid(row=1, column=2, padx=60, pady=10, ipadx=30, ipady=10)
        
        traindata_label = Label(main_frame, image=self.traindata_photo, bg="white")
        traindata_label.grid(row=2, column=0, padx=60, pady=32)
        train_btn = Button(main_frame, text="Train Data", **btn_style, width=button_width, command=self.train_data)
        train_btn.grid(row=3, column=0, padx=60, pady=10, ipadx=30,  ipady=10)

        photo_label = Label(main_frame, image=self.photo_photo, bg="white")
        photo_label.grid(row=2, column=1, padx=60, pady=32)
        photos_btn = Button(main_frame, text="Photos", **btn_style,width=button_width, command=self.open_image)
        photos_btn.grid(row=3, column=1, padx=60, pady=10, ipadx=30,  ipady=10)
        
        facedetect_label = Label(main_frame, image=self.facedetect_photo, bg="white")
        facedetect_label.grid(row=2, column=2, padx=60, pady=32)
        face_detector_btn = Button(main_frame, text="Face Detector",width=button_width,command=self.face_recognition, **btn_style)
        face_detector_btn.grid(row=3, column=2, padx=60, pady=10, ipadx=30, ipady=10)

        developer_label = Label(main_frame, image=self.developer_photo, bg="white")
        developer_label.grid(row=2, column=3, padx=60, pady=32)
        developer_btn = Button(main_frame,command=self.developer, text="Developer", width=button_width,**btn_style)
        developer_btn.grid(row=3, column=3, padx=60, pady=10, ipadx=30, ipady=10)

        # Footer
        footer_lbl = Label(self.root, text="Developed by Team-47", font=("Helvetica", 15), bg="#003366", fg="white", bd=0)
        footer_lbl.place(x=0, y=760, width=1530, height=30)

    def iexit(self):
       self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?",parent=self.root)
       if self.iexit>0:
          self.root.destroy()
       else:
          return
          

    def student_details(self):
        print("Student Details Function Called")

    def view_attendance(self):
        print("Attendance Function Called")

    def exit(self):
        self.root.quit()

    def help(self):
        print("Help Desk Function Called")

    def train_data(self):
        print("Train Data Function Called")

    
    def face_recognition(self):
        print("Face Detector Function Called")

    def developer(self):
        messagebox.showinfo("Developer", "Developed by Team-47")


    #openimage
    def open_image(self):
        folder_path = r"C:\Users\hp\Desktop\FacialAttendanceSystem\data"
        try:
            subprocess.run(["open", folder_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Unable to open folder: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


#Func Btn
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)

    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)
    
    def face_recognition(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)

    def view_attendance(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)

    def developer(self):
      self.new_window=Toplevel(self.root)
      self.app=Developer(self.new_window)

    def help(self):
      self.new_window=Toplevel(self.root)
      self.app=Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Facial_Attendance_System(root)
    root.mainloop()
