# Ultrasonic-Sensor
# Ultrasonic-Sensor
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

Trig = 23 
Echo = 24
LED = 27
Buzzer = 22

print "Distance Measurement In Progress"

#Initializing our TRIG and ECHO
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

#Initizalizing our LED and Buzzer
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.output(LED,GPIO.LOW)         #We are having the LED and Buzzer 
GPIO.output(Buzzer,GPIO.LOW)

try:
    while True:

        GPIO.output(Trig, False)
        print "Sensor is Settling..."
        time.sleep(0.5)

        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:
          pulse_start = time.time()

        while GPIO.input(Echo) == 1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17000

        distance = round(distance, 2)

        print "Distance:",distance,"cm"
        
        #Turning on LED and Buzzer 
        if distance < 10:
            GPIO.output(LED,GPIO.HIGH)
            GPIO.output(Buzzer, GPIO.HIGH)
        else:
            GPIO.output(LED,GPIO.LOW)
            GPIO.output(Buzzer, GPIO.LOW)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    GPIO.cleanup()
