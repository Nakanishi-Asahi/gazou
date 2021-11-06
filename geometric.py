import numpy as np
import cv2
import math

def main():
    gry = cv2.imread('gaussian_noise.jpg', 0)
    height, width = gry.shape
    filtered = gry
    for i in range(height - 2):
        for j in range(width - 2):
            y = i + 1
            x = j + 1
            integral = 1
            for c in range(3):
                for r in range(3):
                    integral *= gry[y - 1 + c, x - 1 + r]
            filtered[y, x] = math.pow(integral, 1 / 9)
    cv2.imwrite('geometric.jpg', filtered)

main()
