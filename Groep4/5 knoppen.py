import tkinter as tk
import RPi.GPIO as GPIO
import time

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)

# Stel de pin voor de servo in (bijvoorbeeld pin 18)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Maak een PWM-object voor de servo (frequentie 50Hz)
servo = GPIO.PWM(servo_pin, 50)
servo.start(7.5)  # Start de servo met een 7.5% duty cycle (meestal 90 graden voor de SG90)

# Knoppen instellingen (GPIO pinnen en corresponderende servo posities)
buttons = {
    17: 5,   # Knop 1: 5%
    27: 25,  # Knop 2: 25%
    22: 50,  # Knop 3: 50%
    23: 75,  # Knop 4: 75%
    24: 100, # Knop 5: 100%
}

# Correcte GPIO setup voor knoppen
for pin in buttons.keys():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GUI-opbouw
root = tk.Tk()
root.title("Servo Controller")
root.geometry("400x200")

slider = tk.Canvas(root, width=300, height=30, bg="lightgray")
slider.pack(pady=20)
bar = slider.create_rectangle(0, 5, 0, 25)  # Balk die de huidige servo-positie aangeeft

# Functie om knoppen uit te lezen en de servo te verplaatsen
def check_buttons():
    for pin, position in buttons.items():
        if GPIO.input(pin) == GPIO.HIGH:
            update_servo(position)
    root.after(100, check_buttons)  # Controleer elke 100 ms of een knop is ingedrukt

# Functie om de servo te besturen
def update_servo(position):
    # De servo positie omrekenen naar een geschikte duty cycle
    duty_cycle = (position / 100) * 10 + 2.5  # Bereken de juiste duty cycle voor de servo (2.5% tot 12.5%)
    print(f"Setting duty cycle: {duty_cycle}%")

    # Zorg ervoor dat de duty cycle in het bereik van 2.5% en 12.5% blijft
    if duty_cycle < 2.5:
        duty_cycle = 2.5
    elif duty_cycle > 12.5:
        duty_cycle = 12.5

    servo.ChangeDutyCycle(duty_cycle)

    # Update de GUI-balk om de servo positie weer te geven
    new_x = (position / 100) * 300  # Bereken de nieuwe positie van de balk (0 tot 300)
    slider.coords(bar, 0, 5, new_x, 25)  # Update de coördinaten van de balk

# Start de knopcontrole
check_buttons()

# Start de GUI
root.mainloop()

# Opruimen bij afsluiten
servo.stop()
GPIO.cleanup()
