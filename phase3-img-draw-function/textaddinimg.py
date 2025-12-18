import cv2
image=cv2.imread("phase3-img-draw-function\pylogo.png")
if image is not None:
   cv2.putText(image,"good night",(100,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
   cv2.imshow("Text Added Image",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
else :
    print("Image not loaded; cannot draw line.")  