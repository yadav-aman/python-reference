#!/usr/bin/env python3
from PIL import Image
from os import listdir, chdir, rename

def transform(files):
    for file in files:
        new_name = file+'.jpeg' # As original files didn't have any extention
        """
        For each file:
        1. Rotate the image 90° clockwise
        2. Resize the image from 192x192 to 128x128
        3. Save the image to a new folder in .jpeg format
        """
        im = Image.open(file).convert('RGB')
        new_location = '/opt/icons/'+new_name
        im.rotate(270).resize((128,128)).save(new_location) # rotate() function rotates images counter clockwise

if __name__ == '__main__':
    files = listdir("images")
    chdir('/home/student-03-76bf325c4c2b/images')
    print("Transforming Images")
    transform(files)
    print("Transformation Done")