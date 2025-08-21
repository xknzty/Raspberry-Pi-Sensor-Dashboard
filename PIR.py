import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from signal import pause
import time
LedPin = 27
pir = MotionSensor(17)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
def motion_function():
    print("Bewegung erkannt...")
    GPIO.output(LedPin, False)
    time.sleep(5)
    
def no_motion_function():
    print("Keine Bewegung")
    GPIO.output(LedPin, True)


pir.when_activated = motion_function
pir.when_deactivated = no_motion_function

pause()