import numpy as np
from math import cos, sin, pi
from PIL import Image

image = "edged.jpg"
im = Image.open(image)
imageArr = np.array(im)

height = len(imageArr)
width  = len(imageArr[0])

def build_hough_space_fom_image(img, shape = (100, 300), val = 1):
    hough_space = np.zeros(shape)
    print(hough_space)
    for i, row in enumerate(img):
        for j, pixel in enumerate(row):   
            if pixel != val : continue
        hough_space = add_to_hough_space_polar((i,j), hough_space)
    return hough_space
def add_to_hough_space_polar(p, feature_space):
    space = np.linspace(0, pi, len(feature_space))
    d_max = len(feature_space[0]) / 2
    d_max = int(d_max)
    for i in range(len(space)):
        theta = space[i]
        d = int(p[0] * sin(theta) + p[1] * cos(theta)) + d_max
        if (d >= d_max * 2) : continue
        print("adding 1")
        feature_space[i, d] += 1
    return feature_space


print(build_hough_space_fom_image(image))