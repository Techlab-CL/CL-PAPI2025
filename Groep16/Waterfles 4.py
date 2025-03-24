import RPi.GPIO as GPIO
import time

# Instellen van de GPIO mode
GPIO.setmode(GPIO.BCM)

# Pinconfiguratie
water_sensor_pin = 17  # De GPIO pin waarop de water sensor is aangesloten
led_pin = 18           # De GPIO pin waarop de LED is aangesloten

# Instellen van de pinnen
GPIO.setup(water_sensor_pin, GPIO.IN)  # Water sensor is input
GPIO.setup(led_pin, GPIO.OUT)          # LED is output

try:
    while True:
        if GPIO.input(water_sensor_pin) == GPIO.HIGH:  # Geen water (sensor geeft HIGH signaal)
            GPIO.output(led_pin, GPIO.LOW)  # Zet de LED uit
            print("Geen water, LED uit!")
        else:
            GPIO.output(led_pin, GPIO.HIGH)  # Zet de LED aan
            print("Water gedetecteerd, LED aan!")
        time.sleep(1)  # Wacht een seconde voor de volgende meting

except KeyboardInterrupt:
    print("Programma gestopt")
    GPIO.cleanup()  # Zorg ervoor dat de GPIO netjes wordt afgesloten