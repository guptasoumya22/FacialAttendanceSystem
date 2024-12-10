from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Management System")

        # Variables
        self.var_atten_enroll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dept = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        self.root.configure(bg="white")

        # Title Label
        title_lbl = Label(
            self.root,
            text="Attendance",
            font=("times new roman", 35, "bold"),
            bg="#003366",
            fg="white",
            relief=RIDGE,
            bd=10,
        )
        title_lbl.place(x=0, y=140, width=1366, height=70)

        # Header Image
        img1= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\header1.webp").resize((500,130), Image.Resampling.LANCZOS)
        img2= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\fas3.png").resize((500,130), Image.Resampling.LANCZOS)
        img3= Image.open(r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\header3.jpg").resize((500,130), Image.Resampling.LANCZOS)
        
        combined_width = img1.width + img2.width + img3.width
        combined_height = img1.height
        combined_img = Image.new("RGB", (combined_width, combined_height))
        combined_img.paste(img1, (0, 0))
        combined_img.paste(img2, (img1.width, 0))
        combined_img.paste(img3, (img1.width + img2.width, 0))
        self.photoimg = ImageTk.PhotoImage(combined_img)
        f_lbl = Label(self.root, image=self.photoimg, bd=0)
        f_lbl.place(x=20, y=20, width=combined_width, height=130)

        # Background Frame
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=220, width=1300, height=500)

        # Footer
        footer_lbl = Label(
            self.root,
            text="Developed by Team-47",
            font=("Helvetica", 15),
            bg="#003366",
            fg="white",
            bd=0,
        )
        footer_lbl.place(x=0, y=760, width=1530, height=30)

        # Left Frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            bg="white",
            fg="black",
            text="Student Information",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=630, height=470)

        # Enrollment
        enroll_label = Label(Left_frame, text="Enrollment No.", font=("times new roman", 12, "bold"))
        enroll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        enroll_entry = ttk.Entry(Left_frame, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"), width=17)
        enroll_entry.grid(row=0, column=3, padx=20, pady=5, sticky=W)

        # Name
        name_label = Label(Left_frame, text="Name", font=("times new roman", 12, "bold"))
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(Left_frame, textvariable=self.var_atten_enroll, font=("times new roman", 12, "bold"), width=17)
        name_entry.grid(row=0, column=1, padx=20, pady=5, sticky=W)

        # Date
        date_label = Label(Left_frame, text="Date", font=("times new roman", 12, "bold"))
        date_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(Left_frame, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"), width=17)
        date_entry.grid(row=1, column=1, padx=20, pady=5, sticky=W)

        # Attendance Status
        attendance_label = Label(Left_frame, text="Attendance Status", font=("times new roman", 12, "bold"))
        attendance_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(
            Left_frame, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), width=17, state="readonly"
        )
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=1, column=3, padx=20, pady=5, sticky=W)
        self.atten_status.current(0)

        # Time
        time_label = Label(Left_frame, text="Time", font=("times new roman", 12, "bold"))
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(Left_frame, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"), width=17)
        time_entry.grid(row=2, column=1, padx=20, pady=5, sticky=W)

        # Department
        dept_label = Label(Left_frame, text="Department", font=("times new roman", 12, "bold"))
        dept_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dept_entry = ttk.Entry(Left_frame, textvariable=self.var_atten_dept, font=("times new roman", 12, "bold"), width=17)
        dept_entry.grid(row=2, column=3, padx=20, pady=5, sticky=W)

        # Buttons
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=170, width=715, height=35)

        save_btn = Button(btn_frame, text="Import CSV", width=20, font=("times new roman", 12, "bold"), command=self.importCsv)
        save_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", width=20, font=("times new roman", 12, "bold"), command=self.exportCsv)
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=20, font=("times new roman", 12, "bold"))
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=20, font=("times new roman", 12, "bold"))
        reset_btn.grid(row=0, column=3)

        # Right Frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            bg="white",
            fg="black",
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=650, y=10, width=635, height=470)

        # Table Frame
        table_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=20, y=20, width=600, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            column=("name", "roll", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Functions
    def importCsv(self):
        global mydata
        mydata.clear()
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
        )
        try:
            with open(file_path, "r") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    mydata.append(row)
                self.fetch_data(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import CSV\n{e}")

    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data available to export.")
                return
            file_path = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                defaultextension=".csv",
            )
            with open(file_path, "w", newline="") as file:
                csvwriter = csv.writer(file)
                for row in mydata:
                    csvwriter.writerow(row)
            messagebox.showinfo("Export Successful", f"Data exported to {os.path.basename(file_path)} successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export CSV\n{e}")

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        if rows:
            self.var_atten_enroll.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_dept.set(rows[2])
            self.var_atten_time.set(rows[3])
            self.var_atten_date.set(rows[4])
            self.var_atten_attendance.set(rows[5])

    def reset_data(self):
        self.var_atten_enroll.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
