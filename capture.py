import cv2
import os

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#cv2.namedWindow("Capture")

while True:
    ret, frame = cam.read()
    cv2.imshow("Capture", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        #print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "test.jpg"
        cv2.imwrite(img_name, frame)
        #print("{} written!".format(img_name))
        break

cam.release()

cv2.destroyAllWindows()
os.system("python page1.py")
