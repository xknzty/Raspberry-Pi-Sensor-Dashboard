from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from signal import pause
import time


app = Flask(__name__)


LedPin = 27
pir = MotionSensor(17)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
motion_state = "Keine Bewegung"
    
def motion_function():
        
    
    global motion_state
    motion_state = "Bewegung erkannt..."
    GPIO.output(LedPin, False)
    time.sleep(5)
        
        
def no_motion_function():
    GPIO.output(LedPin, True)
    global motion_state
    motion_state =  "Keine Bewegung"
        
        


pir.when_activated = motion_function
pir.when_deactivated = no_motion_function


@app.route("/")
def PIR():    
    return render_template("index.html", state=motion_state)

@app.route("/status")
def status():
    return jsonify({"state":motion_state})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)