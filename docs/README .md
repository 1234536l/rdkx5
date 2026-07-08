# Medical Gloves Sorting Robot
## Introduction
This project runs on Horizon RDK X5, uses USB camera to detect medical nitrile gloves. It converts pixel coordinates to robot coordinates, and controls collaborative manipulator with soft pneumatic gripper to finish sorting, no vacuum suction cup.

## Environment
Hardware: Horizon RDK X5, 7DoF manipulator, soft gripper, USB camera
OS: Ubuntu 22.04
Algorithm: YOLOv8 object detection

## File Structure
- utils: Image preprocess & coordinate transformation tools
- samples/vision: Camera detection code
- tros: Manipulator & gripper control logic
- datasets: Test glove images
- docs: Wiring & calibration documents

## Run Command
1. Install dependencies
`pip3 install -r requirements.txt`
2. Build workspace
`colcon build && source install/setup.bash`
3. Start vision detection
`python3 samples/vision/glove_detect.py`
4. Start manipulator sorting
`ros2 run tros arm_grasp_node`