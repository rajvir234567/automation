import cv2

def takeSnapshot():
    video_object = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = video_object.read()
        cv2.imwrite("pic1.png", frame)
        result = False

    video_object.release()
    cv2.destroyAllWindows()

takeSnapshot()