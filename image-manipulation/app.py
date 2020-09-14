#!/usr/bin/env python3
from PIL import Image
from os import listdir, chdir, rename

def transform(files):
    for file in files:
<<<<<<< HEAD
        new_name = file+'.jpeg' # As original files didn't had any extention
>>>>>>> 00b3868214e3326c7733aef8f85516f6db2cf7d9
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
