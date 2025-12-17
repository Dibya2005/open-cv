import cv2  
image=cv2.imread("phase2_img_rewsizing_and_shaping\IM.jpg")
if image is not None:
    flipped_image=cv2.flip(image,1)
    # flip code 1 for horizontal, 0 for vertical, -1 for both
    cv2.imshow("Flipped Image",flipped_image)
    cv2.imwrite("flippedimg.jpg",flipped_image)
    cv2.imwrite("flippedimg.jpg",flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded; cannot flip.")