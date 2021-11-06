import numpy as np
import cv2

def main():
    img = np.zeros((480, 640, 3), dtype = np.uint8)
    cv2.circle(img, (320, 240), 200, (0, 127, 255), -1)
    cv2.imwrite('out.jpg', img)

main()
