import cv2

# to read an image we have a function call imread('filename',flag(1,-1,0))
# 1--> coloured image
# 0--> gray imag
# -1 --> shows the img as it is

# img = cv2.imread('lena.jpg',-1)
# print(img)
# now to show the image that we have read 
# we have a function imshow('nameofwindow',varibalename)

# cv2.imshow('image',img)
# cv2.waitKey(5000) #5000 here is the miliseconds
# cv2.destroyAllWindows()

img = cv2.imread('lena.jpg',0)
cv2.imshow('image',img)

k=cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()
else:
    print("you fool")    

