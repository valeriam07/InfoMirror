from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/turn_on_leds")
def turn_on_leds():
    print("LEDs encendidos.")
    return "LEDs encendidos."

@app.route("/turn_off_leds")
def turn_off_leds():
    print("LEDs apagados.")
    return "LEDs apagados."

@app.route("/turn_on_screen")
def turn_on_screen():
    print("Pantalla encendida.")
    return "Pantalla encendida."

@app.route("/turn_off_screen")
def turn_off_screen():
    print("Pantalla apagada.")
    return "Pantalla apagada."

@app.route("/adjust_brightness/<int:value>")
def adjust_brightness(value):
    print(f"Ajustando brillo al {value}%.")
    return f"Brillo ajustado al {value}%."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
