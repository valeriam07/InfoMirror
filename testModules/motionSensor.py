import gpiod
import time

# Usa el primer chip de GPIO disponible (normalmente 'gpiochip4' en RPi 5)
chip = gpiod.Chip('gpiochip4')

# Pines: puedes cambiar estos por los que uses
PIR_PIN = 17   # GPIO17 (pin fisico 11)
LED_PIN = 27   # GPIO27 (pin fisico 13)

# Solicita acceso a las lineas
pir_line = chip.get_line(PIR_PIN)
led_line = chip.get_line(LED_PIN)

# Configura los pines
pir_line.request(consumer="pir_sensor", type=gpiod.LINE_REQ_DIR_IN)
led_line.request(consumer="led", type=gpiod.LINE_REQ_DIR_OUT)

print("Esperando movimiento...")

try:
    while True:
        motion = pir_line.get_value()
        if motion == 1:
            print("Movimiento detectado!")
            led_line.set_value(1)
        else:
            led_line.set_value(0)
            print("Sin movimiento, apagando")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
    led_line.set_value(0)

finally:
    pir_line.release()
    led_line.release()
