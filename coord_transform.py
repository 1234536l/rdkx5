import numpy as np

class Camera2Robot:
    def __init__(self, cam_intrinsic, cam2robot_matrix):
        self.K = np.array(cam_intrinsic)
        self.T = np.array(cam2robot_matrix)

    def pixel2camera(self, pixel_x, pixel_y, depth):
        fx, fy = self.K[0,0], self.K[1,1]
        cx, cy = self.K[0,2], self.K[1,2]
        x_cam = (pixel_x - cx) * depth / fx
        y_cam = (pixel_y - cy) * depth / fy
        return np.array([x_cam, y_cam, depth, 1.0])
    
    def camera2robot(self, cam_point):
        robot_point = self.T @ cam_point
        return robot_point[:3]

    def pixel2robot(self, px, py, depth):
        cam_xyz = self.pixel2camera(px, py, depth)
        return self.camera2robot(cam_xyz)