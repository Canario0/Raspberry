from gpiozero import LED
from time import sleep
from signal import pause

led = LED(17)

# while True:
#     led.on()
#     sleep(2)
#     led.off()
#     sleep(2)

led.blink()

pause()