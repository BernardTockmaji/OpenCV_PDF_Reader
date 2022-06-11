import cv2 as cv
import glob
from fpdf import FPDF


def eye_comfort2(alpha, r, g, b, path):
    pdf_img = cv.imread(path)
    #pdf_img = cv.resize(pdf_img, (612, 792))
    overlay = pdf_img.copy()
    cv.rectangle(pdf_img, (0, 0), (pdf_img.shape[1], pdf_img.shape[0]), (b, g, r), -1)
    cv.addWeighted(overlay, alpha, pdf_img, 1 - alpha, 0, pdf_img)
    cv.imwrite("C:/Users/berna/Desktop/pdfimages/*.png", pdf_img)
    # cv.imshow('Resized Window', pdf_img)
    cv.waitKey(0)


def eye_comfort(alpha, r, g, b, path):
    images = [cv.imread(file) for file in glob.glob(path + "/*.png")]
    n = 0
    for i in images:
        n = n+1
        pdf_img = i
        overlay = pdf_img.copy()
        cv.rectangle(pdf_img, (0, 0), (pdf_img.shape[1], pdf_img.shape[0]), (b, g, r), -1)
        cv.addWeighted(overlay, alpha, pdf_img, 1 - alpha, 0, pdf_img)
        cv.imwrite("C:/Users/berna/Desktop/pdfimages/comfortmode/comfort" + str(n) + ".png", pdf_img)
        cv.waitKey(0)
