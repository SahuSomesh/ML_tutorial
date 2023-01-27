import cv2

img = cv2.imread('men1.png',1)

img2 = cv2.imread('opencv-logo.png')

print(img.shape) # returns a tuple of no of rows, column, and channels
print(img.size) # returns total no of pixels is accessed
print(img.dtype) # returns image datatype is obtained

b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

# how to add 2 images

cv2.add()


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ROI -> Region of Interest

