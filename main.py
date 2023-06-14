import tkinter
import customtkinter
import numpy as np
import cv2 as cv
import sys



img = cv.imread(filename="huh.jpg")



if img is None:
    sys.exit("could not read the file.")

img_clone = img.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for row in img:
    for pixel in row:
        if pixel > 126:
            print('&',end="")
            continue
        print('.',end="")
    print("\n")
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

