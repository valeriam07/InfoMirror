# ---------------------------------------------------------------
# Clase MotionSensor
# ---------------------------------------------------------------
# Esta clase gestiona la deteccion de movimiento mediante un sensor PIR
# conectado a la Raspberry Pi. Al detectar movimiento, enciende un LED
# como indicador visual. Es una de las funcionalidades del sistema InfoMirror.
#
# Caracteristicas:
# - Monitorea constantemente la salida del sensor PIR.
# - Enciende un LED si se detecta movimiento.
# - Apaga el LED si no hay movimiento.
# ---------------------------------------------------------------

import gpiod
import time

class MotionSensor:
    def __init__(self, parent, pir_pin=17, chip_name="gpiochip4"):
        self.parent = parent
        self.chip = gpiod.Chip(chip_name)
        self.pir_line = self.chip.get_line(pir_pin)
        self.pir_line.request(consumer="pir_sensor", type=gpiod.LINE_REQ_DIR_IN)
        self.running = False

    def if_motion_detected(self):
        self.running = True
        try:
            while self.running:
                motion = self.pir_line.get_value()
                if motion == 1:
                    if not self.parent.manual_led_override:
                        self.parent.led_controller.turnOn()
                        if not self.parent.manual_display_override:
                                self.parent.display.turnOn()
                        time.sleep(15) # Esperar 20s antes de leer otra vez
                else:
                    self.parent.led_controller.turnOff()
                    self.parent.display.turnOff()
                time.sleep(0.1) 
        except KeyboardInterrupt:
            print("Cancelado por el usuario.")
        finally:
            self.cleanup()

    def stop(self):
        self.running = False

    def cleanup(self):
        self.parent.led_controller.turnOff()
        self.pir_line.release()
        self.led_line.release()
