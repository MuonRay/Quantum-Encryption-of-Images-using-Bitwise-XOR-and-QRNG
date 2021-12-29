# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:16:06 2021

@author: cosmi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:11:11 2021

@author: cosmi

Full Color XOR encryption and decryption
"""

import cv2
import numpy as np
from numpy import random

random.seed(12345)    #random number seed, this can be a "locked" seed - for frequency analysis testing or we can use a TRNG to make fully random. If no seed is used, the PRNG uses the systems hardware as an entropy source, using the systems clock for example.

# Load original image to make the key the same shape
demo = cv2.imread("OrionNebula.png")
r, c, t = demo.shape

# Display original image
cv2.imshow("Original image", demo)

# Create random key image in the same shape
key = random.randint(256, size = (r, c, t))

# Encryption
# Iterate over the image
encryption_key_image = np.zeros((r, c, t), np.uint8)
for row in range(r):
    for column in range(c):
        for depth in range(t):
            encryption_key_image[row, column, depth] = key[row, column, depth]   # this will creat the key as a separate image file
            
cv2.imshow("Encryption Key image", encryption_key_image)

cv2.imwrite("pseudorandomkey.png", encryption_key_image)

cv2.waitKey()
cv2.destroyAllWindows()