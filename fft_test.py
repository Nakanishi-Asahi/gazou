from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def main():
    img = Image.open('lena.jpg')
    gray_img = img.convert('L')
    f_xy = np.asarray(gray_img)
    f_uv = np.fft.fft2(f_xy)
    print(f_uv)
    shifted_f_uv = np.fft.fftshift(f_uv)
    magnitude_spectrum2d = 20 * np.log(np.absolute(shifted_f_uv))
    unshifted_f_uv = np.fft.fftshift(shifted_f_uv)
    i_f_xy = np.fft.ifft2(unshifted_f_uv).real
    fig, axes = plt.subplots(1, 3, figsize = (8, 4))
    for ax in axes:
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
    axes[0].imshow(f_xy, cmap = 'gray')
    axes[0].set_title('Input Image')
    axes[1].imshow(magnitude_spectrum2d, cmap = 'gray')
    axes[1].set_title('Magnitude Spectrum')
    axes[2].imshow(i_f_xy, cmap = 'gray')
    axes[2].set_title('Reversed Image')
    plt.show()

if __name__ == '__main__':
    main()
