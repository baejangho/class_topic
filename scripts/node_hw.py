#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ROS Publisher 및 Subscriber가 1개의 Node에 포함된 형태

import rospy
from std_msgs.msg import Int64

rospy.init_node("hw1")

class Turtle_Mover(object):
    def __init__(self):
        self.int_pub = rospy.Publisher("int_i", Int64, queue_size=5)
        rospy.Timer(rospy.Duration(1.0/1.0), self.timerCallback) # 30.0을 변경하여, 초당 처리 횟수 지정 가능
        self.int_i = 0 
   
    def timerCallback(self, _event): # event는 TimerCallback 함수에 필수적으로 필요하며, 사용할 필요 없음
        self.int_i = self.int_i + 1
        self.int_pub.publish(Int64(self.int_i))

            



new_class = Turtle_Mover()
while not rospy.is_shutdown():
    rospy.spin()