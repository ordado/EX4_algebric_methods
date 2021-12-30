# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
from PIL import Image
import numpy as np
from numpy.linalg import svd

if __name__ == '__main__':
    image = Image.open("tiger.jpg")
    pix = np.array(image)
    red = pix[:, :, 0]
    blue = pix[:, :, 1]
    green = pix[:, :, 2]
    u_r, sigma_r, vt_r = svd(red)
    u_b, sigma_b, vt_b = svd(blue)
    u_g, sigma_g, vt_g = svd(green)
    l = [1, 5, 10, 20, 40, 200]
    for k in l:
        red_k = np.zeros((u_r.shape[0], vt_r.shape[0]))
        blue_k = np.zeros((u_b.shape[0], vt_b.shape[0]))
        green_k = np.zeros((u_g.shape[0], vt_g.shape[0]))
        error_temp = 0

        for i in range(k):
            red_k[i][i] = sigma_r[i]
            blue_k[i][i] = sigma_b[i]
            green_k[i][i] = sigma_g[i]
            error_temp += (sigma_r[i] ** 2)
        print((sum(sigma_r ** 2) - error_temp) / sum(sigma_r ** 2))
        red_k = np.dot(u_r, (np.dot(red_k, vt_r)))
        blue_k = np.dot(u_b, (np.dot(blue_k, vt_b)))
        green_k = np.dot(u_g, (np.dot(green_k, vt_g)))
        new_image = np.zeros((pix.shape[0], pix.shape[1], 3))
        new_image[:, :, 0] = red_k
        new_image[:, :, 1] = blue_k
        new_image[:, :, 2] = green_k
        new_image = Image.fromarray(new_image.astype('uint8'))
        new_image.save("t_%d.png" % (k))
        new_image.show()
