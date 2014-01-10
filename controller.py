import pymorse
import time

def send_pose(s, morse, x, y, yaw):
    s.publish({'x' : x, 'y' : y, 'z' : 0.0, \
               'yaw' : yaw, 'pitch' : 0.0, 'roll' : 0.0})
    time.sleep(0.1)

with pymorse.Morse("localhost", 4000) as simu:

    # teleport_stream = simu.rosie.teleport

    # send_pose(teleport_stream, simu, -1.0, 0, 0.0)
    time.sleep(0.1)

    obj = simu.rosie.torso.r_arm.gripper.release()
    print(obj)

    time.sleep(1)
        
