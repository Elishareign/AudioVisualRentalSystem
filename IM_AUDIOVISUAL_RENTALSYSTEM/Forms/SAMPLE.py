import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import hashlib
import sqlite3
from dashboard import Dashboard

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1555x800")
        self.root.configure(fg_color="#A3B18A")
        self.root.resizable(False, False)

        self.central_background_frame = ctk.CTkFrame(self.root, width=1500, height=750, corner_radius=32, fg_color="#B5C1A1")
        self.central_background_frame.place(relx=0.5, rely=0.5, anchor='center')

        login_frame = ctk.CTkFrame(root, width=360, height=500, corner_radius=32, fg_color="#FEFDED", bg_color="#B5C1A1")
        login_frame.place_configure(width=400, height=490, relx=0.5, rely=0.5, anchor='center')

        # Load and resize the logo image
        logo_image = Image.open("Resources/testinglogo1.png")
        logo_image = logo_image.resize((255, 170), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.logo_label = ctk.CTkLabel(master=login_frame, image=self.logo_photo, text="")
        self.logo_label.grid(row=0, column=0, padx=75, pady=(20, 5))

        # Username and password entry
        self.name_label = ctk.CTkLabel(master=login_frame, text="NAME", font=("DM sans", 14), text_color="black")
        self.name_label.grid(row=1, column=0, padx=70, pady=(0, 0), sticky="w")

        self.name_entry = ctk.CTkEntry(master=login_frame, width=270, height=35, fg_color="#D9D9D9", border_color="#D9D9D9", corner_radius=10,)
        self.name_entry.grid(row=2, column=0, padx=0, pady=5)

        self.password_label = ctk.CTkLabel(master=login_frame, text="PASSWORD", font=("DM sans", 14), text_color="black")
        self.password_label.grid(row=3, column=0, padx=70, pady=(10, 5), sticky="w")

        self.password_entry = ctk.CTkEntry(master=login_frame, width=270, height=35, font=("DM sans", 14), text_color="black", fg_color="#D9D9D9", border_color="#D9D9D9", corner_radius=10, show="*")
        self.password_entry.grid(row=4, column=0, padx=20, pady=5)

        # Login button
        self.login_button = ctk.CTkButton(master=login_frame, text="Log in", font=("DM sans", 14, "bold"), width=150, height=35, fg_color="#154734", hover_color="#588157", command=self.login)
        self.login_button.grid(row=5, column=0, padx=20, pady=(20, 10))

        # Forgot password button
        self.forgot_password_button = ctk.CTkButton(master=login_frame, text="Forgot Password?", font=("DM sans", 14, "bold"), text_color="#154734", fg_color="#FEFDED", hover_color="#FEFDED", command=self.forgot_password)
        self.forgot_password_button.grid(row=6, column=0, padx=20)

        # Initialize database connection
        self.conn = sqlite3.connect('RentalRecords.db')

        # Create users table if it doesn't exist
        self.create_users_table()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Instance method to create users table if it doesn't exist
    def create_users_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            ''')
            self.conn.commit()
            print("Users table created successfully or already exists.")
        except Exception as e:
            print(f"Error creating users table: {e}")

    def insert_initial_user(self):
        # Method to insert initial user, e.g., admin
        username = 'admin'
        password = 'adminpassword'  # Replace with an actual password
        hashed_password = self.hash_password(password)

        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
            print("Initial user inserted successfully.")
        except Exception as e:
            print(f"Error inserting initial user: {e}")

    def login(self):
        username = self.name_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)

        conn = sqlite3.connect('RentalRecords.db')
        cursor = conn.cursor()

        # Check if the username and hashed password match
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        result = cursor.fetchone()

        if result:
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        conn.close()

    def open_dashboard(self):
        self.root.destroy()
        root = ctk.CTk()
        app = Dashboard(root)
        root.mainloop()

    def forgot_password(self):
        forgot_password_window = ctk.CTkToplevel()
        forgot_password_window.title("Forgot Password")
        forgot_password_window.geometry("400x300")
        forgot_password_window.configure(fg_color="#A3B18A")

        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        forgot_password_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        forgot_password_window.attributes('-topmost', True)

        message_label = ctk.CTkLabel(forgot_password_window, text="Change Password", font=("century gothic", 18), text_color="black")
        message_label.pack(pady=20)

        new_password_label = ctk.CTkLabel(forgot_password_window, text="New Password", font=("century gothic", 13), text_color="black")
        new_password_label.pack(pady=5, padx=80, anchor='w')

        new_password = ctk.CTkEntry(forgot_password_window, font=("century gothic", 13), text_color="black", width=250, show="*")
        new_password.pack(pady=5)

        confirm_password_label = ctk.CTkLabel(forgot_password_window, text="Confirm Password", font=("century gothic", 13), text_color="black")
        confirm_password_label.pack(pady=5, padx=80, anchor='w')

        confirm_password = ctk.CTkEntry(forgot_password_window, font=("century gothic", 13), text_color="black", width=250, show="*")
        confirm_password.pack(pady=5)

        save_changes = ctk.CTkButton(forgot_password_window, text="Save Changes", fg_color="#154734", hover_color="#588157", command=lambda: self.save_new_password(new_password, confirm_password, forgot_password_window))
        save_changes.pack(pady=20)

    def save_new_password(self, new_password, confirm_password, window):
        new_password_value = new_password.get()
        confirm_password_value = confirm_password.get()

        if len(new_password_value) < 8:
            messagebox.showerror("Error", "Password should be at least 8 characters long.")
            return

        if new_password_value == confirm_password_value:
            hashed_password = self.hash_password(new_password_value)

            conn = sqlite3.connect('RentalRecords.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET password=? WHERE username=?", (hashed_password, 'admin'))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Password changed successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Passwords do not match.")
