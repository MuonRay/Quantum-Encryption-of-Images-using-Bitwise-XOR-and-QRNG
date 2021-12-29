# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:11:29 2021

@author: cosmi

XOR encrypt+decrypt using pseudo-random number

"""

import cv2
import numpy as np

img = cv2.imread("OrionNebula.png", 0)
r, c = img.shape
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
encryption = cv2.bitwise_xor(img, key)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imshow("encrypted image", encryption)
cv2.imshow("decrypted image", decryption )
cv2.waitKey()
cv2.destroyAllWindows()