from PIL import Image
import os
import csv

with open('picture_names.csv', 'rb') as datum:
    csvreader = csv.reader(datum, delimiter=',', quotechar='"')
    for row in csvreader:
        name = row[2] + '.jpg'
        username = row[1] + '.jpg'
        if os.path.exists(name):
            os.rename(name, username)
        else:
            print(name + "Does not exist")

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()


if __name__ == '__main__':
    image = 'grasshopper.jpg'
    crop(image, (161, 166, 706, 1050), 'cropped.jpg')
