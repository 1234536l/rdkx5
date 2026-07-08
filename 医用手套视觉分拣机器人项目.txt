# 医用手套视觉分拣机器人项目
## 项目概述
基于地平线RDK X5开发，USB工业摄像头实时识别医用丁腈手套，通过坐标转换算法将像素坐标转为机械臂世界坐标，控制7自由度协作机械臂搭配柔性气动夹爪完成自动分拣，全程无真空吸盘结构。

## 软硬件环境
### 硬件
- 主控：地平线RDK X5
- 执行机构：7自由度协作机械臂 + 柔性硅胶气动夹爪
- 感知设备：USB工业相机

### 软件
- 系统：Ubuntu 22.04
- 机器人框架：TROS
- 视觉算法：YOLOv8目标检测
- Python版本：3.8+

## 工程目录介绍
- utils：图像预处理、像素-机械臂坐标转换通用工具
- samples/vision：摄像头实时视觉识别主程序
- tros：机械臂运动控制、夹爪开合逻辑
- datasets：医用手套测试样本图片
- docs：硬件接线、标定、运行调试文档
- LICENSE：Apache2.0开源协议

## 一键运行流程
1. 安装依赖
pip3 install -r requirements.txt
2. 编译机械臂TROS工程
colcon build --packages-select tros
source install/setup.bash
3. 启动视觉识别终端
python3 samples/vision/glove_detect.py
4. 启动机械臂分拣终端
ros2 run tros arm_grasp_node

## 核心功能说明
1. 视觉模块：摄像头画面实时推理，识别画面内医用手套并输出目标像素中心点
2. 坐标转换：通过相机内外参矩阵，将二维像素转换为机械臂可执行三维世界坐标
3. 机械臂分拣：接收坐标后自动完成「移动至上方-下降-夹爪闭合夹持-抬升-转运放置-松爪复位」完整流程