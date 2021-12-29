# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:35:14 2021

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

# Load original image
demo = cv2.imread("OrionNebula.png")
r, c, t = demo.shape

# Display original image
cv2.imshow("Original image", demo)

# Create random key
key = cv2.imread("pseudorandomkey.png")

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
