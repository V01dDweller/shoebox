#!/usr/bin/env python3

"""
Given a directory full of photos, iterate through them in order to
create a directory, then move each photo into that directory. The goal
is to organize a collection of photos in folders, for example, iCloud
Photo from a iPhone and iPad.
"""

import glob
import os
import shutil
from PIL import Image

def get_date_taken(path):
    """
    Use the PIL library to get image metadata. Return the shooting date
    in YYYY-MM-DD format

    Credit: https://stackoverflow.com/a/23064792
    """
    raw_date_time = Image.open(path)._getexif()[36867]
    date_time_dashed = raw_date_time.replace(":", "-")
    date_time = date_time_dashed.split(' ')[0]

    return date_time

COLOR = {
    "red": "\u001b[31;1m",
    "green": "\u001b[32;1m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35;1m",
    "cyan": "\u001b[36;1m",
    "white": "\u001b[37;1m",
    "reset": "\u001b[0m"
    }

HOME_DIR = os.environ['HOME']
WORK_DIR = HOME_DIR + '/Desktop/test_photos/'
IMAGE_LIST = glob.glob(WORK_DIR + '/*JPG')

print('Ready to organize ' + COLOR["yellow"] +  str(len(IMAGE_LIST)) +
    COLOR["reset"] + ' images in \'' + COLOR["blue"] + WORK_DIR +
    COLOR["reset"] + '\' ?')
print(' ')
input("Press Enter to continue")

for image in IMAGE_LIST:
    DATE = get_date_taken(image)
    IMAGE_BASENAME = os.path.basename(image)
    DEST_DIR = WORK_DIR + DATE
    DEST = DEST_DIR + '/' + IMAGE_BASENAME
    if not os.path.exists(DEST_DIR):
        print('Creating folder ' + COLOR["blue"] + DATE + COLOR["reset"])
        os.mkdir(DEST_DIR)
    print ('Moving file ' + COLOR["green"] + IMAGE_BASENAME + COLOR["reset"] +
        ' to ' + COLOR["blue"] + DATE + COLOR["reset"] + ' folder')
    shutil.move(image, DEST)

print(' ')

# vi: ts=4:sw=4:expandtab:
