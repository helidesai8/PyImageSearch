import numpy as np
import cv2


def translate(image, x, y):
    m = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, m, (image.shape[1], image.shape[0]))
    # return the translated image
    return shifted


def rotate(image, angle, centre=None, scale=1.0):
    (h, w) = image.shape[:2]
    if centre is None:
        centre = (w / 2, h / 2)

    m = cv2.getRotationMatrix2D(centre, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))

    return rotated


def resize(image, height, width, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (w * r, height)

    elif height is None:
        r = width / float(w)
        dim = (width, h * r)

    else:
        dim = (width, height)

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized
