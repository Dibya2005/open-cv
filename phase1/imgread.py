import cv2
img=cv2.imread('phase1\IM.jpg')
#IMG LOADING TEST
# if img is None:
#     print("Image not found or unable to load.")
# else:
#     print("Image loaded successfully.")
#     print(f"Image dimensions: {img.shape}")
# #img show test
# if img is not None:
#  cv2.imshow('Image',img)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
# else:
#   print("failed")
#img saving test
if img is not None:
 success = cv2.imwrite('phase1\\IM_copy.jpg', img)
 if success:
    print("Image saved successfully.")
 else:
    print("Failed to save image.")
else:
    print("Image not loaded; cannot save.")