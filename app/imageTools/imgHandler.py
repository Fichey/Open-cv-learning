import sys
import os
import cv2 as cv
from imageTools.asciiConverter import convert


def imgToAsc():
    file_name = input("which file would you like to convert? :")

    img = cv.imread(filename=file_name)
    if img is None:
        sys.exit("could not read the file.")
        
    print("***INPUT 0 FOR ORIGINAL IMAGE SIZE***")
    new_width = int(input("input the desired width of an image: "))
    new_height = int(input("input the desired height of the image: "))

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    if(new_height != 0 and new_width != 0):
        img = cv.resize(img, (new_width, new_height), interpolation = cv.INTER_CUBIC)
    os.system('cls')
    os.system('cls')
    os.system('cls')
    convert(img)