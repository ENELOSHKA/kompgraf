import os, math
import numpy as np
from PIL import Image, ImageDraw,ImageEnhance,ImageChops
import random
import cv2
import matplotlib.pyplot as plt



os.chdir("E:\Windows (вместо С)\комп граф\лаб2")



X = Image.open("оригинал л2.bmp")
X1 = Image.open("вариант1 л2.bmp")
print(X.size[0],X.size[1],'\n',X1.size[0],X1.size[1])
iar = np.array(X).astype('float')/255
iar1 = np.array(X1).astype('float')/255
print (iar.shape)
for k in range(1944):
    ki = k * 1/1944
    print(ki)
    iar[k,:]=iar[k,:]+ki
s = Image.fromarray(iar)
print(ki)
iars = iar-iar1
print(iars)
im = Image.fromarray(iars*255)
print(np.mean(np.abs(iars)))
im.show()
ss =Image.fromarray(iar*255)
ss.show()



