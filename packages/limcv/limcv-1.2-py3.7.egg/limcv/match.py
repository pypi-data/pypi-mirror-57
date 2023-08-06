#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from threading import Thread
import imutils
import cv2


def get_perfect_scale(image, template):
    # load the image image, convert it to grayscale, and detect edges
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)

    # load the image, convert it to grayscale, and initialize the
    # bookkeeping variable to keep track of the matched region
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    a = np.linspace(0.5, 0.75, 15)[::-1]
    b = np.linspace(0.75, 1.0, 15)[::-1]
    c = np.linspace(1.0, 1.25, 8)
    d = np.linspace(1.25, 1.5, 8)
    e = np.linspace(1.5, 1.75, 8)
    f = np.linspace(1.75, 2.0, 8)

    max_a = []
    max_b = []
    max_c = []
    max_d = []
    max_e = []
    max_f = []

    threads = []
    threads.append(Thread(target=calculate_scale, args=(gray, template, a, max_a, 'a')))
    threads.append(Thread(target=calculate_scale, args=(gray, template, b, max_b, 'b')))
    threads.append(Thread(target=calculate_scale, args=(gray, template, c, max_c, 'c')))
    threads.append(Thread(target=calculate_scale, args=(gray, template, d, max_d, 'd')))
    threads.append(Thread(target=calculate_scale, args=(gray, template, e, max_e, 'e')))
    threads.append(Thread(target=calculate_scale, args=(gray, template, f, max_f, 'f')))

    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join(2)
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # print(max_a, len(max_a))
    # print(max_b, len(max_b))
    # print(max_c, len(max_c))
    # print(max_d, len(max_d))
    # print(max_e, len(max_e))
    # print(max_f, len(max_f))

    if len(max_a) == 2:
        max_t = max_a[0]
        perfect_scale = max_a[1]

    if len(max_b) == 2 and max_t < max_b[0]:
        max_t = max_b[0]
        perfect_scale = max_b[1]

    if len(max_c) == 2 and max_t < max_c[0]:
        max_t = max_c[0]
        perfect_scale = max_c[1]
    if len(max_d) == 2 and max_t < max_d[0]:
        max_t = max_d[0]
        perfect_scale = max_d[1]
    if len(max_e) == 2 and max_t < max_e[0]:
        max_t = max_e[0]
        perfect_scale = max_e[1]
    if len(max_f) == 2 and max_t < max_f[0]:
        max_t = max_f[0]
        perfect_scale = max_f[1]

    return perfect_scale


def calculate_scale(gray, template, scales, max, name):
    (tH, tW) = template.shape[:2]
    found = None
    perfect_scale = 1.0
    max_value = 0

    # loop over the scales of the image
    for scale in scales:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            print("break")
            break

        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        # check to see if the iteration should be visualized
        # if args.get("visualize", False):
        # 	# draw a bounding box around the detected region

        # if we have found a new maximum correlation value, then ipdate
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
            if maxVal > max_value:
                max_value = maxVal
                perfect_scale = scale
    max.append(max_value)
    max.append(perfect_scale)

# unpack the bookkeeping varaible and compute the (x, y) coordinates
# of the bounding box based on the resized ratio
