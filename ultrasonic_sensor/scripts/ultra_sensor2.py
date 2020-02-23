#!/usr/bin/env python
# Ultrasonic-Sensor

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float32
GPIO.setmode(GPIO.BCM)

#Setting the GPIO Pins
TRIG = 23
ECHO = 24

#Initializing our TRIG and ECHO
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#Object Detection and Distance Measurement of Object
def object_distance():

    print "Distance Measurement In Progress"

    #Setting up our Trig to high in order for signal to be sent
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start_pulse = time.time()

    while GPIO.input(ECHO) == 1:
        end_pulse = time.time()

    #Calculating pulse duration and distance
    pulse_time = end_pulse - start_pulse
    distance = round((pulse_time * 17000),2)

    return distance

# Creating a publisher that will send ROS Master the topic that will
# be shared to the subscriber node(Motors Code)
def publisher():

    pub = rospy.Publisher('Object Distance', Float32, queue_size=10)
    rate = rospy.Rate(1)
    msg_to_publish = Float32();

    while not rospy.is_shutdown():
        msg_to_publish.data = distance
        pub.publish(msg_to_publish)
        rospy.logininfo(distance)
        rate.sleep()

if __name__ == '__main__':

    rospy.init_node("simple_publisher")
    publisher()

    try:
        while True:
            obj_distance = object_distance()
            print "Distance is " obj_distance "cm"
            time.sleep(1)
    except KeyboardInterrupt:
        print("Object Detection Stopped")
        GPIO.cleanup()
