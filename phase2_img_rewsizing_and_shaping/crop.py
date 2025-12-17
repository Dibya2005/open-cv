import cv2
image=cv2.imread("phase2_img_rewsizing_and_shaping\IM.jpg")
if image is not None:
  croped_image=image[100:400,50:400]
  cv2.imshow("Cropped Image",croped_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("Image not loaded; cannot crop.")

