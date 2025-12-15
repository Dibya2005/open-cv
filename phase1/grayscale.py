import cv2
img=cv2.imread('phase1\IM.jpg')
#IMG LOADING TEST
if img is not None:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
    print("Image converted to grayscale and displayed successfully.")Z
else:
    print("Image not loaded; cannot convert to grayscale.")