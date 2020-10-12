#Made by TheFenrisLycaon
#Commited on 10th OCT, 2020

import cv2
import numpy as np
import time

print("""
Mr. Robot:  Hey kiddo !! Let's Get Anonymus !
         	Prepare to get invisible .....................
    """)

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0

def nothing():
	pass

for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lv", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while(cap.isOpened()):
    ret, img = cap.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LH", "Tracking")
    l_v = cv2.getTrackbarPos("LH", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking" )
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    blurred = cv2.GaussianBlur(hsv, value, 0)

    low = np.array([l_h,l_s,l_v])
    high = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, low, high)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv2.imshow('Anonimity is Key !', img)
    k = cv2.waitKey(10)
    if k == 27:
        break