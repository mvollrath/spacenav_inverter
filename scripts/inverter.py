#!/usr/bin/env python

"""
Subscribes to spacenav messages and publishes the inverse.
"""

import rospy
from geometry_msgs.msg import Twist
from spacenav_inverter import TwistInverter


def main():
    rospy.init_node('spacenav_inverter')

    inverted_pub = rospy.Publisher(
        '/spacenav/twist_inverted',
        Twist,
        queue_size=1
    )

    inverter = TwistInverter(inverted_pub)

    rospy.Subscriber('/spacenav/twist', Twist, inverter.handle_twist)

    rospy.spin()

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
