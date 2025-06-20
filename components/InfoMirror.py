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
from components import LEDController
import time 

class InfoMirror:
    def __init__(self):
        self.motion_sensor = MotionSensor.MotionSensor(parent = self) # Sensor de movimiento
        self.display = Display.Display(parent = self) # Display de informacion 
        self.led_controller = LEDController.LEDController(parent = self) # Control de LEDs
        self.manual_led_override = False # Control de luces por medio de la app
        self.manual_display_override = False # Control del display por medio de la app
        self.display.turnOn() 

    def start_motion_sensor(self):
        self.motion_sensor.if_motion_detected()

    def stop_motion_sensor(self):
        self.motion_sensor.stop()
        
    def manage_leds_request(self, request):
        match request:
                case 1: # Encender LEDs
                        self.manual_led_override = False
                        responde = self.led_controller.turnOn()
                case 2: # Apagar LEDs
                        self.manual_led_override = True 
                        print("ENTRA")
                        response = self.led_controller.turnOff()
        return response

    def manage_display_request(self, request):
        match request:
                case 1: # Encender display
                        self.manual_display_override = False
                        response = self.display.turnOn()
                case 2: # Apagar display
                        self.manual_display_override = True
                        response = self.display.turnOff()
                case 3: # Mostrar clima
                        response = self.display.showWeather()
                case 4: # Mostrar hora
                        response = self.display.showTime()
                case 5: # Mostrar calendario
                        response = self.display.showCalendar() 
        return response
 



	
