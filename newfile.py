from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

from houghTransform import houghTransform


def apply_hough_transform(image_path: str=""):
    image = np.array(Image.open(image_path))
    lines = houghTransform(image, 1, 360)

    p = np.unravel_index(lines.argmax(), lines.shape)
    
    max_distance = 2 * np.sqrt(pow(image.shape[0], 2) + pow(image.shape[1], 2))

    ro = p[0] - (max_distance / 2)
    theta = p[1] * (np.pi / 180)

    a = np.cos(theta)
    b = np.sin(theta)
    x = a * ro
    y = b * ro

    pt1 = (int(x + 1000*(-b)), int(y + 1000*(a)))
    pt2 = (int(x - 1000*(-b)), int(y - 1000*(a)))
    
    fig, axs = plt.subplots(2)

    axs[0].matshow(lines)
    axs[0].scatter(p[1], p[0], facecolors="none", edgecolors="r")

    axs[1].plot([pt1[0], pt2[0]], [pt1[1], pt2[1]])
    axs[1].imshow(image)
    plt.show()

apply_hough_transform(image_path="Untitled2")