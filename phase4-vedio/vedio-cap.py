import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()#ret true or false frame image
    if not ret:
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'): #wait for 'q' key to stop 
        break
cap.release()
cv2.destroyAllWindows()
    
  