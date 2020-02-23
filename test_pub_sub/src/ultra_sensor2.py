#!/usr/bin/env python
# Ultrasonic-Sensor

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float32
GPIO.setmode(GPIO.BCM)

#Setting the GPIO Pins
TRIG = 6
ECHO = 5

#Initializing our TRIG and ECHO
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#Object Detection and Distance Measurement of Object
def distance_of_object():

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

    pub = rospy.Publisher('obj_distance', Float32, queue_size=10)
    rate = rospy.Rate(1)
    distance_to_pub = Float32()

    while not rospy.is_shutdown():
        distance_pub = distance_of_object()
        print "Distance is:", distance_pub
        distance_to_pub.data = distance_pub
        pub.publish(distance_to_pub)

        rospy.loginfo(obj_distance)
        rate.sleep()

if __name__ == '__main__':

    rospy.init_node("simple_publisher")

    try:
        while True:
            publisher()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Object Detection Stopped")
        GPIO.cleanup()

