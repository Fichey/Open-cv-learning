import tkinter
import customtkinter
import math
import numpy as np
import cv2 as cv
import sys

#getting the average value of the sqare if pixels

def average(cutout: np.uint8):
    q = 1
    cutout = cutout.reshape(len(cutout)**2)
    a = int(sum(cutout) / len(cutout))
    return a

#apparently the compress function is built in opencv but I realized this after writing my own so might as well keep it
    
#reducing the amount of pixels in an image

def compress(img: np.uint8, size_of_sqare: int)-> np.uint8:
    if size_of_sqare < 2:
        return img
    
    rows, cols = img.shape
    rows = rows - rows%size_of_sqare #clipping right and bottom for a clean compression
    cols = cols - cols%size_of_sqare
    print(rows, cols)
    
    print(img)
    
    if len(img.shape) == 2:
        compressed_img = np.array([[
                    average(img[y:y+size_of_sqare,x:x+size_of_sqare])
                for x in range(0,cols,size_of_sqare)] 
            for y in range(0,rows,size_of_sqare)]
            ).astype(np.uint8)
        return compressed_img


# converting img array to ascii characters and printing them

def convert(img: np.uint8):
    characters = " .:-=+*#%@"

    for row in img:
        for pixel in row:
            print(characters[pixel//26],end="")
            print(characters[pixel//26],end="")
        print()
    

# main app
    
file_name = input("which file would you like to convert? :")
compression_level = input("what converion level would you like to use? :")


img = cv.imread(filename=file_name)
if img is None:
    sys.exit("could not read the file.")


img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img = compress(img,3)

convert(img)

    
# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("huh.jpg",img)
    
