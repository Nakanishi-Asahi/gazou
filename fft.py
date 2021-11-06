from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def main():
    img = Image.open('lena_sin_noise.jpg')
    gray_img = img.convert('L')
    f_xy = np.asarray(gray_img)
    f_uv = np.fft.fft2(f_xy)
    shifted_f_uv = np.fft.fftshift(f_uv)
    magnitude_spectrum2d = 20 * np.log(np.absolute(shifted_f_uv))
    filtered = shifted_f_uv
    height, width = filtered.shape
    filter_h = 5
    filter_w = 5
    filter_y = 70
    filter_x = 80
    for i in range(filter_h):
        for j in range(filter_w):
            y = filter_y - int(filter_h / 2) + i
            x = filter_x - int(filter_w / 2) + j
            filtered[y, x] *= 0
    filter_y = 80
    filter_x = 70
    for i in range(filter_h):
        for j in range(filter_w):
            y = filter_y - int(filter_h / 2) + i
            x = filter_x - int(filter_w / 2) + j
            filtered[y, x] *= 0
    magnitude_filtered = 20 * np.log(np.absolute(filtered))
    unshifted_f_uv = np.fft.fftshift(filtered)
    i_f_xy = np.fft.ifft2(unshifted_f_uv).real
    fig, axes = plt.subplots(1, 3, figsize = (8, 4))
    for ax in axes:
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
    axes[0].imshow(f_xy, cmap = 'gray')
    axes[0].set_title('Input Image')
    axes[1].imshow(magnitude_filtered, cmap = 'gray')
    axes[1].set_title('Magnitude Spectrum')
    axes[2].imshow(i_f_xy, cmap = 'gray')
    axes[2].set_title('Reversed Image')
    plt.show()

if __name__ == '__main__':
    main()
