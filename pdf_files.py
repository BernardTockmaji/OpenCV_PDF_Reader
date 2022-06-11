import fitz
from tkinter import *
import glob
import os
from os import listdir
from os.path import isfile, join


def pdf2_to_image(path):
    # To get better resolution
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
    all_files = glob.glob(path)

    for filename in all_files:
        doc = fitz.open(filename)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap(matrix=mat)  # render page to an image
            pix.save("C:/Users/berna/Desktop/pdfimages/page-%i.png" % page.number)  # store image as a PNG


def convert_comfort_mode():
    comfort_path = "C:/Users/berna/Desktop/pdfimages/comfortmode/comfort/*.jpg" # path to your Image directory
    for each_file in listdir(comfort_path):
        if isfile(join(comfort_path, each_file)):
            image_path = os.path.join(comfort_path, each_file)
            pdf_path = os.path.join(comfort_path, each_file.rsplit('.', 1)[0]+'.pdf')
            img = Image(image_path)
            img.write(pdf_path)
