'''
Description: from https://pysource.com/2021/11/02/kalman-filter-predict-the-trajectory-of-an-object/
FilePath: \Pysource_Kalman_filter\orange_prediction.py
Autor: Rainche
Date: 2021-10-28 22:06:14
LastEditTime: 2021-11-27 15:54:49
'''
#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
from orange_detector import OrangeDetector
from kalmanfilter import KalmanFilter

cap = cv2.VideoCapture("orange.mp4")

# Load detector
od = OrangeDetector()

# Load Kalman filter to predict the trajectory
kf = KalmanFilter()

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

    # predicted = kf.predict(cx, cy)
    predicted = kf.predict(x, y, x2, y2)
    
    cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 4)
    cv2.rectangle(frame, (predicted[0], predicted[1]), (predicted[2], predicted[3]), (255, 0, 0), 4)
    # cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    # cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(150)
    if key == 27:
        break