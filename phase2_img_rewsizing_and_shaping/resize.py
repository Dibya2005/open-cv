import cv2
image=cv2.imread("phase2_img_rewsizing_and_shaping\IM.jpg")
cv2.imshow("IM.jpg", image)
if image is not None:
    resized_image=cv2.resize(image,(500,500))
    cv2.imshow("Resized Image",resized_image)
    cv2.imwrite("resizedimg.jpg",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image not loaded; cannot resize.")