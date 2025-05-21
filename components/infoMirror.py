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

import Display
import MotionSensor
import time 

class InfoMirror:
    def __init__(self):
        self.motion_sensor = MotionSensor.MotionSensor()
        self.display = Display.Display()

    def start_motion_sensor(self):
        self.motion_sensor.if_motion_detected()

    def stop_motion_sensor(self):
        self.motion_sensor.stop()

    def manage_display_request(self):
        self.display.turnOn()
        time.sleep(2)
        self.display.showTime()
        time.sleep(2)
        self.display.showWeather()
        time.sleep(2)
        self.display.showCalendar()
        time.sleep(2)




			

mirror = InfoMirror()
#mirror.start_motion_sensor()  
mirror.manage_display_request()


	
