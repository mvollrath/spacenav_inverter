import rospy
from geometry_msgs.msg import Twist


class TwistInverter:
    """
    Publishes the inverse of incoming geometry_msgs/Twist messages.
    """
    def __init__(self, inverted_pub):
        self.inverted_pub = inverted_pub

    def handle_twist(self, twist_msg):
        inverted_msg = Twist()
        inverted_msg.linear.x = -twist_msg.linear.x
        inverted_msg.linear.y = -twist_msg.linear.y
        inverted_msg.linear.z = -twist_msg.linear.z
        inverted_msg.angular.x = -twist_msg.angular.x
        inverted_msg.angular.y = -twist_msg.angular.y
        inverted_msg.angular.z = -twist_msg.angular.z
        self.inverted_pub.publish(inverted_msg)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
