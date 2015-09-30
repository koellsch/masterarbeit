#!/usr/bin/python
import rospy
import unittest
import rostest

from atf_recorder import RecordingManager


class AtfApp:
    def __init__(self):
        self.recorder = RecordingManager("testblock")
        pass

    def execute(self):
        self.recorder.start()
        self.recorder.stopp()
        pass


class Test(unittest.TestCase):

    def setUp(self):
        self.app = AtfApp()

    def test_Recording(self):

        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_recording')
    rostest.rosrun("atf_app", 'test_name', Test, sysargs=None)
