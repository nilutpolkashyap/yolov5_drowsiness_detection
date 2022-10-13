import cv2
  
vid = cv2.VideoCapture(2)

count = 0
print(count)
  
while(vid.isOpened()):
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    if count == 50:
        break

    if key == ord("s"):
        # cv2.imwrite("/images/frame_%d.jpg" % count, frame)
        cv2.imwrite("awake_%d.jpg" % count, frame)
        count += 1
        print("Count : ", count)
  
vid.release()
cv2.destroyAllWindows()