import numpy as np
import cv2

def main():
    gry = cv2.imread('lena.jpg', 0)
    cv2.imwrite('lena_gry.jpg', gry)

main()
