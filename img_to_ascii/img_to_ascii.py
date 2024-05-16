#import pillow, PIL (python image library) for image processing
from PIL import Image
import PIL

# target_jpg = Image.open("5x5_img.jpg")
target_jpg = Image.open("image_one.jpg")
# target_jpg = Image.open("5x10_img.jpg")

px = target_jpg.load()


jpg_size = target_jpg.size
jpg_width = jpg_size[0]
jpg_height = jpg_size[1]
# print(jpg_height)
# print(jpg_width)
pixle_array = []


# print(px[4,9])

pixle_option = ['.', '^', ':', 'i', '|', 'n', 'm', 'X', '&', '#']

for i in range(jpg_height):
    temp_array = []
    for j in range(jpg_width):
        this_pixle = px[j,i]
        brightness = (this_pixle[0] + this_pixle[1] + this_pixle[2]) / 3

        if brightness > 0 and brightness <= 25:
            temp_array.append(pixle_option[0])
        elif brightness > 25 and brightness <= 50:
            temp_array.append(pixle_option[1])
        elif brightness > 50 and brightness <= 75:
            temp_array.append(pixle_option[2])
        elif brightness > 75 and brightness <= 100:
            temp_array.append(pixle_option[3])
        elif brightness > 100 and brightness <= 125:
            temp_array.append(pixle_option[4])
        elif brightness > 125 and brightness <= 150:
            temp_array.append(pixle_option[5])
        elif brightness > 150 and brightness <= 175:
            temp_array.append(pixle_option[6])
        elif brightness > 175 and brightness <= 200:
            temp_array.append(pixle_option[7])
        elif brightness > 200 and brightness <= 225:
            temp_array.append(pixle_option[8])
        else:
            temp_array.append("#")
        #print(temp_array)
    pixle_array.append(temp_array)

# print(pixle_array)

#print(pixle_array[1039][827])

for i in range(jpg_height):
    for j in range(jpg_width):
        print(pixle_array[i][j], end="")
        # print(pixle_array[i][j], end="")
    print("")






