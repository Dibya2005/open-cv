import cv2
img=cv2.imread('phase1\IM.jpg')
#img shape test
if img is not None:
    h,w,c=img.shape
    print(f"Image dimensions - Height: {h}, Width: {w}, Channels: {c}")
else:
    print("Image not loaded.")