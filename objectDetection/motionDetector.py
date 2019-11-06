import cv2

# captura de video desde webcam
video = cv2.VideoCapture(0)  # 0 indica ls web cam principal del laptop

while True:
    check, frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("capture",gray)

    key = cv2.waitKey(1)
    print(gray)

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows