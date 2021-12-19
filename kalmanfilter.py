'''
Description: https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
FilePath: \Pysource_Kalman_filter\kalmanfilter.py
Autor: Rainche
Date: 2021-10-28 22:06:14
LastEditTime: 2021-12-19 14:28:02
'''

import cv2
import numpy as np


class KalmanFilter:
    kf = cv2.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)


    def predict(self, coordX, coordY):
        ''' This function estimates the position of the object'''
        measured = np.array([[np.float32(coordX)], [np.float32(coordY)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        x, y = int(predicted[0]), int(predicted[1])
        return x, y

