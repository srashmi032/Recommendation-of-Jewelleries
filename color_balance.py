from __future__ import (
    division, absolute_import, print_function, unicode_literals)

import cv2 as cv
import numpy as np

#Adjust pixel values 
def show(final):
    print('display')
    cv.imshow('Result', final)
    cv.waitKey(0)
    cv.destroyAllWindows()


img = cv.imread('c4.jpg')
final = cv.cvtColor(img, cv.COLOR_BGR2LAB)

avg_a = np.average(final[:, :, 1])
avg_b = np.average(final[:, :, 2])

for x in range(final.shape[0]):
    for y in range(final.shape[1]):
        l, a, b = final[x, y, :]
       
        l *= 100 / 255.0
        final[x, y, 1] = a - ((avg_a - 128) * (l / 100.0) * 0.98)
        final[x, y, 2] = b - ((avg_b - 128) * (l / 100.0) * 0.98)

final = cv.cvtColor(final, cv.COLOR_LAB2BGR)


show(final)
cv.imwrite('resultw21.jpg', final)