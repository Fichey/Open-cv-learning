import os
import cv2 as cv
from imageTools.asciiConverter import convert

def vidToAsc():
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