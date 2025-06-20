# ---------------------------------------------------------------
# Clase LEDController
# ---------------------------------------------------------------
# Esta clase gestiona una tira de LEDs para la iluminacion del espejo,
# conectada a la Raspberry Pi. La intensidad del la luz es regulada 
# por un potenciometro o desde la aplicacion. 
#
# Caracteristicas:
# - Encendido y apagado de luces (depende del sensor PIR o request)
# - Regulacion de la intensidad (desde la aplicacion o potenciometro)
# ---------------------------------------------------------------

import gpiod

class LEDController:
    def __init__(self, parent, led_pin=27, chip_name="gpiochip4"):
        self.parent = parent
        self.chip = gpiod.Chip(chip_name)
        self.led_line = self.chip.get_line(led_pin)
        self.led_line.request(consumer="led", type=gpiod.LINE_REQ_DIR_OUT)

    def turnOn(self):
        print("[LEDS] Encender luces")
        self.led_line.set_value(1)
        self.leds = 1

    def turnOff(self):
        print("[LEDS] Apagar luces")
        self.led_line.set_value(0)
        self.leds = 0



