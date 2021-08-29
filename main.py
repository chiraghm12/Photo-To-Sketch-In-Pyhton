# Photo-To-Sketch-In-Pyhton
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("123.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)

greyimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invertimg=cv2.bitwise_not(greyimg)

blurimg=cv2.GaussianBlur(invertimg, (111,111),0)
invblurimg=cv2.bitwise_not(blurimg)
sketchimg=cv2.divide(greyimg,invblurimg, scale=256.0)
cv2.imwrite("sketch.png", sketchimg)

cv2.imshow("sketch image",sketchimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
