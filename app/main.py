from imageTools.imgHandler import imgToAsc
from imageTools.vidHandler import vidToAsc
import os 

# main app

def main():
    # print(os.getcwd())
    print("Welcome! Please choose what would you like to do by inputing a number")
    print("1. Convert an image into ascii art")
    print("2. Convert a video into ascii art")
    choice = input("")

    match choice:
        case "1":
            imgToAsc()
        case "2":
            vidToAsc()

if __name__ == "__main__":
    main()


    
# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("huh.jpg",img)
    
