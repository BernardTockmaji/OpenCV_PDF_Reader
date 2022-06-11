import cv2 as cv
import numpy as np
import glob


def change_color(path, color=(0, 0, 1)):
    images = [cv.imread(file) for file in glob.glob(path + "/*.png")]
    n = 0
    for i in images:
        n = n+1
        image = i
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 100, 200)
        rgb = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        rgb *= np.array(color, np.uint8)
        out = np.bitwise_or(image, rgb)
        cv.imwrite("C:/Users/berna/Desktop/pdfimages/changeText/" + str(n) + ".jpg", out)
        cv.waitKey(0)


def change_background(path):
    images = [cv.imread(file) for file in glob.glob(path + "/*.png")]
    n = 0
    for i in images:
        n = n+1
        image = i
        image[np.where((image == [255, 255, 255]).all(axis=2))] = [205, 161, 152]
        cv.imwrite("C:/Users/berna/Desktop/pdfimages/changebackground/background" + str(n) + ".jpg", image)

    cv.waitKey(0)
