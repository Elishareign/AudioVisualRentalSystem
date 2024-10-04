import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import *
import hashlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import ttk
from datetime import datetime
import random
from tkcalendar import DateEntry
from dashboard import Dashboard



class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1555x800")
        self.root.configure(fg_color="#A3B18A")
        self.root.resizable(False, False)

        self.central_background_frame = ctk.CTkFrame(root, width=1400, height=700, corner_radius=10, fg_color="#B5C1A1")
        self.central_background_frame.place(relx=0.5, rely=0.5, anchor='center')

        login_frame = ctk.CTkFrame(root, width=360, height=500, corner_radius=10, fg_color="white")
        login_frame.place_configure(width=400, height=490, relx=0.5, rely=0.5, anchor='center')

        # Load and resize the logo image
        logo_image = Image.open("Resources/testinglogo.png")
        logo_image = logo_image.resize((150, 150), Image.LANCZOS)  
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.logo_label = ctk.CTkLabel(master=login_frame, image=self.logo_photo, text="")
        self.logo_label.grid(row=0, column=0, padx=125, pady=(20, 5))

        self.title_label = ctk.CTkLabel(master=login_frame, text="TRANSIENT", font=("century gothic", 20, "bold"), text_color="black")
        self.title_label.grid(row=1, column=0, padx=150, pady=(5, 5))

        # Username and password entry
        self.name_label = ctk.CTkLabel(master=login_frame, text="Name", font=("century gothic", 13, "bold"), text_color="black")
        self.name_label.grid(row=2, column=0, padx=100, pady=(10, 5), sticky="w")

        self.name_entry = ctk.CTkEntry(master=login_frame, width=200, fg_color="white")
        self.name_entry.grid(row=3, column=0, padx=0, pady=5)

        self.password_label = ctk.CTkLabel(master=login_frame, text="Password", font=("century gothic", 13, "bold"), text_color="black")
        self.password_label.grid(row=4, column=0, padx=100, pady=(10, 5), sticky="w")

        self.password_entry = ctk.CTkEntry(master=login_frame, width=200, fg_color="white", show="*")
        self.password_entry.grid(row=5, column=0, padx=20, pady=5)

        # Login button
        self.login_button = ctk.CTkButton(master=login_frame, text="Log in", fg_color="#154734", hover_color="#588157", command=self.login)
        self.login_button.grid(row=6, column=0, padx=20, pady=(20, 10))

        # Forgot password button
        self.forgot_password_button = ctk.CTkButton(master=login_frame, text="Forgot Password?", font=("century gothic", 13, "bold"), text_color="#154734", fg_color="white", hover_color="white", command=self.forgot_password)
        self.forgot_password_button.grid(row=7, column=0, padx=20, pady=(10, 20))

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        username = self.name_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)

        # Dummy check for username and hashed password
        if username == "admin" and hashed_password == self.hash_password("admin"):
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    
    def open_dashboard(self):
        self.root.destroy()
        root = ctk.CTk()
        app = Dashboard(root)
        root.mainloop()
        
    def forgot_password(self):
        # Create a new window for forgot password
        forgot_password_window = ctk.CTkToplevel()
        forgot_password_window.title("Forgot Password")
        forgot_password_window.geometry("400x400")
        forgot_password_window.configure(fg_color="#A3B18A")

        # Calculate the center position relative to self.root
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        forgot_password_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set window on top
        forgot_password_window.attributes('-topmost', True)

        # Add your forgot password widgets here
        message_label = ctk.CTkLabel(forgot_password_window, text="Change Password", font=("century gothic", 18), text_color="black")
        message_label.pack(pady=20)

        new_password_label = ctk.CTkLabel(forgot_password_window, text="New Password", font=("century gothic", 13), text_color="black")
        new_password_label.pack(pady=5, padx = 80  , anchor = W )

        new_password = ctk.CTkEntry(forgot_password_window, font=("century gothic", 13), text_color="black" , width= 250)
        new_password.pack(pady=5)

        confirm_password_label = ctk.CTkLabel(forgot_password_window, text="Confirm Password", font=("century gothic", 13), text_color="black")
        confirm_password_label.pack(pady=5, padx = 80  , anchor = W )

        confirm_password = ctk.CTkEntry(forgot_password_window, font=("century gothic", 13), text_color="black" , width= 250)
        confirm_password.pack(pady=5)

        save_changes = ctk.CTkButton(forgot_password_window, text="Save Changes", fg_color="#154734", hover_color="#588157")
        save_changes.pack(pady=20)

def main():
    root = ctk.CTk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
