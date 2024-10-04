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

class Equipment(ctk.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.main_frame = ctk.CTkFrame(self.master)
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.main_frame = ctk.CTkFrame(self.master, fg_color='#fefded', height=800)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Ensure the main frame expands to fill the space
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Date and Time update function
        def updateTime():
            now = datetime.now()
            formatted_time = now.strftime("%A: %B %d, %Y, %I:%M%p")
            self.DateTime.configure(text=formatted_time)
            self.main_frame.after(1000, updateTime)

        # Title
        rentals = ctk.CTkLabel(self.main_frame, text="Equipment", font=('Century Gothic', 30, 'bold'), text_color='#154734')
        rentals.grid(row=0, column=0, padx=40, pady=20, sticky='w')

        self.DateTime = ctk.CTkLabel(self.main_frame, text="", font=('Century Gothic', 20, 'bold'), text_color='#154734')
        self.DateTime.grid(row=0, column=0, padx=1100, pady=20, sticky='w')
        updateTime()

        # SEARCH EQUIPMENT
        SearchLabel = CTkLabel(self.main_frame, text="Search:", text_color='#154734', font=('Century Gothic', 20, 'bold'))
        SearchLabel.grid(row=1, column=0, padx=470, pady=10, sticky='w')
        SearchEntry = CTkEntry(self.main_frame, width=370, font=('Century Gothic', 20), placeholder_text="Search Equipment...")
        SearchEntry.grid(row=1, column=0, padx=550, pady=10, sticky='w')
        SearchButton = CTkButton(self.main_frame, text="Search", font=('Century Gothic', 20, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10)
        SearchButton.grid(row=1, column=0, padx=960, pady=10, sticky='w')

        # ADD ITEM
        AddItem = CTkButton(self.main_frame, text="Add Item", font=('Century Gothic', 21, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', corner_radius=10)
        AddItem.grid(row=1, column=0, padx=1280, pady=10, sticky='w')

        # Custom style for ttk.Notebook
        style = ttk.Style()
        style.theme_use('default')

        # Notebook color and font customization
        style.configure('TNotebook', background='#fefded', borderwidth=0)
        style.configure('TNotebook.Tab', font=('Century Gothic', 16, 'bold'), background='#154734', foreground='white')
        style.map('TNotebook.Tab', background=[('selected', '#a3b18a'), ('active', 'gray')])

        # NOTEBOOK FOR TABS
        notebook = ttk.Notebook(self.main_frame, style='TNotebook')

        # AVAILABLE TAB
        AvailableTab = CTkFrame(notebook, width=1355, height=600)
        notebook.add(AvailableTab, text="Available")

        # RENTED TAB
        RentedTab = CTkFrame(notebook, width=1355, height=600)
        notebook.add(RentedTab, text="Rented")

        notebook.grid(row=3, column=0, columnspan=2, padx=40, pady=20, sticky='w')

        # STYLE FOR HEADINGS
        style.configure("Treeview.Heading", font=('Century Gothic', 13, 'bold'), background='#a3b18a', foreground='black')

        # DATA GRID VIEW FOR AVAILABLE TAB
        datagridview = ttk.Treeview(AvailableTab, columns=("Equipment ID", "Equipment Name", "Category", "Rental Price", "Quantity"))
        datagridview.heading("#0", text="")
        datagridview.column("#0", width=0, stretch="no")

        # COLUMNS FOR AVAILABLE TAB
        datagridview.column("Equipment ID", width=150, anchor='w')
        datagridview.heading("Equipment ID", text="EQUIPMENT ID")
        datagridview.column("Equipment Name", width=350, anchor='w')
        datagridview.heading("Equipment Name", text="EQUIPMENT NAME")
        datagridview.column("Category", width=390, anchor='w')
        datagridview.heading("Category", text="CATEGORY")
        datagridview.column("Rental Price", width=250, anchor='w')
        datagridview.heading("Rental Price", text="RENTAL PRICE")
        datagridview.column("Quantity", width=250, anchor='w')
        datagridview.heading("Quantity", text="QUANTITY")

        datagridview.grid(row=0, column=0, sticky='nsew', columnspan=3)

        # DATA GRID VIEW FOR RENTED TAB
        datagridview1 = ttk.Treeview(RentedTab, columns=("Equipment ID", "Equipment Name", "Category", "Rental Price", "Quantity"))
        datagridview1.heading("#0", text="")
        datagridview1.column("#0", width=0, stretch="no")

        # COLUMNS FOR RENTED TAB
        datagridview1.column("Equipment ID", width=150, anchor='w')
        datagridview1.heading("Equipment ID", text="EQUIPMENT ID")
        datagridview1.column("Equipment Name", width=350, anchor='w')
        datagridview1.heading("Equipment Name", text="EQUIPMENT NAME")
        datagridview1.column("Category", width=390, anchor='w')
        datagridview1.heading("Category", text="CATEGORY")
        datagridview1.column("Rental Price", width=250, anchor='w')
        datagridview1.heading("Rental Price", text="RENTAL PRICE")
        datagridview1.column("Quantity", width=250, anchor='w')
        datagridview1.heading("Quantity", text="QUANTITY")

        datagridview1.grid(row=0, column=0, sticky='nsew', columnspan=3)