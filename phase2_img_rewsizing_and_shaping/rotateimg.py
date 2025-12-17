import cv2  
image=cv2.imread("phase2_img_rewsizing_and_shaping\IM.jpg")
if image is not None:
    (h,w)=image.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,45,1.0)
    roteted_image=cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Rotated Image",roteted_image)
    cv2.imwrite("rotatedimg.jpg",roteted_image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded; cannot rotate.")
