#!/usr/bin/env python3

from PIL import Image
import os, sys

user = os.getenv('USER')
img_dir = '/home/{}/supplier-data/images/'.format(user)

for filename in os.listdir(img_dir):
    if filename.lower().endswith(".tiff"):
        img_path = os.path.join(img_dir, filename)
        img = Image.open(img_path)
        img = img.resize((600,400))
        if img.mode == "RGBA":
            img = img.convert("RGB")
        new_filename = os.path.splitext(filename)[0] + ".jpeg"
        new_img_path = os.path.join(img_dir, new_filename)
        img.save(new_img_path, format="JPEG")
