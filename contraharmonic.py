import numpy as np
import cv2
import math

def main():
    gry = cv2.imread('salt_noise.jpg', 0)
    height, width = gry.shape
    filtered = gry
    q_value = -1.5
    for i in range(height - 2):
        for j in range(width - 2):
            y = i + 1
            x = j + 1
            integral1 = 0
            integral2 = 0
            for c in range(3):
                for r in range(3):
                    integral1 += math.pow(gry[y - 1 + c, x - 1 + r], q_value + 1)
                    integral2 += math.pow(gry[y - 1 + c, x - 1 + r], q_value)
            filtered[y, x] = integral1 / integral2
    cv2.imwrite('contraharmonic_salt.jpg', filtered)

main()
