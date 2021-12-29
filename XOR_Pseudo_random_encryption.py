# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:08:30 2021

@author: cosmi

XOR Encrypt using pseudo-random number
"""

import cv2
import numpy as np

img = cv2.imread("OrionNebula.png", 0)
r, c = img.shape
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
encryption = cv2.bitwise_xor(img, key)

cv2.imshow("Encrypted Image", encryption)
cv2.waitKey()
cv2.destroyAllWindows()