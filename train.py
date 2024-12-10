# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import cv2
# import os
# import numpy as np


# class Train:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Student Management System")
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
#         header_lbl = Label(self.root, image=self.photoimg, bd=0)
#         header_lbl.place(x=20, y=20, width=combined_width, height=130)

#         # Title Label
#         title_lbl = Label(self.root, text="Train Data",
#                           font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
#         title_lbl.place(x=0, y=140, width=1366, height=70)

#         # Main Frame with Background Image
#         bg_image_path = r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\main_bg.jpg"
#         bg_image = Image.open(bg_image_path).resize((1300, 500), Image.Resampling.LANCZOS)
#         self.bg_photo = ImageTk.PhotoImage(bg_image)

#         main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
#         main_frame.place(x=30, y=220, width=1300, height=500)

#         bg_label = Label(main_frame, image=self.bg_photo)
#         bg_label.image = self.bg_photo  # Keep reference to avoid garbage collection
#         bg_label.place(x=0, y=0, width=1300, height=500)

#         # Train Data Button
#         btn_style = {
#             'font': ("times new roman", 20, "bold"),
#             'bg': "#003366",
#             'fg': "white",
#             'relief': RIDGE,
#             'bd': 10,
#         }

#         train_btn = Button(main_frame, text="Train Data", **btn_style, command=self.train_classifier)
#         train_btn.place(relx=0.5, rely=0.9, anchor=CENTER)  # Place at center bottom

#         # Footer
#         footer_lbl = Label(self.root, text="Developed by Team-47",
#                            font=("Helvetica", 15), bg="#003366", fg="white", bd=0)
#         footer_lbl.place(x=0, y=760, width=1366, height=30)

#     def train_classifier(self):
#         data_dir = "data"
#         path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
#         faces = []
#         ids = []

#         for image_path in path:
#             try:
#                 img = Image.open(image_path).convert("L")
#                 imageNp = np.array(img, "uint8")

#                 file_name_parts = os.path.split(image_path)[1].split('.')
#                 if len(file_name_parts) > 2 and file_name_parts[1].isdigit():
#                     id = int(file_name_parts[1])
#                 else:
#                     print(f"Skipping file '{image_path}' (invalid ID format)")
#                     continue

#                 faces.append(imageNp)
#                 ids.append(id)

#                 cv2.imshow("Training", imageNp)
#                 cv2.waitKey(1)

#             except Exception as e:
#                 print(f"Error processing file '{image_path}': {e}")
#                 continue

#         if not faces or not ids:
#             messagebox.showerror("Error", "No valid training data found!")
#             return

#         try:
#             clf = cv2.face.LBPHFaceRecognizer_create()
#             clf.train(faces, np.array(ids))
#             clf.write("classifier.xml")
#             cv2.destroyAllWindows()
#             messagebox.showinfo("Result", "Training Datasets Completed.")
#         except Exception as e:
#             messagebox.showerror("Error", f"Training failed: {e}")


# if __name__ == "__main__":
#     root = Tk()
#     obj = Train(root)
#     root.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")
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
        header_lbl = Label(self.root, image=self.photoimg, bd=0)
        header_lbl.place(x=20, y=20, width=combined_width, height=130)

        # Title Label
        title_lbl = Label(self.root, text="Train Data",
                          font=("Helvetica", 35, "bold"), bg="#003366", fg="white", relief=RIDGE, bd=10)
        title_lbl.place(x=0, y=140, width=1366, height=70)

        # Main Frame with Background Image
        bg_image_path = r"C:\Users\hp\Desktop\FacialAttendanceSystem\images\main_bg.jpg"
        bg_image = Image.open(bg_image_path).resize((1300, 500), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=30, y=220, width=1300, height=500)

        bg_label = Label(main_frame, image=self.bg_photo)
        bg_label.image = self.bg_photo  # Keep reference to avoid garbage collection
        bg_label.place(x=0, y=0, width=1300, height=500)

        # Train Data Button
        btn_style = {
            'font': ("times new roman", 20, "bold"),
            'bg': "#003366",
            'fg': "white",
            'relief': RIDGE,
            'bd': 10,
        }

        train_btn = Button(main_frame, text="Train Data", **btn_style, command=self.train_classifier)
        train_btn.place(relx=0.5, rely=0.9, anchor=CENTER)  # Place at center bottom

        # Footer
        footer_lbl = Label(self.root, text="Developed by Team-47",
                           font=("Helvetica", 15), bg="#003366", fg="white", bd=0)
        footer_lbl.place(x=0, y=760, width=1366, height=30)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert("L")
                imageNp = np.array(img, "uint8")

                file_name_parts = os.path.split(image_path)[1].split('.')
                if len(file_name_parts) > 2 and file_name_parts[1].isdigit():
                    id = int(file_name_parts[1])
                else:
                    print(f"Skipping file '{image_path}' (invalid ID format)")
                    continue

                faces.append(imageNp)
                ids.append(id)

                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)

            except Exception as e:
                print(f"Error processing file '{image_path}': {e}")
                continue

        if not faces or not ids:
            messagebox.showerror("Error", "No valid training data found!")
            return

        # Fix: Check for cv2.face module and use it
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            messagebox.showerror(
                "Error",
                "cv2.face module not found. Ensure 'opencv-contrib-python' is installed.",
            )
            return

        try:
            clf.train(faces, np.array(ids))
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Datasets Completed.")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {e}")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

