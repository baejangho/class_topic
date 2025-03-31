#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ROS Publisher 및 Subscriber가 1개의 Node에 포함된 형태

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist, Vector3

rospy.init_node("ros_publisher_subscriber_basic")
TARGET_POSE_X = 10.0

def callback(_data, _publisher):
    cmd = Twist()
    print('position;',_data.x)
    if abs(_data.x - TARGET_POSE_X) < 0.1:
        cmd.linear.x=0
        _publisher.publish(cmd)
        rospy.loginfo("Goal Reached, Stop")
        rospy.signal_shutdown("Goal Reached, Process Shutdown")
    elif _data.x < TARGET_POSE_X:
        cmd.linear.x=0.5
        _publisher.publish(cmd)
        rospy.loginfo("Go Forward to Goal")
    elif _data.x > TARGET_POSE_X:
        cmd.linear.x=-0.5
        _publisher.publish(cmd)
        rospy.loginfo("Go Backward to Goal")

cmd_vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=5)
rospy.Subscriber("/turtle1/pose", Pose, callback, cmd_vel_pub)

while not rospy.is_shutdown():
    rospy.spin()