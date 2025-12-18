import cv2
cam=cv2.VideoCapture(0)
frame_width=int(cv2.CAP_PROP_FRAME_WIDTH)
frame_height=int(cv2.CAP_PROP_FRAME_HEIGHT)
fourcc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter('output.avi',fourcc,20.0,(frame_width,frame_height))
while True:
    ret,frame=cam.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
out.release()
cv2.destroyAllWindows()