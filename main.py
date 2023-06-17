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





img = cv.imread(filename="huh.jpg")

if img is None:
    sys.exit("could not read the file.")


# copying and converting to gray
img_clone = img.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

test = np.arange(36)
test = test.reshape(6,6)
print(test[0:2][0:2])

print(img.dtype)

img = compress(img,2)

print(img.shape)
# print(img_clone.size)

# for row in img:
#     for pixel in row:
#         if pixel > 126:
#             print('&',end="")
#             continue
#         print('.',end="")
#     print("\n")
    
    
cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("huh.jpg",img)
    

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

