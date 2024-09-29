import numpy as np

def convert(img: np.uint8):
    characters = " _.,-=+:;cba!?0123456789$W#@Ñ"
    divisiveNumber = 256/ len(characters)
    resultFrame = ""
    
    for row in img:
        for pixel in row:
            resultFrame += characters[int(pixel//divisiveNumber)] * 3
        resultFrame += "\n"
    return resultFrame

#apparently the compress function is built in opencv but I realized this after writing my own so might as well keep it
    
    
# getting the average value of the sqare if pixels

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
