binary1 = '1101'
binary2 = '1010'

# Convert binary strings to integers, concatenate, and then convert back to binary
concatenated_binary = bin(int(binary1, 2) << len(binary2) | int(binary2, 2))[2:]

print("Concatenated Binary:", concatenated_binary)

print(type(concatenated_binary))



exit()

import cv2
import numpy as np

img_list = [
    "boards/board_1.png",
    "boards/board_2.png",
    "boards/board_3.png",
    "boards/board_4.png",
    "boards/board_5.png",
]

# combine images horizontally
images = []
for img in img_list:
    images.append(cv2.imread(img))

# combine images horizontally
result = np.hstack((images[0], images[1]))
for i in range(2, len(images)):
    result = np.hstack((result, images[i]))

# display images
cv2.imshow("result", result)
cv2.waitKey(0)

# # Read your images
# image1 = cv2.imread('boards/board_1.png')
# image2 = cv2.imread('boards/board_2.png')
# image3 = cv2.imread('boards/board_3.png')

# # Make sure all images have the same height
# height = max(image1.shape[0], image2.shape[0], image3.shape[0])

# # Resize images to have the same height
# image1 = cv2.resize(image1, (int(image1.shape[1] * height / image1.shape[0]), height))
# image2 = cv2.resize(image2, (int(image2.shape[1] * height / image2.shape[0]), height))
# image3 = cv2.resize(image3, (int(image3.shape[1] * height / image3.shape[0]), height))

# # Combine images horizontally
# result = np.hstack((image1, image2, image3))

# # Display the result
# cv2.imshow('Horizontal Concatenation', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

exit()

cur_width_part = 0
cur_height_part = 0

width = 400
height = 400

width_part_total = 8
height_part_total = 8

part_width = width // width_part_total
part_height = height // height_part_total

curchan = 0
curwidth = 0
curheight = 0

for i in range (100000):
    if cur_width_part == width_part_total-1:
        cur_width_part = 0
        if cur_height_part == height_part_total-1:
            cur_height_part = 0
            if curchan == 2:
                curchan = 0
                if curwidth == part_width-1:
                    curwidth = 0
                    if curheight == part_height-1:
                        curheight = 0
                    else:
                        curheight +=1
                else:
                    curwidth +=1
            else:
                curchan +=1
        else:
            cur_height_part += 1
    else:
        cur_width_part += 1

    real_width = cur_width_part * part_width + curwidth
    real_height = cur_height_part * part_height + curheight


    print("curwidth:", curwidth)
    print("curheight:", curheight)

    print("real_width:", real_width)
    print("real_height:", real_height)
    
    print("curchan:", curchan)
    print("cur_width_part:", cur_width_part)
    print("cur_height_part:", cur_height_part)
    print("cycle:", i)
    print("")