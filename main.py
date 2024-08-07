import tkinter
import customtkinter
import math
import numpy as np
import cv2 as cv
import sys
import os
from pynput import keyboard





#apparently the compress function is built in opencv but I realized this after writing my own so might as well keep it
    
    
#getting the average value of the sqare if pixels

# def average(cutout: np.uint8):
#     q = 1
#     cutout = cutout.reshape(len(cutout)**2)
#     a = int(sum(cutout) / len(cutout))
#     return a
    
    
# def compress(img: np.uint8, size_of_sqare: int)-> np.uint8:
#     if size_of_sqare < 2:
#         return img
    
#     rows, cols = img.shape
#     rows = rows - rows%size_of_sqare #clipping right and bottom for a clean compression
#     cols = cols - cols%size_of_sqare
#     print(rows, cols)
    
#     print(img)
    
#     if len(img.shape) == 2:
#         compressed_img = np.array([[
#                     average(img[y:y+size_of_sqare,x:x+size_of_sqare])
#                 for x in range(0,cols,size_of_sqare)] 
#             for y in range(0,rows,size_of_sqare)]
#             ).astype(np.uint8)
#         return compressed_img


# converting img array to ascii characters and printing them
print(len(" .,:I>?]1/trzXQOmhoWB@$"))
def convert(img: np.uint8):
    characters = " .,:I>?]1/trzXQOmwqhB@$"

    for row in img:
        for pixel in row:
            print(characters[int(pixel//11.1)] * 3,end="")
        print()
    

def img_to_asc():
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
    convert(img)



def vid_to_asc():
    vid_name = input("Input the name of the video to convert: ")
    cap = cv.VideoCapture(vid_name)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame.shape[0] <= frame.shape[1]:
            divider = frame.shape[0] / 30
        else:
            divider = frame.shape[1] / 30
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.resize(frame, (int(int(frame.shape[1])/divider), int(int(frame.shape[0])/divider)), interpolation = cv.INTER_CUBIC)
    
        #cv.imshow(vid_name,frame)
        
        
        os.system('cls')
        convert(frame)
        # print(frame.size)
        # n_frame = np.zeros(frame.size)
        # print(n_frame)
        # n_frame = n_frame.reshape(frame.shape[0], frame.shape[1])
        # for i in range(frame.shape[0]-1):
        #     for j in range(frame.shape[1]-1):
        #         if abs(frame[i][j] - frame[i+1][j]) > 126 or abs(frame[i][j] - frame[i][j+1]) > 126:
        #             n_frame[i][j] = 255
        # print(frame.shape)
        # cv.imshow(vid_name + "(grayscale)",n_frame)
        
            
    os.system('cls')
    cap.release()
    cv.destroyAllWindows()

    


# main app

print("Welcome! Please choose what would you like to do by inputing a number")
print("1. Convert an image into ascii art")
print("2. Convert a video into ascii art")
choice = input("")

match choice:
    case "1":
        img_to_asc()
    case "2":
        vid_to_asc()

    


    
# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("huh.jpg",img)
    
