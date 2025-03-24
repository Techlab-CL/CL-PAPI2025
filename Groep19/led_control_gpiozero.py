from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

led1.on()
led2.on()
led3.on()

print("im gonna fart in 5 seconds")
sleep(5)

led1.off()
led2.off()
led3.off()

print("sorry i farted")