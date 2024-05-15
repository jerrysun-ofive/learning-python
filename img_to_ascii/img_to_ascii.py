#import pillow, PIL (python image library) for image processing
from PIL import Image
import PIL

target_jpg = Image.open("/Users/jerrysun/Documents/learning-python/img_to_ascii/image_one.jpg")

jpg_size = target_jpg.size
jpg_width = jpg_size[0]
jpg_height = jpg_size[1]
pixle_array = []

"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

pixle_option = ['.', '^', ':', 'i', '|', 'n', 'm', 'X', '&', '#']

for i in range(jpg_width):
    for j in range(jpg_height):
        this_pixle = target_jpg.getpixel((i, j))
        brightness = (this_pixle[0] + this_pixle[1] + this_pixle[2]) / 3

        #print(str(brightness) + "  ")

        if brightness > 0 and brightness <= 25:
            pixle_array.append(pixle_array[0])
        elif brightness > 25 and brightness <= 50:
            pixle_array.append(pixle_array[1])
        elif brightness > 50 and brightness <= 75:
            pixle_array.append(pixle_array[2])
        elif brightness > 75 and brightness <= 100:
            pixle_array.append(pixle_array[3])
        elif brightness > 100 and brightness <= 125:
            pixle_array.append(pixle_array[4])
        elif brightness > 125 and brightness <= 150:
            pixle_array.append(pixle_array[5])
        elif brightness > 150 and brightness <= 175:
            pixle_array.append(pixle_array[6])
        elif brightness > 175 and brightness <= 200:
            pixle_array.append(pixle_array[7])
        elif brightness > 200 and brightness <= 225:
            pixle_array.append(pixle_array[8])
        else:
            pixle_array.append("!")

print(pixle_array)


