from tkinter import Tk
import customtkinter as ctk
from datetime import datetime
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Report(ctk.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.main_frame = ctk.CTkFrame(self.master)
        self.create_widgets()

    def create_widgets(self):
        # Main frame for reports
        report_fm = ctk.CTkFrame(self.master, fg_color='#fefded')
        report_fm.pack(fill='both', expand=True)

        # Report label
        payments_lb = ctk.CTkLabel(report_fm, text="Reports", font=('Century Gothic', 30, 'bold'), text_color='#154734')
        payments_lb.grid(row=0, column=0, padx=40, pady=20, sticky='w')

        # DateTime label
        self.DateTime = ctk.CTkLabel(report_fm, text="", font=('Century Gothic', 20, 'bold'), text_color='#154734')
        self.DateTime.grid(row=0, column=2, padx=20, pady=20, sticky='e')

        # Function to update the time
        def updateTime():
            now = datetime.now()
            formatted_time = now.strftime("%A, %B %d, %Y, %I:%M %p")
            self.DateTime.configure(text=formatted_time)
            self.main_frame.after(1000, updateTime) 
        
        updateTime()

        def filterData(timeframe):
            if timeframe == 'today':
                # TODAY DATA
                data = [random.randint(0, 20) for _ in range(3)]
            elif timeframe == 'this_month':
                # THIS MONTH'S DATA
                data = [random.randint(0, 50) for _ in range(3)]
            else:
                # Default data
                data = [10, 20, 30]
            return data

        def BarGraph(frame, Data1, Data2):
            categories = ['Item 1', 'Item 2', 'Item 3']
            fig, ax = plt.subplots(figsize=(8, 5))  # Adjusting the figure size
            BarWidth = 0.4
            index = range(len(categories))
            ax.bar(index, Data1, BarWidth, label='Data 1', color='#a3b18a')
            ax.bar([i + BarWidth for i in index], Data2, BarWidth, label='Data 2', color='#154734')
            ax.set_xlabel('DATA')
            ax.set_ylabel('Values')
            ax.set_title('REPORTS GRAPH')
            ax.set_xticks([i + BarWidth / 2 for i in index])
            ax.set_xticklabels(categories)
            ax.legend()
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

        # Frame for bar graph
        graph_frame = ctk.CTkFrame(report_fm, fg_color='#fefded')
        graph_frame.grid(row=2, column=0, sticky='nsew', padx=20, pady=20, columnspan=2, rowspan=4)

        # Short description
        description = ctk.CTkLabel(report_fm, text="Short description of what's in the graph", font=('Century Gothic', 16), text_color='black')
        description.grid(row=1, column=0, padx=100, pady=10, sticky='w', columnspan=3)

        def update_graph(timeframe):
            for widget in graph_frame.winfo_children():
                widget.destroy()
            Data1 = filterData(timeframe)
            Data2 = filterData(timeframe)
            BarGraph(graph_frame, Data1, Data2)

        # Today button
        today = ctk.CTkButton(report_fm, text="TODAY", font=('Century Gothic', 16, 'bold'), fg_color='#a3b18a', text_color='white', hover_color='gray', command=lambda: update_graph('today'))
        today.grid(row=1, column=2, padx=160, pady=10, sticky='ne')

        # Month button
        month = ctk.CTkButton(report_fm, text="THIS MONTH", font=('Century Gothic', 16, 'bold'), fg_color='#154734', text_color='white', hover_color='gray', command=lambda: update_graph('this_month'))
        month.grid(row=1, column=2, padx=10, pady=10, sticky='ne')

        # First frame
        first_frame = ctk.CTkFrame(report_fm, fg_color='#f5f5f5', width=450, height=200, corner_radius=20)
        first_frame.grid(row=2, column=2, padx=50, pady=10, sticky='ne')

        # Second frame
        second_frame = ctk.CTkFrame(report_fm, fg_color='#f5f5f5', width=450, height=430, corner_radius=20)
        second_frame.grid(row=3, column=2, padx=50, pady=10, sticky='se')

        # Configure window grid weights for resizing
        report_fm.grid_rowconfigure(2, weight=1)
        report_fm.grid_columnconfigure(0, weight=1)
        report_fm.grid_columnconfigure(1, weight=1)
        report_fm.grid_columnconfigure(2, weight=0)

        # Initial call to update the graph with default data
        update_graph('default')
