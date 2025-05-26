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


class LEDController():
	def __init__(self, parent):
		self.parent = parent
		self.leds = 0
		
	def turnOn(self):
		print("[LEDS] Encender luces")
		
	def turnOff(self):
		print("[LEDS] Apagar luces")
		
	def setBrightness(self, brightness):
		print(f"[LEDS] Cambiar brillo a {brightness}")
