import numpy as np
import cv2
import math

def main():
    gry = cv2.imread('lena.jpg', 0)
    height, width = gry.shape
    noise = np.random.normal(0, 20, (height, width))
    gaus = gry + noise
    cv2.imwrite('gaussian_noise.jpg', gaus)

main()
