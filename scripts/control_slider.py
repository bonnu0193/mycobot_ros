#!/usr/bin/env python2
# from std_msgs.msg import String
import time, subprocess

import rospy
from sensor_msgs.msg import JointState

from pymycobot.mycobot import MyCobot


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "%s", data.position)
    # print(data.position)
    data_list = []
    print(data.position)
    for index, value in enumerate(data.position):
        data_list.append(value)

    mc.send_radians(data_list, 80)
    # time.sleep(0.5)
    
def listener():
    rospy.init_node('control_slider', anonymous=True)

    rospy.Subscriber("joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    print('sart')
    port = subprocess.check_output(['echo -n /dev/ttyAMA0'], 
                                    shell=True).decode()
    print(port)
    mc = MyCobot(port, 1000000)
    print(mc)
    listener()
