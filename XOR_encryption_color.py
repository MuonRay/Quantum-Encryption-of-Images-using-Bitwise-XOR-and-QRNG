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

# Load original image
demo = cv2.imread("OrionNebula.png")
r, c, t = demo.shape

# Display original image
cv2.imshow("Original image", demo)

# Create random key
key = random.randint(256, size = (r, c, t))

# Encryption
# Iterate over the image
encrypted_image = np.zeros((r, c, t), np.uint8)
for row in range(r):
    for column in range(c):
        for depth in range(t):
            encrypted_image[row, column, depth] = demo[row, column, depth] ^ key[row, column, depth]   # A^B = C, A XOR B = C
            
cv2.imshow("Encrypted image", encrypted_image)

# Decryption
# Iterate over the encrypted image
decrypted_image = np.zeros((r, c, t), np.uint8)
for row in range(r):
    for column in range(c):
        for depth in range(t):
            decrypted_image[row, column, depth] = encrypted_image[row, column, depth] ^ key[row, column, depth] # C ^ B = A, C XOR B = A
            
cv2.imshow("Decrypted Image", decrypted_image)

cv2.waitKey()
cv2.destroyAllWindows()
