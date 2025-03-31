#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ROS Publisher 및 Subscriber가 1개의 Node에 포함된 형태

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist, Vector3

rospy.init_node("ros_publisher_subscriber_basic")
TARGET_POSE_X = 10.0

class Turtle_Mover(object):
    def __init__(self):
        self.pose_init = False
        self.cmd_vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=5)
        rospy.Subscriber("/turtle1/pose", Pose, self.callback)
        rospy.Timer(rospy.Duration(1.0/2.0), self.timerCallback) # 30.0을 변경하여, 초당 처리 횟수 지정 가능
        
    def callback(self, _data): # 단순 데이터 저장용으로 사용, 실제 처리는 Timer Callback에서 진행
        self.pose_init = True
        self.pose_data = _data
        print(self.pose_data)
   
    def timerCallback(self, _event): # event는 TimerCallback 함수에 필수적으로 필요하며, 사용할 필요 없음
        if self.pose_init == False:
            return

        if abs(self.pose_data.x - TARGET_POSE_X) < 0.1:
            self.cmd_vel_pub.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, 0)))
            rospy.loginfo("Goal Reached, Stop")
            rospy.signal_shutdown("Goal Reached, Process Shutdown")

        elif self.pose_data.x < TARGET_POSE_X:
            self.cmd_vel_pub.publish(Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0)))
            rospy.loginfo("Go Forward to Goal")
        elif self.pose_data.x > TARGET_POSE_X:
            self.cmd_vel_pub.publish(Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, 0)))
            rospy.loginfo("Go Backward to Goal")

new_class = Turtle_Mover()
while not rospy.is_shutdown():
    rospy.spin()