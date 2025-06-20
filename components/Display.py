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
import threading
import datetime
import calendar
import requests

class Display:
    BACKGROUND_COLOR = "#2c2c2c"  # gris oscuro
    TEXT_COLOR = "#ffffff"        # blanco
    FONT_FAMILY = "Arial"
    FONT_NORMAL = (FONT_FAMILY, 23)
    
    def __init__(self, parent):
        self.parent = parent
        self.root = None
        self.label = None
        self.running = False
        self.encendido = False

    def turnOn(self):
        self.encendido = True
        if not self.running:
            self.running = True
            threading.Thread(target=self._start_gui, daemon=True).start()
        text="Bienvenid@ a InfoMirror \U0001FA9E\u2728"
        self._update_label(text)
        print("[DISPLAY] Encendiendo Display")

    def _start_gui(self):
        self.root = tk.Tk()
        self.root.title("InfoMirror")
        self.root.geometry("2000x1200")
        self.root.configure(bg=self.BACKGROUND_COLOR)

        self.label = tk.Label(
            self.root,
            text="Bienvenid@ a InfoMirror \U0001FA9E\u2728",
            font=(self.FONT_NORMAL),
            fg=self.TEXT_COLOR,
            bg=self.BACKGROUND_COLOR,
            justify="left",
            anchor="w",
            padx=70
        )
        self.label.pack(expand=True, fill="both", padx=70, pady=50)

        self.root.protocol("WM_DELETE_WINDOW", self.turnOff)
        self.root.mainloop()

        self.running = False
        self.root = None
        self.label = None

    def turnOff(self):
        self._update_label("")
        self.encendido = False
        print("[DISPLAY] Apagando Display")

    def _update_label(self, text):
        if self.label and self.root:
            self.root.after(0, lambda: self.label.config(text=text))
        else:
            print("[WARNING] Pantalla apagada. Enciende primero con `turnOn()`.")

    def get_weather(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=9.93&longitude=-84.08&current_weather=true"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()["current_weather"]
                return f"\U0001F324\uFE0F Temp: {data['temperature']}C\n\U0001F343 Viento: {data['windspeed']} km/h"
            else:
                return "No se pudo obtener el clima."
        except Exception as e:
            return f"Error: {e}"

    def showWeather(self):
        if(self.encendido):
                weather_info = self.get_weather()
                if self.label and self.root:
                        self.label.config(
                            text=weather_info,
                            font=self.FONT_NORMAL  
                        )
                self._update_label(weather_info)
                
                print("[DISPLAY] Mostrando el clima")

    def showTime(self):
        if(self.encendido):
                now = datetime.datetime.now()
                time_info = now.strftime("\U0001F552 Hora: %H:%M\nFecha: %A, \n%d de %B de %Y")
                if self.label and self.root:
                        self.label.config(
                            text=time_info,
                            font=(self.FONT_NORMAL)  
                        )
                self._update_label(time_info)
                print("[DISPLAY] Mostrando hora y fecha")

    def showCalendar(self):
        if(self.encendido):
                now = datetime.datetime.now()
                cal = calendar.TextCalendar()
                month_cal = "\U0001F4C5 Calendario\n" + cal.formatmonth(now.year, now.month)
                if self.label and self.root:
                        self.label.config(
                            text=month_cal,
                            font=(self.FONT_NORMAL, 18)  
                        )
                self._update_label(month_cal)
                print("[DISPLAY] Mostrando el calendario")

