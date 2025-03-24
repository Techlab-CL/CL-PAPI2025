import RPi.GPIO as GPIO
import time

# Zet de GPIO-mode op BCM
GPIO.setmode(GPIO.BCM)

# Stel de GPIO-pinnen in
sensor_pin = 26   # GPIO 26 voor de bodemvochtsensor (signaal)
led_pin = 19      # GPIO 19 voor de LED

# Zet de GPIO-pinnen in de juiste modus
GPIO.setup(sensor_pin, GPIO.IN)   # Sensor pin als input
GPIO.setup(led_pin, GPIO.OUT)     # LED pin als output

# Start een oneindige loop die de vochtigheid leest
try:
    while True:
        # Lees de waarde van de sensor (0 = droog, 1 = vochtig)
        if GPIO.input(sensor_pin) == GPIO.HIGH:  # Sensor geeft HIGH als de grond vochtig is
            print("De aarde is vochtig, LED aan.")
            GPIO.output(led_pin, GPIO.HIGH)  # Zet de LED uit als de aarde vochtig is
        else:
            print("De aarde is droog, LED uit!")
            GPIO.output(led_pin, GPIO.LOW)  # Zet de LED aan als de aarde droog is

        # Wacht 1 seconde voor de volgende meting
        time.sleep(1)

# Zorg ervoor dat we de GPIO netjes opruimen bij het afsluiten van het programma
except KeyboardInterrupt:
    print("Programma gestopt door gebruiker.")
finally:
    GPIO.cleanup()