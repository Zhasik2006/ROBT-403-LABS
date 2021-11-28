#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

current_pos = 0.0
start_time = rospy.get_rostime()

pub = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=10)

def joint5_move():
    rospy.init_node('Zhassulan_joint5_move', anonymous=True)
    rospy.loginfo("Current position:" + str(current_pos))

    while not rospy.is_shutdown():
	step()


    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('Shutdown')


def step():
    current_time = rospy.get_rostime()
    if ((current_time.secs - start_time.secs) >= 5):
	    if (current_pos == 0.0):
		pub.publish(1.0)
	    else:
		pub.publish(0.0)
	    rospy.loginfo('Position changed to ' + str(current_pos))

if __name__ == '__main__':
    try:
        joint5_move()
    except rospy.ROSInterruptException:
        pass




