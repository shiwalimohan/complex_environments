from morse.builder import *

# Append PR2 robot to the scene
rosie = BasePR2()
rosie.translate(x=1, y=0, z=0.0)

### add semantic camera
s_camera = SemanticCamera()
s_camera.translate(x=0, y=0, z=1)
s_camera.add_interface('socket')
rosie.append(s_camera)

### add pose
pose = Pose()
pose.add_interface('socket')
rosie.append(pose)

gripper = Gripper()
gripper.translate(x=1,z=0.8)
gripper.rotate(y=math.pi/2)
gripper.properties(Angle = 180.0, Distance=2.0)
gripper.add_interface('socket')
rosie.r_arm.append(gripper)

table = PassiveObject('props/objects','SmallTable')
table.setgraspable()
table.translate(x=0, y=0, z=0)
table.rotate(z=0.2)

plate = PassiveObject('props/kitchen_objects', 'Plate')
plate.setgraspable()
plate.translate(x=0, y=0, z=0.92)

tape1 = PassiveObject(prefix='BlackVideotape')
tape1.properties(Object = True, Graspable = True, Label = "BlackTape")
tape1.translate(x=3, y=5, z=0)

# teleport = Teleport()
# rosie.append(teleport)
# teleport.add_stream('socket')

keyboard = Keyboard()
keyboard.name = 'keyboard_control'
rosie.append(keyboard)

# Set scenario
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
