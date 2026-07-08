Medical Glove Visual Sorting Robot Project
Project Overview
Developed based on Horizon RDK X5, this system uses a USB industrial camera to identify medical nitrile gloves in real time. A coordinate conversion algorithm converts pixel coordinates into robotic arm world coordinates, and controls a 7-degree-of-freedom collaborative robotic arm equipped with a flexible pneumatic gripper to realize automatic sorting. No vacuum suction cup structure is adopted throughout the workflow.
Hardware & Software Environment
Hardware
Main Controller: Horizon RDK X5
Actuator: 7-DOF collaborative robotic arm + flexible silicone pneumatic gripper
Sensing Device: USB industrial camera
Software
Operating System: Ubuntu 22.04
Robot Framework: TROS
Vision Algorithm: YOLOv8 Object Detection
Python Version: 3.8 and above
Project Directory Introduction
utils: General tools for image preprocessing and pixel-to-robotic-arm coordinate conversion
samples/vision: Main program for real-time camera vision recognition
tros: Robotic arm motion control and gripper opening/closing logic
datasets: Test sample images of medical gloves
docs: Documents for hardware wiring, calibration and operation debugging
LICENSE: Apache 2.0 Open Source License
One-Click Operation Procedure
Install dependencies
bash
运行
pip3 install -r requirements.txt

Compile the TROS project of the robotic arm
bash
运行
colcon build --packages-select tros
source install/setup.bash

Launch the vision recognition terminal
bash
运行
python3 samples/vision/glove_detect.py

Launch the robotic arm sorting terminal
bash
运行
ros2 run tros arm_grasp_node

Core Function Description
Vision Module: Real-time inference of camera frames, identifies medical gloves in the frame and outputs the pixel center point of targets
Coordinate Conversion: Converts 2D pixel coordinates into 3D world coordinates executable by the robotic arm via camera intrinsic and extrinsic parameter matrices
Robotic Arm Sorting: After receiving coordinates, automatically completes the full workflow: move above target → descend → close gripper for clamping → lift up → transfer and place → release gripper and reset
