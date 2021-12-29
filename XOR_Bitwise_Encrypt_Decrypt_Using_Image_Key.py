# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:28:18 2021

@author: cosmi

XOR encrypt + decrypt using an image as Key

"""



import cv2
 

demo = cv2.imread("OrionNebula.png",0)
r, c = demo.shape


key = cv2.imread("pseudorandomkey.png",0)


 
encryption = cv2.bitwise_xor(demo, key) # encryption
decryption = cv2.bitwise_xor(encryption, key) # decryption
 
cv2.imshow("encryption", encryption) # Display ciphertext image
cv2.imshow("decryption", decryption) # Display the decrypted image
 
cv2.waitKey()
cv2.destroyAllWindows()