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


class Payment(ctk.CTkFrame):
     def __init__(self, master):
        self.master = master
        self.main_frame = ctk.CTkFrame(self.master)
    
        payments_fm = ctk.CTkFrame(self.master, fg_color='#fefded')
        payments_fm.pack(fill='both', expand=True)

        # Payments label
        payments_lb = ctk.CTkLabel(payments_fm, text="Payments", font=('Century Gothic', 30, 'bold'), text_color='#154734')
        payments_lb.grid(row=0, column=0, padx=40, pady=20, sticky='w')

        # Function to update the time
        def updateTime():
            now = datetime.now()
            formatted_time = now.strftime("%A: %B %d, %Y, %I:%M%p")
            DateTime.configure(text=formatted_time)
            payments_fm.after(1000, updateTime)

        # DateTime label
        DateTime = ctk.CTkLabel(payments_fm, text="", font=('Century Gothic', 20, 'bold'), text_color='#154734')
        DateTime.grid(row=0, column=1, padx=860, pady=20, sticky='w')
        updateTime()

        # Custom style for ttk.Notebook
        style = ttk.Style()
        style.theme_use('default')

        # Style for headings
        style.configure("Treeview.Heading", font=('Century Gothic', 13, 'bold'), background='#a3b18a', foreground='black')

        # Frame for data grid view
        frame_payments = ctk.CTkFrame(payments_fm, fg_color='#fefded')
        frame_payments.grid(row=1, column=0, columnspan=2, sticky='w', padx=20, pady=20)


        # Data grid view for rental tab
        datagridview_payments = ttk.Treeview(frame_payments, columns=("Rental ID", "Customer Name", "Event Name", "Equipment", "Rental Start", "Return Date", "Payment Status"))
        datagridview_payments.heading("#0", text="")
        datagridview_payments.column("#0", width=10, stretch=ctk.NO)  

        # Columns for rental tab
        datagridview_payments.column("Rental ID", width=200, anchor='w')
        datagridview_payments.heading("Rental ID", text="RENTAL ID")
        datagridview_payments.column("Customer Name", width=300, anchor='w')
        datagridview_payments.heading("Customer Name", text="CUSTOMER NAME")
        datagridview_payments.column("Event Name", width=200, anchor='w')
        datagridview_payments.heading("Event Name", text="EVENT NAME")
        datagridview_payments.column("Equipment", width=200, anchor='w')
        datagridview_payments.heading("Equipment", text="EQUIPMENT")
        datagridview_payments.column("Rental Start", width=180, anchor='w')
        datagridview_payments.heading("Rental Start", text="RENTAL START")
        datagridview_payments.column("Return Date", width=180, anchor='w')
        datagridview_payments.heading("Return Date", text="RETURN DATE")
        datagridview_payments.column("Payment Status", width=150, anchor='w')
        datagridview_payments.heading("Payment Status", text="PAYMENT STATUS")

        datagridview_payments.grid(row=0, column=0, sticky='nsew')

        # Configure grid row and column to expand
        frame_payments.grid_rowconfigure(0, weight=1)
        frame_payments.grid_columnconfigure(0, weight=1)
