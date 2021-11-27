'''
Description: 
FilePath: \Pysource_Kalman_filter\orange_detector.py
Autor: Rainche
Date: 2021-10-28 22:06:14
LastEditTime: 2021-11-27 15:24:47
'''
#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
import numpy as np


class OrangeDetector:
    def __init__(self):
        # Create mask for orange color
        self.low_orange = np.array([11, 128, 90])
        self.high_orange = np.array([179, 255, 255])

    def detect(self, frame):
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks with color ranges
        mask = cv2.inRange(hsv_img, self.low_orange, self.high_orange)

        # Find Contours
        _ , contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        box = (0, 0, 0, 0)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            box = (x, y, x + w, y + h)
            break

        return box