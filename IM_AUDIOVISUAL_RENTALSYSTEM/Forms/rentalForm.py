from tkinter import Tk, Toplevel, ttk
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
import sqlite3

class Rental(ctk.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.main_frame = ctk.CTkFrame(self.master)
    
        # Create the main frame for scheduling with specified height
        schedule_fm = ctk.CTkFrame(self.master, fg_color='#fefded', height=800)
        schedule_fm.pack(fill='both', expand=True)
        
        # Ensure the main frame expands to fill the space
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Date and Time update function
        def updateTime():
            now = datetime.now()
            formatted_time = now.strftime("%A: %B %d, %Y, %I:%M%p")
            DateTime.configure(text=formatted_time)
            schedule_fm.after(1000, updateTime)
        
        # Title
        rentals = ctk.CTkLabel(schedule_fm, text="Rentals", font=('Century Gothic', 30, 'bold'), text_color='#154734')
        rentals.grid(row=1, column=0, padx=60, pady=20, sticky='w')

        DateTime = ctk.CTkLabel(schedule_fm, text="", font=('Century Gothic', 20, 'bold'), text_color='#154734')
        DateTime.grid(row=1, column=0, padx=1100, pady=20, sticky='w')
        updateTime()

        # Search Rentals
        SearchLabel = ctk.CTkLabel(schedule_fm, text="Search:", text_color='#154734', font=('Century Gothic', 20, 'bold'))
        SearchLabel.grid(row=2, column=0, padx=400, pady=0, sticky='w')
        SearchEntry = ctk.CTkEntry(schedule_fm, width=370, font=('Century Gothic', 20), placeholder_text="Search Rentals...")
        SearchEntry.grid(row=2, column=0, padx=490, pady=10, sticky='w')
        SearchButton = ctk.CTkButton(schedule_fm, text="Search", font=('Century Gothic', 20, 'bold'), fg_color='#154734', text_color='white', hover_color='gray')
        SearchButton.grid(row=2, column=0, padx=870, pady=10, sticky='w')

        def connect_db(timeout=5000):
            conn = sqlite3.connect('RentalRecords.db', timeout=timeout)
            return conn

        # Function to create database tables if they don't exist
        def create_tables(conn):
            cursor = conn.cursor()
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                LastName TEXT, FirstName TEXT, MiddleName TEXT, 
                Address TEXT, ContactNo TEXT, EmailAddress TEXT)''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                EventName TEXT, EventLocation TEXT, EventDate TEXT, 
                CustomerID INTEGER,
                FOREIGN KEY (CustomerID) REFERENCES Customer(id))''')
            
            conn.commit()

        # Example usage:
        try:
            conn = connect_db(timeout=5000)  # Set a timeout of 5 seconds (5000 milliseconds)
            create_tables(conn)
            conn.close()
            print("Database and tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")

        def create_rental_window():
            create_window = CTkToplevel()
            create_window.title("RENTAL FORM")
            create_window.geometry("1100x700")
            create_window.configure(fg_color='#fefded')
            set_appearance_mode('light')
            create_window.grab_set()
            create_window.resizable(False, False)

            def BackRental():
                create_window.destroy()
                windows.deiconify()
                windows.lift()

            # BACK BUTTON
            BackButton = CTkButton(create_window, text="BACK", font=('Century Gothic', 20, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10, command=BackRental)
            BackButton.grid(row=0, column=0, padx=25, pady=20, sticky='w')

            # MAIN FRAME
            frame1 = CTkScrollableFrame(create_window, fg_color='#f1f1f1', width=950, height=950)
            frame1.grid(row=1, column=0, padx=25, pady=25, sticky='nsew')

            create_window.grid_rowconfigure(1, weight=1)
            create_window.grid_columnconfigure(0, weight=1)

            # TITLE
            RentalForm = CTkLabel(frame1, text="Rental Form", text_color='#154734', font=('Century Gothic', 28, 'bold'))
            RentalForm.grid(row=0, column=0, padx=25, pady=10, sticky='w')

            # LNAME
            CustLName = CTkLabel(frame1, text="LAST NAME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            CustLName.grid(row=1, column=0, padx=25, pady=10, sticky='w')
            CustLNameEntry = CTkEntry(frame1, width=200, font=('Century Gothic', 18), placeholder_text="Last Name")
            CustLNameEntry.grid(row=1, column=0, padx=130, pady=10, sticky='w')

            # FNAME
            CustFName = CTkLabel(frame1, text="FIRST NAME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            CustFName.grid(row=1, column=0, padx=350, pady=10, sticky='w')
            CustFNameEntry = CTkEntry(frame1, width=200, font=('Century Gothic', 18), placeholder_text="First Name")
            CustFNameEntry.grid(row=1, column=0, padx=460, pady=10, sticky='w')

            # MNAME
            CustMName = CTkLabel(frame1, text="MIDDLE NAME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            CustMName.grid(row=1, column=0, padx=680, pady=10, sticky='w')
            CustMNameEntry = CTkEntry(frame1, width=200, font=('Century Gothic', 18), placeholder_text="Middle Name")
            CustMNameEntry.grid(row=1, column=0, padx=810, pady=10, sticky='w')

            # EVENT
            Event = CTkLabel(frame1, text="EVENT:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Event.grid(row=2, column=0, padx=550, pady=10, sticky='w')
            EventEntry = CTkEntry(frame1, width=400, font=('Century Gothic', 18), placeholder_text="Enter Event Name...")
            EventEntry.grid(row=2, column=0, padx=620, pady=10, sticky='w')

            # ADDRESS
            AddressEntry = CTkLabel(frame1, text="ADDRESS:", text_color='black', font=('Century Gothic', 18, 'bold'))
            AddressEntry.grid(row=2, column=0, padx=25, pady=10, sticky='w')
            AddressEntryField = CTkEntry(frame1, width=400, font=('Century Gothic', 18), placeholder_text="Enter Address...")
            AddressEntryField.grid(row=2, column=0, padx=110, pady=10, sticky='w')

            # EVENT LOCATION
            Loc = CTkLabel(frame1, text="EVENT LOCATION:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Loc.grid(row=3, column=0, padx=550, pady=10, sticky='w')
            LocEntry = CTkEntry(frame1, width=300, font=('Century Gothic', 18), placeholder_text="Enter Event Location...")
            LocEntry.grid(row=3, column=0, padx=720, pady=10, sticky='w')

            # EVENT DATE
            EventDate = CTkLabel(frame1, text="EVENT DATE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            EventDate.grid(row=4, column=0, padx=550, pady=10, sticky='w')
            EventDateEntry = DateEntry(frame1, width=15, font=('Century Gothic', 14, 'bold'), background='#154734', foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
            EventDateEntry.grid(row=4, column=0, padx=670, pady=10, sticky='w')

            # RENTAL DATE
            RentalDate = CTkLabel(frame1, text="RENTAL DATE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            RentalDate.grid(row=5, column=0, padx=550, pady=10, sticky='w')
            RentalDateEntry = DateEntry(frame1, width=11, font=('Century Gothic', 14, 'bold'), background='#154734', foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
            RentalDateEntry.grid(row=5, column=0, padx=670, pady=10, sticky='w')

            # RENTAL TIME
            RentalTime = CTkLabel(frame1, text="TIME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            RentalTime.grid(row=5, column=0, padx=820, pady=10, sticky='w')
            RentalTimeEntry = CTkEntry(frame1, width=150, font=('Century Gothic', 18), placeholder_text="00:00H")
            RentalTimeEntry.grid(row=5, column=0, padx=870, pady=10, sticky='w')

            # EMAIL
            Email = CTkLabel(frame1, text="EMAIL:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Email.grid(row=4, column=0, padx=25, pady=10, sticky='w')
            EmailEntry = CTkEntry(frame1, width=410, font=('Century Gothic', 18), placeholder_text="Enter Email Address...")
            EmailEntry.grid(row=4, column=0, padx=100, pady=10, sticky='w')

            # RETURN DATE
            ReturnDate = CTkLabel(frame1, text="RETURN DATE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            ReturnDate.grid(row=6, column=0, padx=550, pady=10, sticky='w')
            ReturnDateEntry = DateEntry(frame1, width=11, font=('Century Gothic', 14, 'bold'), background='#154734', foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
            ReturnDateEntry.grid(row=6, column=0, padx=670, pady=10, sticky='w')

            # RETURN TIME
            ReturnTime = CTkLabel(frame1, text="TIME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            ReturnTime.grid(row=6, column=0, padx=820, pady=10, sticky='w')
            ReturnTimeEntry = CTkEntry(frame1, width=150, font=('Century Gothic', 18), placeholder_text="00:00H")
            ReturnTimeEntry.grid(row=6, column=0, padx=870, pady=10, sticky='w')

            separator = ttk.Separator(frame1, orient='horizontal')
            separator.grid(row=7, column=0, columnspan=2, pady=10, sticky='ew')

            # PACKAGE
            Package = CTkLabel(frame1, text="PACKAGE", text_color='#154734', font=('Century Gothic', 20, 'bold'))
            Package.grid(row=8, column=0, padx=50, pady=10, sticky='w')

            def SaveData():
                LastName = CustLNameEntry.get()
                FirstName = CustFNameEntry.get()
                MiddleName = CustMNameEntry.get()
                Address = AddressEntryField.get()
                ContactNo = PhoneEntry.get()
                EmailAddress = EmailEntry.get()
                EventName = EventEntry.get()
                EventLocation = LocEntry.get()
                EventDate = EventDateEntry.get()

                if not all([LastName, FirstName, MiddleName, Address, ContactNo, EmailAddress, EventName, EventLocation, EventDate]):
                    messagebox.showerror("Form Error", "Please fill out all fields.")
                    return

                try:
                    conn = connect_db()
                    cursor = conn.cursor()
                    
                    cursor.execute('''
                        INSERT INTO Customer (LastName, FirstName, MiddleName, Address, ContactNo, EmailAddress)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (LastName, FirstName, MiddleName, Address, ContactNo, EmailAddress))
                    
                    CustomerID = cursor.lastrowid
                    
                    cursor.execute('''
                        INSERT INTO Event (EventName, EventLocation, EventDate, CustomerID)
                        VALUES (?, ?, ?, ?)
                    ''', (EventName, EventLocation, EventDate, CustomerID))
                    
                    conn.commit()
                    conn.close()
                    
                    messagebox.showinfo("Success", "Data saved successfully.")
                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

            # SAVE BUTTON
            SaveButton = CTkButton(frame1, text="SAVE", font=('Century Gothic', 20, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10, command=SaveData)
            SaveButton.grid(row=10, column=0, padx=25, pady=20, sticky='w')

            # PHONE
            Phone = CTkLabel(frame1, text="PHONE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Phone.grid(row=3, column=0, padx=25, pady=10, sticky='w')
            PhoneEntry = CTkEntry(frame1, width=100, font=('Century Gothic', 18), placeholder_text="Enter Phone Number")
            PhoneEntry.grid(row=3, column=0, padx=120, pady=10, sticky='w')

            windows = create_window

            create_window.mainloop()

        # Update Rental Window Function
        def update_rental_window():
            update_window = CTkToplevel()
            update_window.title("Update Rental")
            update_window.geometry("1100x700")
            update_window.configure(fg_color='#fefded')
            set_appearance_mode('light')
            update_window.grab_set() 
            update_window.resizable(False, False)

            # BACK BUTTON
            BackButton = CTkButton(update_window, text="Back", font=('Century Gothic', 21, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10)
            BackButton.grid(row=0, column=0, padx=25, pady=20, sticky='w')

            # MAIN FRAME
            frame1 = CTkScrollableFrame(update_window, fg_color='#f1f1f1', width=950, height=950)
            frame1.grid(row=1, column=0, padx=25, pady=25, sticky='nsew')

            update_window.grid_rowconfigure(1, weight=1)
            update_window.grid_columnconfigure(0, weight=1)

            # TITLE
            RentalForm = CTkLabel(frame1, text="Rental Form", text_color='#154734', font=('Century Gothic', 28, 'bold'))
            RentalForm.grid(row=0, column=0, padx=25, pady=10, sticky='w')

            # NAME
            CustName = CTkLabel(frame1, text="NAME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            CustName.grid(row=1, column=0, padx=25, pady=10, sticky='w')
            CustName = CTkEntry(frame1, width=420, font=('Century Gothic', 18), placeholder_text="Last Name, First Name, Middle Name")
            CustName.grid(row=1, column=0, padx=90, pady=10, sticky='w')

            # EVENT
            Event = CTkLabel(frame1, text="EVENT:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Event.grid(row=1, column=0, padx=550, pady=10, sticky='w')
            Event = CTkEntry(frame1, width=400, font=('Century Gothic', 18), placeholder_text="Enter Event Name...")
            Event.grid(row=1, column=0, padx=620, pady=10, sticky='w')

            # ADDRESS
            Address = CTkLabel(frame1, text="ADDRESS:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Address.grid(row=2, column=0, padx=25, pady=10, sticky='w')
            Address = CTkEntry(frame1, width=400, font=('Century Gothic', 18), placeholder_text="Enter Address...")
            Address.grid(row=2, column=0, padx=110, pady=10, sticky='w')

            # EVENT LOCATION
            Loc = CTkLabel(frame1, text="EVENT LOCATION:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Loc.grid(row=2, column=0, padx=550, pady=10, sticky='w')
            Loc = CTkEntry(frame1, width=300, font=('Century Gothic', 18), placeholder_text="Enter Event Location...")
            Loc.grid(row=2, column=0, padx=720, pady=10, sticky='w')
            
            # EVENT DATE
            EventDate = CTkLabel(frame1, text="EVENT DATE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            EventDate.grid(row=3, column=0, padx=550, pady=10, sticky='w')
            EventDate = DateEntry(frame1, width=15, font=('Century Gothic', 14, 'bold'), background='#154734', foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
            EventDate.grid(row=3, column=0, padx=670, pady=10, sticky='w')

            # NUMBER
            Phone = CTkLabel(frame1, text="PHONE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Phone.grid(row=3, column=0, padx=25, pady=10, sticky='w')
            Phone = CTkEntry(frame1, width=410, font=('Century Gothic', 18), placeholder_text="Enter Phone Number...")
            Phone.grid(row=3, column=0, padx=100, pady=10, sticky='w')

            # RENTAL DATE
            RentalDate = CTkLabel(frame1, text="RENTAL DATE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            RentalDate.grid(row=4, column=0, padx=550, pady=10, sticky='w')
            RentalDate = DateEntry(frame1, width=11, font=('Century Gothic', 14, 'bold'), background='#154734', foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
            RentalDate.grid(row=4, column=0, padx=670, pady=10, sticky='w')
            
            # RENTAL TIME
            RentalTime = CTkLabel(frame1, text="TIME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            RentalTime.grid(row=4, column=0, padx=820, pady=10, sticky='w')
            RentalTime = CTkEntry(frame1, width=150, font=('Century Gothic', 18), placeholder_text="00:00H")
            RentalTime.grid(row=4, column=0, padx=870, pady=10, sticky='w')

            # EMAIL
            Email = CTkLabel(frame1, text="EMAIL:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Email.grid(row=4, column=0, padx=25, pady=10, sticky='w')
            Email = CTkEntry(frame1, width=410, font=('Century Gothic', 18), placeholder_text="Enter Email Address...")
            Email.grid(row=4, column=0, padx=100, pady=10, sticky='w')

            # RETURN DATE
            ReturnDate = CTkLabel(frame1, text="RETURN DATE:", text_color='black', font=('Century Gothic', 18, 'bold'))
            ReturnDate.grid(row=5, column=0, padx=550, pady=10, sticky='w')
            ReturnDate = DateEntry(frame1, width=11, font=('Century Gothic', 14, 'bold'), background='#154734', foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
            ReturnDate.grid(row=5, column=0, padx=670, pady=10, sticky='w')
            
            # RETURN TIME
            ReturnTime = CTkLabel(frame1, text="TIME:", text_color='black', font=('Century Gothic', 18, 'bold'))
            ReturnTime.grid(row=5, column=0, padx=820, pady=10, sticky='w')
            ReturnTime = CTkEntry(frame1, width=150, font=('Century Gothic', 18), placeholder_text="00:00H")
            ReturnTime.grid(row=5, column=0, padx=870, pady=10, sticky='w')

            separator = ttk.Separator(frame1, orient='horizontal')
            separator.grid(row=6, column=0, columnspan=2, pady=10, sticky='ew')

            # PACKAGES
            Packages = CTkLabel(frame1, text="PACKAGE", text_color='#154734', font=('Century Gothic', 20, 'bold'))
            Packages.grid(row=7, column=0, padx=50, pady=10, sticky='w')
            
            SoundSystem = CTkRadioButton(frame1, text="Sound System Package", text_color='black',  font=('Century Gothic', 16))
            SoundSystem.grid(row=8, column=0, padx=50, pady=10, sticky='w')
            SoundSystem = CTkEntry(frame1, width=80, font=('Century Gothic', 18), state='readonly')
            SoundSystem.grid(row=8, column=0, padx=485, pady=10, sticky='w')
            SoundSystem = CTkLabel(frame1, text="₱2,000.00", text_color='black', font=('Century Gothic', 16, 'bold'))
            SoundSystem.grid(row=8, column=0, padx=790, pady=10, sticky='w')
            
            LightsPackage = CTkRadioButton(frame1, text="Lights Package", text_color='black',  font=('Century Gothic', 16))
            LightsPackage.grid(row=9, column=0, padx=50, pady=10, sticky='w')
            LightsPackage = CTkEntry(frame1, width=80, font=('Century Gothic', 18), state='readonly')
            LightsPackage.grid(row=9, column=0, padx=485, pady=10, sticky='w')
            LightsPackage = CTkLabel(frame1, text="₱2,000.00", text_color='black', font=('Century Gothic', 16, 'bold'))
            LightsPackage.grid(row=9, column=0, padx=790, pady=10, sticky='w')
            
            BasicPackage = CTkRadioButton(frame1, text="Basic Event Package", text_color='black',  font=('Century Gothic', 16))
            BasicPackage.grid(row=10, column=0, padx=50, pady=10, sticky='w')
            BasicPackage = CTkEntry(frame1, width=80, font=('Century Gothic', 18), state='readonly')
            BasicPackage.grid(row=10, column=0, padx=485, pady=10, sticky='w')
            BasicPackage = CTkLabel(frame1, text="₱3,500.00", text_color='black', font=('Century Gothic', 16, 'bold'))
            BasicPackage.grid(row=10, column=0, padx=790, pady=10, sticky='w')
            
            StandardPackage = CTkRadioButton(frame1, text="Standard Event Package", text_color='black',  font=('Century Gothic', 16))
            StandardPackage.grid(row=11, column=0, padx=50, pady=10, sticky='w')
            StandardPackage = CTkEntry(frame1, width=80, font=('Century Gothic', 18), state='readonly')
            StandardPackage.grid(row=11, column=0, padx=485, pady=10, sticky='w')
            StandardPackage = CTkLabel(frame1, text="₱5,000.00", text_color='black', font=('Century Gothic', 16, 'bold'))
            StandardPackage.grid(row=11, column=0, padx=790, pady=10, sticky='w')
            
            PremiumPackage = CTkRadioButton(frame1, text="Premium Event Package", text_color='black',  font=('Century Gothic', 16))
            PremiumPackage.grid(row=12, column=0, padx=50, pady=10, sticky='w')
            PremiumPackage = CTkEntry(frame1, width=80, font=('Century Gothic', 18), state='readonly')
            PremiumPackage.grid(row=12, column=0, padx=485, pady=10, sticky='w')
            PremiumPackage = CTkLabel(frame1, text="₱8,000.00", text_color='black', font=('Century Gothic', 16, 'bold'))
            PremiumPackage.grid(row=12, column=0, padx=790, pady=10, sticky='w')
            

            separator = ttk.Separator(frame1, orient='horizontal')
            separator.grid(row=13, column=0, columnspan=2, pady=10, sticky='ew')
            
            PaymentMethod = CTkLabel(frame1, text="PAYMENT METHOD", text_color='#154734', font=('Century Gothic', 20, 'bold'))
            PaymentMethod.grid(row=14, column=0, padx=50, pady=10, sticky='w')
            
            Cash = CTkRadioButton(frame1, text="Cash", text_color='black',  font=('Century Gothic', 16))
            Cash.grid(row=15, column=0, padx=50, pady=10, sticky='w')
            EWallet = CTkRadioButton(frame1, text="E-Wallet", text_color='black',  font=('Century Gothic', 16))
            EWallet.grid(row=16, column=0, padx=50, pady=10, sticky='w')

            # AMOUNT
            Amount = CTkLabel(frame1, text="Total Amount:", text_color='black', font=('Century Gothic', 18, 'bold'))
            Amount.grid(row=17, column=0, padx=550, pady=10, sticky='w')
            Amount = CTkEntry(frame1, width=11, font=('Century Gothic', 14, 'bold'), state='readonly')
            Amount.grid(row=17, column=0, padx=700, pady=10, sticky='w')

            # SAVE BUTTON
            SaveButton = CTkButton(update_window, text="Save Changes", font=('Century Gothic', 21, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10)
            SaveButton.grid(row=2, column=0, padx=50, pady=20, sticky='e')

            # AVAILABLE
            Available = CTkLabel(frame1, text="AVAILABLE", text_color='#154734', font=('Century Gothic', 18, 'bold'))
            Available.grid(row=7, column=0, padx=480, pady=10, sticky='w')

            # PRICE
            Price = CTkLabel(frame1, text="PRICE", text_color='#154734', font=('Century Gothic', 20, 'bold'))
            Price.grid(row=7, column=0, padx=800, pady=10, sticky='w')
               
               
            def BackToRental():
                update_window.destroy()  
                windows.deiconify()
                windows.lift()

            # BACK BUTTON
            Back2Button = CTkButton(update_window, text="BACK", font=('Century Gothic', 20, 'bold'), fg_color='#154734',text_color='white', hover_color='gray', corner_radius=10, command= BackToRental)
            Back2Button.grid(row=0, column=0, padx=25, pady=20, sticky='w')

            def SaveChanges():
            # SAVE BUTTON
                Save2Button = CTkButton(update_window, text="  Save Changes  ", font=('Century Gothic', 20, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10, command=SaveChanges)
                Save2Button.grid(row=3, column=0, padx=900, pady=20, sticky='w')

            update_window.mainloop()

        def BackRental(booking_window):
            booking_window.withdraw()
            windows.deiconify()

        def BackToRental(updatebooking_window):
            updatebooking_window.withdraw()
            windows.deiconify()

        # Add Rental
        CreateRental = ctk.CTkButton(schedule_fm, text="CREATE", font=('Century Gothic', 21, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', command=create_rental_window)
        CreateRental.grid(row=2, column=0, padx=1200, pady=10, sticky='w')

        # Update Rental
        UpdateRental = ctk.CTkButton(schedule_fm, text="UPDATE", font=('Century Gothic', 21, 'bold'), fg_color='#154734', text_color='white', hover_color='gray',command= update_rental_window)
        UpdateRental.grid(row=3, column=0, padx=1200, pady=10, sticky='w')

        # Custom style for ttk.Notebook
        style = ttk.Style()
        style.theme_use('default')

        # Notebook color and font customization
        style.configure('TNotebook', background='#fefded', borderwidth=0)
        style.configure('TNotebook.Tab', font=('Century Gothic', 16, 'bold'), background='#154734', foreground='white')
        style.map('TNotebook.Tab', background=[('selected', '#a3b18a'), ('active', 'gray')])

        # Notebook for Tabs
        notebook = ttk.Notebook(schedule_fm, style='TNotebook')
        
        # Rental Tab
        RentalTab = ctk.CTkFrame(notebook, width=1355, height=600)
        notebook.add(RentalTab, text="Rental Tab")
        
        # Customer Tab
        CustomerTab = ctk.CTkFrame(notebook, width=1355, height=600)
        notebook.add(CustomerTab, text="Customer Tab")

        notebook.grid(row=4, column=0, columnspan=4, padx=50, pady=20, sticky='w')

        # Style for Headings
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Century Gothic', 13, 'bold'), background='#a3b18a', foreground='black')

        # Data Grid View for Rental Tab
        datagridview = ttk.Treeview(RentalTab, columns=("Rental ID", "Customer Name", "Event Name", "Rental Date", "Return Date", "Payment Status", "Type"))
        datagridview.heading("#0", text="")
        datagridview.column("#0", width=0, stretch=NO)
        
        # Columns for Rental Tab
        datagridview.column("Rental ID", width=100, anchor='w')
        datagridview.heading("Rental ID", text="RENTAL ID")
        datagridview.column("Customer Name", width=300, anchor='w')
        datagridview.heading("Customer Name", text="CUSTOMER NAME")
        datagridview.column("Event Name", width=320, anchor='w')
        datagridview.heading("Event Name", text="EVENT NAME")
        datagridview.column("Rental Date", width=160, anchor='w')
        datagridview.heading("Rental Date", text="RENTAL DATE")
        datagridview.column("Return Date", width=160, anchor='w')
        datagridview.heading("Return Date", text="RETURN DATE")
        datagridview.column("Payment Status", width=150, anchor='w')
        datagridview.heading("Payment Status", text="PAYMENT STATUS")
        datagridview.column("Type", width=200, anchor='w')
        datagridview.heading("Type", text="TYPE")

        datagridview.grid(row=0, column=0, sticky='nsew', columnspan=3)

        # Data Grid View for Customer Tab
        datagridview1 = ttk.Treeview(CustomerTab, columns=("Customer ID", "Customer Name", "Address", "Contact Number", "Email Address", "Event Name", "Event Loc"))
        datagridview1.heading("#0", text="")
        datagridview1.column("#0", width=0, stretch=NO)
        
        # Columns for Customer Tab
        datagridview1.column("Customer ID", width=90, anchor='w')
        datagridview1.heading("Customer ID", text="CUST ID")
        datagridview1.column("Customer Name", width=200, anchor='w')
        datagridview1.heading("Customer Name", text="CUSTOMER NAME")
        datagridview1.column("Address", width=300, anchor='w')
        datagridview1.heading("Address", text="ADDRESS")
        datagridview1.column("Contact Number", width=150, anchor='w')
        datagridview1.heading("Contact Number", text="CONTACT NO.")
        datagridview1.column("Email Address", width=150, anchor='w')
        datagridview1.heading("Email Address", text="EMAIL ADDRESS")
        datagridview1.column("Event Name", width=250, anchor='w')
        datagridview1.heading("Event Name", text="EVENT NAME")
        datagridview1.column("Event Loc", width=250, anchor='w')
        datagridview1.heading("Event Loc", text="EVENT LOCATION")

        # Treeview grid for Customer Tab
        datagridview1.grid(row=0, column=0, sticky='nsew', columnspan=3)