import numpy as np
import cv2
import math

def main():
    gry = cv2.imread('lena.jpg', 0)
    width, height = gry.shape
    out = np.zeros((height, width), dtype = np.uint8)
    a = 2
    b = -3
    c = -1000
    shuki = 20
    noise_strength = 10
    for w in range(width):
        for h in range(height):
            dist = math.fabs(a * w + b * h + c) / math.sqrt(a ** 2 + b ** 2)
            out[h][w] = noise_strength * math.sin(2 * math.pi / shuki * dist)
    cv2.imwrite('sin_noise.jpg', out)

main()
