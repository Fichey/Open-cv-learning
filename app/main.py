from imageTools.imgHandler import imgToAsc
from imageTools.vidHandler import vidToAsc
import os 
import sys
from UI.pyqttest import MyWidget
from PyQt6 import QtCore, QtWidgets, QtGui


# main app

def main():
    # print(os.getcwd())
    print(QtGui.QFontMetrics(QtGui.QFont('Courier', 10)).lineSpacing)
    print("Welcome! Please choose what would you like to do by inputing a number")
    print("1. Convert an image into ascii art")
    print("2. Convert a video into ascii art")
    choice = input("")

    app = QtWidgets.QApplication([])
    widget = MyWidget()

    match choice:
        case "1":
            widget.text.setText(imgToAsc())
            
        case "2":
            vidToAsc()
    
    
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


    
# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("huh.jpg",img)
    
