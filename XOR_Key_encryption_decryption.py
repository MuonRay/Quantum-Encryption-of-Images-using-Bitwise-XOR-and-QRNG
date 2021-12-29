# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:19:24 2021

@author: cosmi

XOR Encrypt using a Key
"""

import cv2
import numpy as np
from numpy import random
 
random.seed(12345)    #random number seed, this can be a "locked" seed - for frequency analysis testing or we can use a TRNG to make fully random. If no seed is used, the PRNG uses the systems hardware as an entropy source, using the systems clock for example.


demo = cv2.imread("OrionNebula.png",0)
r, c = demo.shape


key = random.randint(0, 256, size=[r, c], dtype=np.uint8)

 
 
encryption = cv2.bitwise_xor(demo, key) # encryption
decryption = cv2.bitwise_xor(encryption, key) # decryption
 
cv2.imshow("encryption", encryption) # Display ciphertext image
cv2.imshow("decryption", decryption) # Display the decrypted image
 
cv2.waitKey()
cv2.destroyAllWindows()