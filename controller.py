import pymorse
import time

def send_pose(s, morse, x, y, yaw):
    s.publish({'x' : x, 'y' : y, 'z' : 0.0, \
               'yaw' : yaw, 'pitch' : 0.0, 'roll' : 0.0})
    time.sleep(1)

with pymorse.Morse("localhost", 4000) as simu:



    teleport_stream = simu.rosie.teleport
    kuka_client = simu.rosie.arm

    kuka_client.set_rotation('kuka_2', -1.57)
    time.sleep(1) 

    send_pose(teleport_stream, simu, 1.0, 5, 0.0)
    time.sleep(1)

    obj = simu.rosie.arm.gripper.grab()

    print(obj)

    send_pose(teleport_stream, simu, -2.0, 0, 0.0)
    time.sleep(1)

    obj = simu.rosie.arm.gripper.release()

    print(obj)

    obj = simu.rosie.arm.gripper.grab()

    print(obj)

    obj = simu.rosie.arm.gripper.release()

    print(obj)


