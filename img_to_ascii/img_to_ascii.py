#import pillow, PIL (python image library) for image processing
from PIL import Image
import PIL

target_jpg = Image.open("5x5_img.jpg")

jpg_size = target_jpg.size
jpg_width = jpg_size[0]
jpg_height = jpg_size[1]
pixle_array = []

"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

pixle_option = ['.', '^', ':', 'i', '|', 'n', 'm', 'X', '&', '#']

for i in range(jpg_width):
    temp_array = []
    for j in range(jpg_height):
        this_pixle = target_jpg.getpixel((i, j))
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
            pixle_array.append("!")
        #print(temp_array)
    pixle_array.append(temp_array)

print(pixle_array)




