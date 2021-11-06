import numpy as np
import cv2

def main():
    gry = cv2.imread('lena.jpg', 0)
    height, width = gry.shape
    pep = gry
    for i in range(height):
        for j in range(width):
            rand = np.random.rand()
            if 0.0 <= rand and rand < 0.1:
                pep[i, j] = 0

    cv2.imwrite('pepper_noise.jpg', pep)

main()
