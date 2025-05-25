# ---------------------------------------------------------------
# Clase Display
# ---------------------------------------------------------------
# Esta clase gestiona las peticiones de Display de informacion 
# realizadas desde la aplicacion. 
#
# Caracteristicas:
# - Mostrar datos del tiempo
# - Mostrar datos de la hora y fecha
# - Mostrar calendario del mes
# - Encendido y apagado
# ---------------------------------------------------------------


import tkinter as tk
from tkinter import messagebox
import datetime
import calendar
import requests
import time
import threading

class Display:
    def __init__(self):
        self.root = None
        self.label = None
        self.running = False

    def turnOn(self):
        if not self.running:  # evitar multiples hilos
            self.running = True
            threading.Thread(target=self._start_gui, daemon=True).start()

    def _start_gui(self):
        self.root = tk.Tk()
        self.root.title("InfoMirror")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Bienvenid@ a InfoMirror", font=("Arial", 16))
        self.label.pack(expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.turnOff)
        self.root.mainloop()

        # Al cerrar el mainloop, limpiar estado
        self.running = False
        self.root = None
        self.label = None

    def turnOff(self):
        if self.root:
            self.root.destroy()  # Rompe el mainloop y continua _start_gui()

    def _update_label(self, text):
        if self.label and self.root:
            self.root.after(0, lambda: self.label.config(text=text))
        else:
            print("Pantalla apagada. Enciende primero con `turnOn()`.")

    def get_weather(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=-34.61&longitude=-58.38&current_weather=true"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()["current_weather"]
                return f"Temp: {data['temperature']}C\nViento: {data['windspeed']} km/h"
            else:
                return "No se pudo obtener el clima."
        except Exception as e:
            return f"Error: {e}"

    def showWeather(self):
        weather_info = self.get_weather()
        self._update_label(weather_info)

    def showTime(self):
        now = datetime.datetime.now()
        time_info = now.strftime("Hora: %H:%M\nFecha: %A, %d de %B de %Y")
        self._update_label(time_info)

    def showCalendar(self):
        now = datetime.datetime.now()
        cal = calendar.TextCalendar()
        month_cal = cal.formatmonth(now.year, now.month)
        self._update_label(month_cal)
