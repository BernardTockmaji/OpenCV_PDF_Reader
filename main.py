import cv2 as cv
import eye_detection as eye
import eye_comfort_mode as comfort
import pdf_files as pdf
import text_coloring as txt
import mark_page as mark
from tkinter import *
from tkinter.filedialog import askopenfilename


# choosing pdf file
Tk().withdraw()
path = askopenfilename()
pdf.pdf2_to_image(path)

choice = print("enter the function you wish to apply on your pdf"'\n' '1- Eye comfort mode' '\n''2- Change text color & background''\n''3- Mark page''\n'
               '4- Highlight Page' '\n' '5- Eye detection')
i = 0

for i in range(5):
    i = i+1
    choice = input("\n" 'would you like to modify?')
    if choice == '1':
        comfort.eye_comfort(0.8, 223, 200, 130, 'C:/Users/berna/Desktop/pdfimages')
        #pdf.convert_comfort_mode()
        cv.waitKey(0)

    if choice == '2':
        txt.change_color('C:/Users/berna/Desktop/pdfimages')
        txt.change_background('C:/Users/berna/Desktop/pdfimages')
        cv.waitKey(0)

    if choice == '3':
        page_number = input("Enter your page number: ")
        mark.draw('C:/Users/berna/Desktop/pdfimages/page-' + str(page_number) + '.png')
        cv.waitKey(0)

    if choice == '4':
        page_number = input("Enter your page number: ")
        mark.highlight('C:/Users/berna/Desktop/pdfimages/page-' + str(page_number) + '.png')
        cv.waitKey(0)

    if choice == '5':
        eye.eye_detection()
        cv.waitKey(0)

cv.waitKey(0)
