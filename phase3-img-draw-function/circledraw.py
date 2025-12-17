import cv2
image=cv2.imread("phase3-img-draw-function\pylogo.png")
if image is not None:
    pt1=(250,250)
    radius=75  # radius
    color=(0,255,0)
    thickness=5
    cv2.circle(image,pt1,radius,color,thickness)
    cv2.imshow("Circle Drawn Image",image)
    cv2.imwrite("circle_image.jpg",image)
    cv2.imwrite("circle_image.png",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else :
    print("Image not loaded; cannot draw line.")  