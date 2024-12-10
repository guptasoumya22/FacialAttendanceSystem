from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")
        self.root.configure(bg="white")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_name=StringVar()
        self.var_enroll=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()


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
        title_lbl = Label(self.root, text="Student Details", 
                          font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
        title_lbl.place(x=0, y=140, width=1366, height=70)

        # Background Frame 
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=220, width=1300, height=500)

        #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white", fg= "black", text='Student Information', font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10,width=630, height=470)
        
        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="black", fg= "white", text='Current Course Information', font=("times new roman",12,"bold"))
        current_course_frame.place(x=20, y=30,width=610, height=140)
        
        #department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman",12,"bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman",12,"bold"), width=17)
        dep_combo["values"]=("Select Department", "CSE", "ECE", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        #Course
        course_label=Label(current_course_frame, text="Course", font=("times new roman",12,"bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo=ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman",12,"bold"), width=17)
        course_combo["values"]=("Select Course", "B.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #year
        year_label=Label(current_course_frame, text="Year", font=("times new roman",12,"bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman",12,"bold"), width=17)
        year_combo["values"]=("Select Year", "1st", "2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #sem
        sem_label=Label(current_course_frame, text="Sem", font=("times new roman",12,"bold"))
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("times new roman",12,"bold"), width=17)
        sem_combo["values"]=("Select Semester", "1st", "2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)



        #studentinfo
        student_info_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="black", fg= "white", text='Student Info', font=("times new roman",12,"bold"))
        student_info_frame.place(x=20, y=195,width=610, height=260)

        #studid
        stud_id_label=Label(student_info_frame, text="Enrollment No.", font=("times new roman",12,"bold"))
        stud_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)  # Row 0, Column 0

        studentID_entry=ttk.Entry(student_info_frame, textvariable=self.var_name, font=("times new roman",12,"bold"), width=17)
        studentID_entry.grid(row=0, column=1, padx=20, pady=5, sticky=W)  # Increased padx to 20

        # Enrollment No.
        enroll_label=Label(student_info_frame, text="Student Name", font=("times new roman",12,"bold"))
        enroll_label.grid(row=0, column=2, padx=20, pady=5, sticky=W)  # Added more padx for spacing

        enroll_entry=ttk.Entry(student_info_frame, textvariable=self.var_enroll, font=("times new roman",12,"bold"), width=17)
        enroll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        #gender
        gender_label=Label(student_info_frame, text="Gender", font=("times new roman",12,"bold"))
        gender_label.grid(row=1, column=0, padx=10,pady=5,  sticky=W)

        gender_combo=ttk.Combobox(student_info_frame,textvariable=self.var_gender, font=("times new roman",12,"bold"), width=15)
        gender_combo["values"]=("Select Gender", "Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=8, pady=10, sticky=W)

        #DOB
        DOB_label=Label(student_info_frame, text="DOB", font=("times new roman",12,"bold"))
        DOB_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        DOB_entry=ttk.Entry(student_info_frame, textvariable=self.var_DOB, font=("times new roman",12,"bold"), width=17)
        DOB_entry.grid(row=1, column=3, padx=10,pady=5,  sticky=W)

        #email
        email_label=Label(student_info_frame, text="Email", font=("times new roman",12,"bold"))
        email_label.grid(row=2, column=0, padx=10,pady=5,  sticky=W)

        email_entry=ttk.Entry(student_info_frame,textvariable=self.var_email, font=("times new roman",12,"bold"), width=17)
        email_entry.grid(row=2, column=1, padx=10,pady=5,  sticky=W)

        #phoneno.
        phone_no_label=Label(student_info_frame, text="Phone No.", font=("times new roman",12,"bold"))
        phone_no_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        phone_no_entry=ttk.Entry(student_info_frame,textvariable=self.var_phone, font=("times new roman",12,"bold"), width=17)
        phone_no_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #buttons
        btn_frame=Frame(student_info_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=170,width=715,height=70)

        save_btn=Button(btn_frame,text="Save", command=self.add_data, width=17,font=("times new roman",12,"bold"))
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"))
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"))
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman",12,"bold"))
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset, width=17,font=("times new roman",12,"bold"))
        take_photo_btn.grid(row=1,column=0)


        
  
        #rightframe
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white", fg= "black", text='Student Details', font=("times new roman",12,"bold"))
        Right_frame.place(x=650, y=10,width=635, height=470)
        
        #searchframe
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="black", fg= "white", text='Search System', font=("times new roman",12,"bold"))
        search_frame.place(x=20, y=30,width=610, height=140)
        
        search_label=Label(search_frame, text="Department", font=("times new roman",12,"bold"))
        search_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        search_combo=ttk.Combobox(search_frame, font=("times new roman",12,"bold"), width=17)
        search_combo["values"]=("Select", "Enrollment", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame, font=("times new roman",12,"bold"), width=17)
        search_entry.grid(row=0, column=2, padx=10,pady=5,  sticky=W)

        search_btn=Button(search_frame,text="Search",width=17,font=("times new roman",12,"bold"))
        search_btn.grid(row=0,column=3,padx=4)

        show_btn=Button(search_frame,text="Show All",width=17,font=("times new roman",12,"bold"))
        show_btn.grid(row=0,column=4, padx=4)

        #tableframe
        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=20, y=170,width=610, height=140)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("dep","course","year","sem","name", "enroll", "gender", "dob", "email", "phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.xview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("enroll",text="Enrollment no.")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table["show"]="headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("enroll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
    


    #Func 
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_enroll.get() == " " or self.var_name.get() == " ":
           messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
           try:
            conn=mysql.connector.connect(host="localhost", username="root", password="Happysql@22", database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_sem.get(),
                                                        self.var_enroll.get(),
                                                        self.var_name.get(),                                                 
                                                        self.var_gender.get(),
                                                        self.var_DOB.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get()
                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
           except Exception as es:
              messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)


    
#fetch data
    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost", username="root", password="Happysql@22", database="face_recognition")
       my_cursor=conn.cursor()
       my_cursor.execute("SELECT * FROM student")
       data=my_cursor.fetchall()

       if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
              self.student_table.insert("",END,values=i)
          conn.commit()
       conn.close()


#get cursor
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0])
       self.var_course.set(data[1])
       self.var_year.set(data[2])
       self.var_sem.set(data[3])
       self.var_enroll.set(data[4])
       self.var_name.set(data[5])
       self.var_gender.set(data[6])
       self.var_DOB.set(data[7])
       self.var_email.set(data[8])
       self.var_phone.set(data[9])
   
