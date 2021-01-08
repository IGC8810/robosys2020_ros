#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('pub_word')
pub = rospy.Publisher('word', String, queue_size = 1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish('Hello World!!')
    rate.sleep()

