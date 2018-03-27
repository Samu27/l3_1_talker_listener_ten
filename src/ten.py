#!/usr/bin/env python2
import rospy
from std_msgs.msg import String


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "10 messages %s", rospy.get_time())

def ten():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('ten', anonymous=True)

	rospy.Subscriber("filtered", String, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()


if __name__ == '__main__':
	ten()