#update
    def update_data(self):
     if self.var_dep.get() == "Select Department" or self.var_enroll.get() == "" or self.var_name.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
        try:
            Upadate = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if Upadate > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="Happysql@22", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, gender=%s, DOB=%s, email=%s, phone=%s WHERE Enroll=%s", (
                                                  self.var_dep.get(),
                                                  self.var_course.get(),
                                                  self.var_year.get(),
                                                  self.var_sem.get(),
                                                  self.var_gender.get(),
                                                  self.var_DOB.get(),
                                                  self.var_email.get(),
                                                  self.var_phone.get(),
                                                  self.var_enroll.get()  
                                                ))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            else:
                return
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


#delete
    def delete_data(self):
      if self.var_enroll.get()=="":
        messagebox.showerror("Error","Enrollment number must be required",parent=self.root)
      else:
        try:
            delete=messagebox.askyesno("Student delete page","Do you want to delete this details",parent=self.root)
            if delete>0:
                conn = mysql.connector.connect(host="localhost", username="root", password="Happysql@22", database="face_recognition")
                my_cursor = conn.cursor()
                sql="delete from student where enroll=%s"
                val=(self.var_enroll.get(),
                )
                my_cursor.execute(sql,val)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

  #reset          
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_enroll.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_phone.set("")


#generate
    def generate_dataset(self): 
      if self.var_dep.get() == "Select Department" or self.var_enroll.get() == "" or self.var_name.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try:
          conn = mysql.connector.connect(host="localhost", username="root", password="Happysql@22", database="face_recognition")
          my_cursor = conn.cursor()
          my_cursor.execute("Select * from student")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
             id+=1
             my_cursor.execute("UPDATE student SET Dep=%s, course=%s, year=%s, sem=%s, gender=%s, DOB=%s, email=%s, phone=%s WHERE Enroll=%s", (
                                                  self.var_dep.get(),
                                                  self.var_course.get(),
                                                  self.var_year.get(),
                                                  self.var_sem.get(),
                                                  self.var_gender.get(),
                                                  self.var_DOB.get(),
                                                  self.var_email.get(),
                                                  self.var_phone.get(),
                                                  self.var_enroll.get()==id+1 
                                                ))
             conn.commit()
             self.fetch_data()
             self.reset_data()
             conn.close()

    #load predefine data
             face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
             def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                #scaling factor=1.3
                #minimum neighbour=5

                for (x,y,w,h) in faces:
                   face_cropped=img[y:y+h, x:x+w]
                   return face_cropped
            
             cap=cv2.VideoCapture(0)
             img_id=0
             while True:
                ret, my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                   img_id+=1
                   face=cv2.resize(face_cropped(my_frame),(450,450))
                   face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                   file_name_path=r"data\user."+str(id)+"."+str(img_id)+".jpg"
                   cv2.imwrite(file_name_path,face)
                   cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                   cv2.imshow("Crpped Face",face)

                   if cv2.waitKey(1)==13 or int(img_id)==100:
                      break
             cap.release()
             cv2.destroyAllWindows()
             messagebox.showinfo("Result","Generating datasets completed")

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
