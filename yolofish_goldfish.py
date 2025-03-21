# -*- coding: utf-8 -*-
"""yolofish-goldfish.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O9X14c0HSuqBQ1dIR-GTY_6lCvtqA56K
"""

!nvidia-smi

!git clone https://github.com/jch-wang/YOLOV4-C-official-AlexeyAB.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/YOLOV4-C-official-AlexeyAB

!make

!./darknet

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="dyyGIX1ZxI2ZJEiK5Uce")
project = rf.workspace("project-8hufk").project("gold_fish_")
version = project.version(9)
dataset = version.download("yolov5")

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

!ls -l /content/yoyo/golf/test/

!find /content/ -type f -name "*.txt"

!pwd

# Commented out IPython magic to ensure Python compatibility.
# %cp /content/yoyo/golf/valid/labels/*.txt /content/yoyo/fish/

!ls -l /content/YOLOV4-C-official-AlexeyAB/golf/test/

import os
import glob
import IPython.display as display
from PIL import Image

# Define the directory
directory = "/content/yoyo/fish/"

# Count text files
txt_files = glob.glob(os.path.join(directory, "*.txt"))
txt_count = len(txt_files)

# Count image files (supports multiple formats)
image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp"]
image_files = []
for ext in image_extensions:
    image_files.extend(glob.glob(os.path.join(directory, ext)))

image_count = len(image_files)

# Print the results in table format
print(f"{'File Type':<12} | {'Count':<5}")
print("-" * 20)
print(f"{'Images':<12} | {image_count:<5}")
print(f"{'Text Files':<12} | {txt_count:<5}")

# Check if counts match
if image_count == txt_count:
    print("\n✅ The number of images and text files are equal!")
else:
    print("\n⚠️ The counts are not equal!")

# Display sample images (if any exist)
if image_files:
    print("\nDisplaying sample images:")
    for img_path in image_files[:5]:  # Show up to 5 images
        display.display(Image.open(img_path))

import glob, os


dataset_path = '/content/yoyo/fish'

# Percentage of images to be used for the test set
percentage_test = 12;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test+1:
        counter = 1
        file_test.write(dataset_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(dataset_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1

!wget https://pjreddie.com/media/files/yolov3-tiny.weights

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yoyo

!./darknet detector train /content/yoyo/cfg/voc.data /content/yoyo/cfg/yolov3-tiny_obj.cfg   /content/yolov3-tiny.weights -clear