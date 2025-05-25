# ---------------------------------------------------------------
# Clase InfoMirror
# ---------------------------------------------------------------
# Esta es la clase principal del sistema, administra todas las 
# funcionalidades.
#
# Caracteristicas:
# - Deteccion de movimiento -> MotionSensor
# - Control de luces LED -> LEDController
# - Manejo del display del espejo -> Display
# ---------------------------------------------------------------

from components import Display
from components import MotionSensor
import time 

class InfoMirror:
    def __init__(self):
        self.motion_sensor = MotionSensor.MotionSensor()
        self.display = Display.Display()

    def start_motion_sensor(self):
        self.motion_sensor.if_motion_detected()

    def stop_motion_sensor(self):
        self.motion_sensor.stop()

    def manage_display_request(self, request):
        match request:
                case 1: # Encender display
                        response = self.display.turnOn()
                case 2: # Apagar display
                        response = self.display.turnOff()
                case 3: # Mostrar clima
                        response = self.display.showWeather()
                case 4: # Mostrar hora
                        response = self.display.showTime()
                case 5: # Mostrar calendario
                        response = self.display.showCalendar() 
        time.sleep(2)
        return response
 
# mirror = InfoMirror()
# #mirror.start_motion_sensor()  
# mirror.manage_display_request()


	
