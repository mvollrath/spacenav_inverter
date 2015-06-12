#!/usr/bin/env python

PKG = 'spacenav_inverter'
NAME = 'test_spacenav_inverter'

from geometry_msgs.msg import Twist
from rosnode import rosnode_ping
from rostopic import get_topic_class
import unittest
import time

SPINUP_DELAY = 0.1  # seconds


class TestSpacenavInverter(unittest.TestCase):
    def test_node(self):
        """ Verify that we can ping the node. """
        result = rosnode_ping('test_spacenav_inverter', max_count=1)
        self.assertTrue(result)

    def test_topic(self):
        """ Verify that the topic exists with the right message type. """
        cls, name, fn = get_topic_class('/spacenav/twist_inverted')
        self.assertEqual(cls, Twist)


if __name__ == '__main__':
    import rostest
    time.sleep(SPINUP_DELAY)
    rostest.rosrun(PKG, NAME, TestSpacenavInverter)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
