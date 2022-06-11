import cv2 as cv
from PIL import ImageGrab


def eye_detection():
    cap = cv.VideoCapture(0)
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    first_read = True
    while True:
        ret, image = cap.read()

        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
                roi_gray = gray[y:y+w, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
                for (ex, ey, ew, eh) in eyes:
                    cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
                    if len(eyes) >= 2:
                        cv.putText(image, "Eye's detected, press s to check blink", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    else:
                        cv.putText(image, "Blink Detected.....!!!!", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv.imshow('image', image)
                        cv.waitKey(1)
                        #print("Screenshot Taken")
                        snapshot = ImageGrab.grab()
                        save_path = "C:/Users/berna/Desktop/pdfimages/screenshot.png"
                        snapshot.save(save_path)
        else:
            cv.putText(image, "No Face Detected.", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv.imshow('image', image)
        a = cv.waitKey(1)
        # press q to Quit and S to start
        # ord(ch) returns the ascii of ch
        if a == ord('q'):
            break
        elif a == ord('s'):
            first_read = False
    # release the web-cam
    cap.release()
    # close the window
    cv.destroyAllWindows()
