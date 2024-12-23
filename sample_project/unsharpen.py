#!/usr/bin/python
"""Soften an image."""
# -*- coding: utf-8 -*-
# -----------------------------------------
# author      : Kennedy Rotich
# mail        : kennrottich@gmail.com
# date        : 27.11.2024
# -----------------------------------------

import cv2


def unsharpen_mask(image):
    """Soften an input image.

    Parameters
    ----------
    image : numpy ndarray
        The input image.

    Returns
    -------
    numpy ndarray
        The soften image.

    """
    # perform GaussianBlur filter to use it in unsharpening mask
    gaussian_3 = cv2.GaussianBlur(image, (9, 9), 10.0)
    # calculates the weighted sum of two arrays (source image and GaussianBlur
    # filter) to perform unsharpening mask
    unsharp_image = cv2.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)
    # return unsharpened image
    return unsharp_image
