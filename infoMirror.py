import tkinter as tk
from tkinter import messagebox
import datetime
import calendar
import requests
import time

# class InfoMirror():
	# def __init__(self):
		
		
class MotionSensor():
	def __init__(self, pir):
		self.pir = pir
		
	def ifMotionDetected():
		print("[PIR SENSOR] Se detecto moviminto")
		
class LEDController():
	def __init__(self, leds):
		self.leds = leds
		
	def turnOn(self):
		print("[LEDS] Encender luces")
		
	def turnOff(self):
		print("[LEDS] Apagar luces")
		
	def setBrightness(self, brightness):
		print(f"[LEDS] Cambiar brillo a {brightness}")
		
import tkinter as tk
import threading
import datetime
import calendar
import requests

class Display:
    def __init__(self):
        self.root = None
        self.label = None
        self.running = False

    def turnOn(self):
        if self.root is None:
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

    def turnOff(self):
        if self.root:
            self.running = False
            self.root.destroy()
            self.root = None
            self.label = None

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


mirror = Display()
mirror.turnOn()
time.sleep(2)
mirror.showTime()
time.sleep(2)
mirror.showWeather()
time.sleep(2)
mirror.showCalendar()
time.sleep(2)

	
