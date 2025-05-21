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
    def __init__(self, pir_pin=17, led_pin=27, chip_name="gpiochip4"):
        self.chip = gpiod.Chip(chip_name)
        self.pir_line = self.chip.get_line(pir_pin)
        self.led_line = self.chip.get_line(led_pin)
        self.pir_line.request(consumer="pir_sensor", type=gpiod.LINE_REQ_DIR_IN)
        self.led_line.request(consumer="led", type=gpiod.LINE_REQ_DIR_OUT)
        self.running = False

    def if_motion_detected(self):
        self.running = True
        try:
            while self.running:
                motion = self.pir_line.get_value()
                if motion == 1:
                    print("Movimiento detectado!")
                    self.led_line.set_value(1)
                else:
                    self.led_line.set_value(0)
                    print("Sin movimiento, apagando")
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("Cancelado por el usuario.")
        finally:
            self.cleanup()

    def stop(self):
        self.running = False

    def cleanup(self):
        self.led_line.set_value(0)
        self.pir_line.release()
        self.led_line.release()
