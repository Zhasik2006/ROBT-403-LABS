#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

global current_pos 
current_pos = 0.0
pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)

def joint_move():
    rospy.init_node('Zhassulan_joint1_move', anonymous=True)
    rospy.loginfo("Current position:" + str(current_pos))
    global start_time 
    start_time = rospy.get_rostime()
    while not rospy.is_shutdown():
	step()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('Shutdown')


def step():
    global start_time
    global current_pos
    current_time = rospy.get_rostime()
    if ((current_time.secs - start_time.secs) >= 5):
	    if (current_pos == 0.0):
		pub.publish(1.0)
		current_pos = 1.0
	    else:
		pub.publish(0.0)
		current_pos = 0.0
	    start_time = rospy.get_rostime()
	    rospy.loginfo('Position changed to ' + str(current_pos))

if __name__ == '__main__':
    try:
        joint_move()
    except rospy.ROSInterruptException:
        pass




