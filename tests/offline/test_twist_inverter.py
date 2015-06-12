#!/usr/bin/env python

PKG = 'spacenav_inverter'
NAME = 'test_twist_inverter'

import rospy
import unittest

from spacenav_inverter import TwistInverter
from geometry_msgs.msg import Twist

TEST_LINEAR_X = 1
TEST_LINEAR_Y = 2
TEST_LINEAR_Z = 3
TEST_ANGULAR_X = 4
TEST_ANGULAR_Y = 5
TEST_ANGULAR_Z = 6


class MockPublisher:
    def __init__(self):
        self.published = []

    def publish(self, msg):
        self.published.append(msg)


class TestTwistInverter(unittest.TestCase):
    def setUp(self):
        self.mock_pub = MockPublisher()
        self.twist_inverter = TwistInverter(self.mock_pub)

    def test_handle_twist(self):
        tt = Twist()
        tt.linear.x = TEST_LINEAR_X
        tt.linear.y = TEST_LINEAR_Y
        tt.linear.z = TEST_LINEAR_Z
        tt.angular.x = TEST_ANGULAR_X
        tt.angular.y = TEST_ANGULAR_Y
        tt.angular.z = TEST_ANGULAR_Z
        self.twist_inverter.handle_twist(tt)

        self.assertEqual(len(self.mock_pub.published), 1)

        out = self.mock_pub.published[0]
        self.assertEqual(out.linear.x, -TEST_LINEAR_X)
        self.assertEqual(out.linear.y, -TEST_LINEAR_Y)
        self.assertEqual(out.linear.z, -TEST_LINEAR_Z)
        self.assertEqual(out.angular.x, -TEST_ANGULAR_X)
        self.assertEqual(out.angular.y, -TEST_ANGULAR_Y)
        self.assertEqual(out.angular.z, -TEST_ANGULAR_Z)


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, NAME, TestTwistInverter)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
