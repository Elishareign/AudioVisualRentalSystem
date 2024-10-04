from tkinter import Tk, messagebox
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
from datetime import datetime
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os
from rentalForm import Rental
from packageForm import Package
from equipmentForm import Equipment
from reportForm import Report
from paymentForm import Payment

class Dashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Dashboard")
        self.master.geometry("1555x800")
        self.master.configure(bg_color="#fefded")
        self.master.resizable(False, False)
        self.active_button = None  # Track the currently active button
        self.create_widgets()

    def create_widgets(self):
        self.option_frame = ctk.CTkFrame(self.master, border_color='#D9D9D9', fg_color='#fefded', corner_radius=0, border_width=2)
        self.option_frame.pack(side=ctk.LEFT, fill=ctk.Y)

        # Print the current working directory for debugging
        print("Current working directory:", os.getcwd())

        # Load images
        self.load_images()

        # Add logo image at the top of the option frame
        self.create_logo("testinglogo1.png", 80)

        # Option buttons
        self.create_button("home.png", self.homepage, 165, "home")
        self.create_button("rentals.png", self.Rental, 227, "rentals")
        self.create_button("packages.png", self.Package, 295, "packages")
        self.create_button("equipment.png", self.Equipment, 359, "equipment")
        self.create_button("payments.png", self.Payment, 420, "payments")
        self.create_button("reports.png", self.Report, 490, "reports")
        self.create_button("logout.png", self.logout, 700, "logout")

        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width=100, height=800)

        self.main_frame = ctk.CTkFrame(self.master, bg_color="#fefded", corner_radius=0)
        self.main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=800, width=1490)

        self.homepage()

    def load_images(self):
        images = [
            ("testinglogo1.png", (150, 80)),
            ("home.png", (500, 500)),
            ("packages.png", (500, 500)),
            ("rentals.png", (500, 500)),
            ("equipment.png", (500, 500)),
            ("payments.png", (500, 500)),
            ("reports.png", (500, 500)),
            ("logout.png", (500, 500))
        ]

        self.photo_images = {}
        for image_filename, size in images:
            image_path = os.path.join("Resources", image_filename)
            if os.path.exists(image_path):
                image = Image.open(image_path).resize(size, Image.LANCZOS)
                self.photo_images[image_filename] = CTkImage(dark_image=image)
            else:
                messagebox.showerror("Image Error", f"Image {image_filename} not found in 'Resources' folder.")

    def create_logo(self, image_filename, y_pos):
        if image_filename in self.photo_images:
            logo_label = ctk.CTkLabel(self.option_frame, image=self.photo_images[image_filename], text="")
            logo_label.place(x=10, y=y_pos)

    def create_button(self, image_filename, command, y_pos, name):
        if image_filename in self.photo_images:
            button = ctk.CTkButton(self.option_frame, image=self.photo_images[image_filename], text="", fg_color="#fefded", border_width=0, hover_color="#A3B18A", width=95, height=50, command=lambda: self.on_button_click(name, command))
            button.place(x=2, y=y_pos)
            button.name = name
            setattr(self, f"{name}_button", button)


    def on_button_click(self, name, command):
        if self.active_button:
            self.active_button.configure(fg_color="#fefded")  # Reset the previous active button color

        # Set the new active button
        self.active_button = getattr(self, f"{name}_button")
        self.active_button.configure(fg_color="#A3B18A")  # Change the color of the clicked button
        command()


    def homepage(self):
        
        self.clear_main_frame()

        homepage_fm = ctk.CTkFrame(self.main_frame, fg_color='#fefded')
        homepage_fm.pack(fill=ctk.BOTH, expand=True)

        header_frame = ctk.CTkFrame(homepage_fm, fg_color='#fefded')
        header_frame.pack(fill=ctk.X, pady=10, padx=20)

        homepage_lb = ctk.CTkLabel(header_frame, text='Dashboard', font=('Century Gothic bold', 30), text_color='#154734')
        homepage_lb.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        DateTime = ctk.CTkLabel(header_frame, text="", font=('Century Gothic', 20), text_color='#154734')
        DateTime.grid(row=0, column=0, pady=20, sticky='e')

        header_frame.columnconfigure(1, weight=1)

        def updateTime():
            now = datetime.now()
            formatted_time = now.strftime("%A: %B %d, %Y, %I:%M %p")
            DateTime.configure(text=formatted_time)
            homepage_fm.after(1000, updateTime)
        
        updateTime()
        
        container_frame = ctk.CTkFrame(homepage_fm, fg_color='#fefded')
        container_frame.pack(pady=20, padx=20, anchor='n', fill=ctk.X)

        left_frame = ctk.CTkFrame(container_frame, fg_color='#fefded')
        left_frame.pack(pady=10, padx=10, anchor='n', side='left', fill=ctk.Y, expand=True)

        upcoming_event_frame = ctk.CTkFrame(left_frame, fg_color='#F1F1F1', corner_radius=5, width=1000, height=250)
        upcoming_event_frame.pack(pady=0, padx=0, anchor='n', fill=ctk.X, expand=True)
        upcoming_event_frame.pack_propagate(False)

        event_info_frame = ctk.CTkFrame(upcoming_event_frame, fg_color='#F1F1F1')
        event_info_frame.pack(pady=1, padx=2, anchor='center', fill=ctk.X)

        total_events_label = ctk.CTkLabel(event_info_frame, text='Total of Rentals', font=('Century Gothic bold', 20), text_color='#154734')
        total_events_label.grid(row=0, column=0, pady=20, padx=100, sticky='w')

        total_events_entry = ctk.CTkEntry(event_info_frame, state='readonly', font=('Century Gothic bold', 15), fg_color='#F1F1F1', border_width=0, text_color='#154734', height=90, width=100)
        total_events_entry.grid(row=1, column=0, pady=0, padx=120, sticky='w')

        pending_label = ctk.CTkLabel(event_info_frame, text='Pending Payments', font=('Century Gothic bold', 20), text_color='#154734')
        pending_label.grid(row=0, column=2, pady=15, padx=80, sticky='w')

        pending_entry = ctk.CTkEntry(event_info_frame, state='readonly', font=('Century Gothic bold', 20), fg_color='#F1F1F1', border_width=0, text_color='#154734', height=90, width=100)
        pending_entry.grid(row=1, column=2, pady=5, padx=120, sticky='w')

        earnings_frame = ctk.CTkFrame(left_frame, fg_color='#fefded', corner_radius=5, width=1000, height=360)
        earnings_frame.pack(pady=10, padx=0, anchor='n', fill=ctk.X, expand=True)
        earnings_frame.pack_propagate(False)

        earnings_label = ctk.CTkLabel(earnings_frame, text='Earnings', font=('Century Gothic bold', 35), text_color='#154734')
        earnings_label.pack(pady=6, padx=20, anchor='w')

        fig, ax = plt.subplots(figsize=(10, 3))
        fig.patch.set_facecolor('#fefded')
        ax.set_facecolor('#fefded')

        data = [10, 20, 30, 40, 50]
        labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        ax.bar(labels, data, color='#154734')

        ax.set_title('Monthly Earnings', color='#154734')
        ax.set_xlabel('Month', color='#154734')
        ax.set_ylabel('Earnings', color='#154734')
        ax.tick_params(axis='x', colors='#154734')
        ax.tick_params(axis='y', colors='#154734')

        canvas = FigureCanvasTkAgg(fig, master=earnings_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        rentals_frame = ctk.CTkFrame(container_frame, fg_color='#F1F1F1', corner_radius=20, width=300)
        rentals_frame.pack(pady=10, padx=10, anchor='n', side='left', fill=ctk.Y, expand=True)
        rentals_frame.pack_propagate(False)

        rentals_label = ctk.CTkLabel(rentals_frame, text='Rentals', font=('Century Gothic bold', 30), text_color='#154734')
        rentals_label.pack(pady=6, padx=20, anchor='w')

        for i in range(5):
            rental_item = ctk.CTkLabel(rentals_frame, text=f'Customer Name | Equipment\n1 July 2024 00:00 PM - 1 July 2024 00:00 PM', font=('Century Gothic', 15), text_color='#154734')
            rental_item.pack(pady=5, padx=20, anchor='w')

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def Rental(self):
        self.clear_main_frame()
        Rental(self.main_frame)  # Pass self.main_frame to Rental

    def Package(self):
        self.clear_main_frame()
        Package(self.main_frame)  # Pass self.main_frame to Package

    def Equipment(self):
        self.clear_main_frame()
        Equipment(self.main_frame)  # Pass self.main_frame to Equipment

    def Payment(self):
        self.clear_main_frame()
        Payment(self.main_frame)  # Pass self.main_frame to Payment

    def Report(self):
        self.clear_main_frame()
        Report(self.main_frame)  # Pass self.main_frame to Report

    def logout(self):
        pass

    def switch(self, page_function):
        self.clear_main_frame()
        page_function()

if __name__ == "_main_":
    root = Tk()
    app = Dashboard(root)
    root.mainloop()