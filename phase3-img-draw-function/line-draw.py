import cv2
image=cv2.imread("phase3-img-draw-function\pylogo.png")
if image is not None:
    pt1=(50,50)
    pt2=(200,200)
    color=(0,255,0)
    thickness=5
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line Drawn Image",image)
    cv2.imwrite("lined_image.jpg",image)
    cv2.imwrite("lined_image.png",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else :
    print("Image not loaded; cannot draw line.")  