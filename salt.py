import numpy as np
import cv2

def main():
    gry = cv2.imread('lena.jpg', 0)
    height, width = gry.shape
    salt = gry
    for i in range(height):
        for j in range(width):
            rand = np.random.rand()
            if 0.0 <= rand and rand < 0.1:
                salt[i, j] = 255

    cv2.imwrite('salt_noise.jpg', salt)

main()
