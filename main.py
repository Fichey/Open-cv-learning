import tkinter
import customtkinter
import math
import numpy as np
import cv2 as cv
import sys

#reducing the amount of pixels in an image

def average(cutout: np.uint8):
    cutout = cutout.reshape(len(cutout)**2)
    a = int(sum(cutout) / len(cutout))
    return a


# test = np.arange(25)
# test = test.reshape(5,5)

# print(average(test))
        
    

def compress(img: np.uint8, size_of_sqare: int)-> np.uint8:
    if size_of_sqare < 2:
        return img
    
    rows, cols = img.shape
    rows = rows - rows%size_of_sqare #clipping right and bottom for a clean compression
    cols = cols - cols%size_of_sqare
    print(rows, cols)
    
    
    # if len(img.shape) == 2:

    
    
    # test = np.arange(25)
    # test = test.reshape(5,5)
    # print(test)
    
# [[ 0  1  2  3  4] -- test
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
    
    # a = np.array([[test[y, x] for x in range(0, test.shape[1])] for y in range(0, test.shape[0])])
    # print(a)
    
# [[ 0  1  2  3  4] -- a
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
    

            



img = cv.imread(filename="huh.jpg")

if img is None:
    sys.exit("could not read the file.")

print(img.dtype)

# copying and converting to gray
img_clone = img.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

compress(img,5)

# print(img.shape)
# print(img_clone.size)

# for row in img:
#     for pixel in row:
#         if pixel > 126:
#             print('&',end="")
#             continue
#         print('.',end="")
#     print("\n")
    
    
# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("huh.jpg",img)
    

# customtkinter.set_appearance_mode("system")

# app = customtkinter.CTk()

# def button_callback():
#     print('button pressed')

# app.title('my app')
# app.geometry("600x400")
# app.grid_columnconfigure(0, weight=1)

# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

# app.mainloop()

