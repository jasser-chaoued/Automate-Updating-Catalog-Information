#!/usr/bin/env python3
import requests
import os, sys
# This example shows how a file can be uploaded using
# The Python Requests module

user = os.getenv('USER') # To get the username from environment variable
img_dir = '/home/{}/supplier-data/images/'.format(user)
url = "http://localhost/upload/"

for img_name in os.listdir(img_dir) :
    if img_name.lower().endswith(".jpeg"):
        img_path = os.path.join(img_dir, img_name)
        with open(img_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
