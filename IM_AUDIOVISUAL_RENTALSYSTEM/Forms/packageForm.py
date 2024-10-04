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

class Package(ctk.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.main_frame = ctk.CTkFrame(self.master)

        package_fm = ctk.CTkFrame(self.master, fg_color='#fefded')
        package_fm.pack(fill='both', expand=True)

        package_lbl = ctk.CTkLabel(package_fm, text="Package", font=('Century Gothic', 30, 'bold'), text_color='#154734')
        package_lbl.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        # Function to update the time
        def updateTime():
            now = datetime.now()
            formatted_time = now.strftime("%A, %B %d, %Y, %I:%M %p")
            DateTime.configure(text=formatted_time)
            package_fm.after(1000, updateTime)

        # DateTime label
        DateTime = ctk.CTkLabel(package_fm, text="", font=('Century Gothic', 20, 'bold'), text_color='#154734')
        DateTime.grid(row=0, column=0, padx=1100, pady=20, sticky='w')
        updateTime()

        frame1 = CTkScrollableFrame(package_fm, fg_color='#f1f1f1', width=1400, height=700)
        frame1.grid(row=2, column=0, padx=20, pady=40, sticky='w')

        package_title = CTkLabel(frame1, text="PACKAGE", font=('Century Gothic', 20, 'bold'), text_color='black')
        package_title.grid(row=0, column=0, padx=30, pady=20, sticky='w')
        inclusion_title = CTkLabel(frame1, text="INCLUSIONS", font=('Century Gothic', 20, 'bold'), text_color='black')
        inclusion_title.grid(row=0, column=0, padx=500, pady=20, sticky='w')

        # SOUND SYSTEM PACKAGE
        SoundSystemPackage = CTkLabel(frame1, text="Sound System Package", font=('Century Gothic', 16, 'bold'), text_color='#154734')
        SoundSystemPackage.grid(row=1, column=0, padx=25, pady=5, sticky='w')
        PriceSSP = CTkLabel(frame1, text="Package Price: ₱2,000", font=('Century Gothic', 14, 'bold'), text_color='black')
        PriceSSP.grid(row=2, column=0, padx=25, pady=5, sticky='w')
        SoundSystem = CTkLabel(frame1, text="Sound System:", font=('Century Gothic', 16), text_color='black')
        SoundSystem.grid(row=1, column=0, padx=500, pady=5, sticky='w')
        AudioMixer = CTkLabel(frame1, text="• Audio Mixer: 1 unit", font=('Century Gothic', 16), text_color='black')
        AudioMixer.grid(row=2, column=0, padx=500, pady=5, sticky='w')
        Microphones = CTkLabel(frame1, text="• Microphones: 2 units", font=('Century Gothic', 16), text_color='black')
        Microphones.grid(row=3, column=0, padx=500, pady=5, sticky='w')
        Speakers = CTkLabel(frame1, text="• Speakers: 4 units", font=('Century Gothic', 16), text_color='black')
        Speakers.grid(row=4, column=0, padx=500, pady=5, sticky='w')
        PowerAmpli = CTkLabel(frame1, text="• Power Amplifier: 1 unit", font=('Century Gothic', 16), text_color='black')
        PowerAmpli.grid(row=5, column=0, padx=500, pady=5, sticky='w')

        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=6, column=0, columnspan=3, padx=30, pady=10, sticky='ew')

        # LIGHTS PACKAGE
        LightPackage = CTkLabel(frame1, text="Lights Package", font=('Century Gothic', 16, 'bold'), text_color='#154734')
        LightPackage.grid(row=7, column=0, padx=30, pady=5, sticky='w')
        PriceLP = CTkLabel(frame1, text="Package Price: ₱2,000", font=('Century Gothic', 14, 'bold'), text_color='black')
        PriceLP.grid(row=8, column=0, padx=30, pady=5, sticky='w')
        Lights = CTkLabel(frame1, text="Lights:", font=('Century Gothic', 16), text_color='black')
        Lights.grid(row=7, column=0, padx=500, pady=5, sticky='w')
        Spotlight = CTkLabel(frame1, text="• Spotlight: 2 units", font=('Century Gothic', 16), text_color='black')
        Spotlight.grid(row=8, column=0, padx=500, pady=5, sticky='w')
        LedUplights = CTkLabel(frame1, text="• LED Uplights: 8 units", font=('Century Gothic', 16), text_color='black')
        LedUplights.grid(row=9, column=0, padx=500, pady=5, sticky='w')
        DiscoLights = CTkLabel(frame1, text="• Disco Lights: 2 units", font=('Century Gothic', 16), text_color='black')
        DiscoLights.grid(row=10, column=0, padx=500, pady=5, sticky='w')
        ParLights = CTkLabel(frame1, text="• PAR Lights: 4 units", font=('Century Gothic', 16), text_color='black')
        ParLights.grid(row=11, column=0, padx=500, pady=5, sticky='w')
        LightController = CTkLabel(frame1, text="• Light Controller: 1 unit", font=('Century Gothic', 16), text_color='black')
        LightController.grid(row=12, column=0, padx=500, pady=5, sticky='w')

        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=14, column=0, columnspan=3, padx=30, pady=10, sticky='ew')

        # BASIC EVENT PACKAGE
        BasicEventPackage = CTkLabel(frame1, text="Basic Event Package", font=('Century Gothic', 16, 'bold'), text_color='#154734')
        BasicEventPackage.grid(row=15, column=0, padx=30, pady=5, sticky='w')
        PriceBEP = CTkLabel(frame1, text="Package Price: ₱3,500", font=('Century Gothic', 14, 'bold'), text_color='black')
        PriceBEP.grid(row=16, column=0, padx=30, pady=5, sticky='w')
        SoundSystem = CTkLabel(frame1, text="Sound System: ", font=('Century Gothic', 16), text_color='black')
        SoundSystem.grid(row=15, column=0, padx=500, pady=5, sticky='w')
        AudioMixer = CTkLabel(frame1, text="• Audio Mixer: 1 unit", font=('Century Gothic', 16), text_color='black')
        AudioMixer.grid(row=16, column=0, padx=500, pady=5, sticky='w')
        Microphones = CTkLabel(frame1, text="• Microphones: 2 units", font=('Century Gothic', 16), text_color='black')
        Microphones.grid(row=17, column=0, padx=500, pady=5, sticky='w')
        Speakers = CTkLabel(frame1, text="• Speakers: 2 units", font=('Century Gothic', 16), text_color='black')
        Speakers.grid(row=18, column=0, padx=500, pady=5, sticky='w')
        PowerAmpli = CTkLabel(frame1, text="• Power Amplifier: 1 unit", font=('Century Gothic', 16), text_color='black')
        PowerAmpli.grid(row=19, column=0, padx=500, pady=5, sticky='w')

        Lights = CTkLabel(frame1, text="Lights:", font=('Century Gothic', 16), text_color='black')
        Lights.grid(row=15, column=0, padx=825, pady=5, sticky='w')
        Spotlight = CTkLabel(frame1, text="• Spotlights: 1 unit", font=('Century Gothic', 16), text_color='black')
        Spotlight.grid(row=16, column=0, padx=825, pady=5, sticky='w')
        LedUplights = CTkLabel(frame1, text="• LED Uplights: 4 units", font=('Century Gothic', 16), text_color='black')
        LedUplights.grid(row=17, column=0, padx=825, pady=5, sticky='w')
        DiscoLights = CTkLabel(frame1, text="• Disco Lights: 1 unit", font=('Century Gothic', 16), text_color='black')
        DiscoLights.grid(row=18, column=0, padx=825, pady=5, sticky='w')

        Gears = CTkLabel(frame1, text="Gears:", font=('Century Gothic', 16), text_color='black')
        Gears.grid(row=15, column=0, padx=1100, pady=5, sticky='w')
        ExtensionPC = CTkLabel(frame1, text="• Extension Power Cables: 2 units", font=('Century Gothic', 16), text_color='black')
        ExtensionPC.grid(row=16, column=0, padx=1100, pady=5, sticky='w')
        ExtraBatt = CTkLabel(frame1, text="• Extra Batteries: 4 units", font=('Century Gothic', 16), text_color='black')
        ExtraBatt.grid(row=17, column=0, padx=1100, pady=5, sticky='w')
        PowerSupply = CTkLabel(frame1, text="• Power Supply: 1 unit", font=('Century Gothic', 16), text_color='black')
        PowerSupply.grid(row=18, column=0, padx=1100, pady=5, sticky='w')

        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=20, column=0, columnspan=3, padx=30, pady=10, sticky='ew')

        # STANDARD EVENT PACKAGE
        StandardEventPackage = CTkLabel(frame1, text="Standard Event Package", font=('Century Gothic', 16, 'bold'), text_color='#154734')
        StandardEventPackage.grid(row=21, padx=30, pady=5, sticky='w')
        PriceSEP = CTkLabel(frame1, text="Package Price: ₱5,000", font=('Century Gothic', 14, 'bold'), text_color='black')
        PriceSEP.grid(row=22, column=0, padx=30, pady=5, sticky='w')
        SoundSystem = CTkLabel(frame1, text="Sound System: ", font=('Century Gothic', 16), text_color='black')
        SoundSystem.grid(row=21, padx=500, pady=5, sticky='w')
        AudioMixer = CTkLabel(frame1, text="• Audio Mixer: 1 unit", font=('Century Gothic', 16), text_color='black')
        AudioMixer.grid(row=22, padx=500, pady=5, sticky='w')
        Microphones = CTkLabel(frame1, text="• Microphones: 4 units", font=('Century Gothic', 16), text_color='black')
        Microphones.grid(row=23, padx=500, pady=5, sticky='w')
        Speakers = CTkLabel(frame1, text="• Speakers: 4 units", font=('Century Gothic', 16), text_color='black')
        Speakers.grid(row=24, padx=500, pady=5, sticky='w')
        PowerAmpli = CTkLabel(frame1, text="• Power Amplifier: 1 unit", font=('Century Gothic', 16), text_color='black')
        PowerAmpli.grid(row=25, padx=500, pady=5, sticky='w')

        Lights = CTkLabel(frame1, text="Lights:", font=('Century Gothic', 16), text_color='black')
        Lights.grid(row=21, padx=825, pady=5, sticky='w')
        Spotlight = CTkLabel(frame1, text="• Spotlights: 2 units", font=('Century Gothic', 16), text_color='black')
        Spotlight.grid(row=22, padx=825, pady=5, sticky='w')
        LedUplights = CTkLabel(frame1, text="• LED Uplights: 8 units", font=('Century Gothic', 16), text_color='black')
        LedUplights.grid(row=23, padx=825, pady=5, sticky='w')
        DiscoLights = CTkLabel(frame1, text="• Disco Lights: 2 units", font=('Century Gothic', 16), text_color='black')
        DiscoLights.grid(row=24, padx=825, pady=5, sticky='w')
        ParLights = CTkLabel(frame1, text="• PAR Lights: 4 units", font=('Century Gothic', 16), text_color='black')
        ParLights.grid(row=25, padx=825, pady=5, sticky='w')
        LightController = CTkLabel(frame1, text="• Light Controller: 1 unit", font=('Century Gothic', 16), text_color='black')
        LightController.grid(row=26, padx=825, pady=5, sticky='w')

        Gears = CTkLabel(frame1, text="Gears:", font=('Century Gothic', 16), text_color='black')
        Gears.grid(row=21, padx=1100, pady=5, sticky='w')
        ExtensionPC = CTkLabel(frame1, text="• Extension Power Cables: 4 units", font=('Century Gothic', 16), text_color='black')
        ExtensionPC.grid(row=22, padx=1100, pady=5, sticky='w')
        ExtraBatt = CTkLabel(frame1, text="• Extra Batteries: 8 units", font=('Century Gothic', 16), text_color='black')
        ExtraBatt.grid(row=23, padx=1100, pady=5, sticky='w')
        PowerAdapters = CTkLabel(frame1, text="• Power Adapters: 4 units", font=('Century Gothic', 16), text_color='black')
        PowerAdapters.grid(row=24, padx=1100, pady=5, sticky='w')
        JackCables = CTkLabel(frame1, text="• JackCables: 4 units", font=('Century Gothic', 16), text_color='black')
        JackCables.grid(row=25, padx=1100, pady=5, sticky='w')

        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=27, column=0, columnspan=3, padx=30, pady=10, sticky='ew')

        # PREMIUM EVENT PACKAGE
        PremiumEventPackage = CTkLabel(frame1, text="Premium Event Package", font=('Century Gothic', 16, 'bold'), text_color='#154734')
        PremiumEventPackage.grid(row=28, padx=30, pady=5, sticky='w')
        PricePEP = CTkLabel(frame1, text="Package Price: ₱8,000", font=('Century Gothic', 14, 'bold'), text_color='black')
        PricePEP.grid(row=29, column=0, padx=30, pady=5, sticky='w')
        SoundSystem = CTkLabel(frame1, text="Sound System: ", font=('Century Gothic', 16), text_color='black')
        SoundSystem.grid(row=28, padx=500, pady=5, sticky='w')
        AudioMixer = CTkLabel(frame1, text="• Audio Mixer: 1 unit", font=('Century Gothic', 16), text_color='black')
        AudioMixer.grid(row=29, padx=500, pady=5, sticky='w')
        Microphones = CTkLabel(frame1, text="• Microphones: 6 units", font=('Century Gothic', 16), text_color='black')
        Microphones.grid(row=30, padx=500, pady=5, sticky='w')
        Speakers = CTkLabel(frame1, text="• Speakers: 6 units", font=('Century Gothic', 16), text_color='black')
        Speakers.grid(row=31, padx=500, pady=5, sticky='w')
        PowerAmpli = CTkLabel(frame1, text="• Power Amplifier: 1 unit", font=('Century Gothic', 16), text_color='black')
        PowerAmpli.grid(row=32, padx=500, pady=5, sticky='w')

        Lights = CTkLabel(frame1, text="Lights:", font=('Century Gothic', 16), text_color='black')
        Lights.grid(row=28, padx=825, pady=5, sticky='w')
        Spotlight = CTkLabel(frame1, text="• Spotlights: 2 units", font=('Century Gothic', 16), text_color='black')
        Spotlight.grid(row=29, padx=825, pady=5, sticky='w')
        LedUplights = CTkLabel(frame1, text="• LED Uplights: 12 units", font=('Century Gothic', 16), text_color='black')
        LedUplights.grid(row=30, padx=825, pady=5, sticky='w')
        DiscoLights = CTkLabel(frame1, text="• Disco Lights: 3 units", font=('Century Gothic', 16), text_color='black')
        DiscoLights.grid(row=31, padx=825, pady=5, sticky='w')
        ParLights = CTkLabel(frame1, text="• PAR Lights: 8 units", font=('Century Gothic', 16), text_color='black')
        ParLights.grid(row=32, padx=825, pady=5, sticky='w')
        LightController = CTkLabel(frame1, text="• Light Controller: 1 unit", font=('Century Gothic', 16), text_color='black')
        LightController.grid(row=33, padx=825, pady=5, sticky='w')

        Gears = CTkLabel(frame1, text="Gears:", font=('Century Gothic', 16), text_color='black')
        Gears.grid(row=28, padx=1100, pady=5, sticky='w')
        ExtensionPC = CTkLabel(frame1, text="• Extension Power Cables: 6 units", font=('Century Gothic', 16), text_color='black')
        ExtensionPC.grid(row=29, padx=1100, pady=5, sticky='w')
        ExtraBatt = CTkLabel(frame1, text="• Extra Batteries: 12 units", font=('Century Gothic', 16), text_color='black')
        ExtraBatt.grid(row=30, padx=1100, pady=5, sticky='w')
        PowerAdapters = CTkLabel(frame1, text="• Power Adapters: 6 units", font=('Century Gothic', 16), text_color='black')
        PowerAdapters.grid(row=31, padx=1100, pady=5, sticky='w')
        JackCables = CTkLabel(frame1, text="• JackCables: 6 units", font=('Century Gothic', 16), text_color='black')
        JackCables.grid(row=32, padx=1100, pady=5, sticky='w')

        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=34, column=0, columnspan=3, padx=30, pady=20, sticky='ew')
