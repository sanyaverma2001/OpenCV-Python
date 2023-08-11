import cv2

cap1 = cv2.VideoCapture(0)

while(True):
    ret,frame = cap1.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()