#! /usr/bin/env python3

import os
import requests
import json
from PIL import Image

def process_text_file(file_path):
    """
    Processes a text file and extracts relevant information.
    Returns a dictionary containing name, weight, description, and image_name.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        name = lines[0].strip()
        weight = int(lines[1].split()[0])  # Convert weight to an integer
        description = lines[2].strip()
        image_name = os.path.splitext(os.path.basename(file_path))[0] + ".jpeg"
        return {
            "name": name,
            "weight": weight,
            "description": description,
            "image_name": image_name,
        }

def upload_to_server(data, server_url):
    """
    Uploads the data (as JSON) to the specified server URL.
    """
    response = requests.post(server_url, json=data)
    if response.status_code == 201:
        print(f"Uploaded successfully: {data['name']}")
    else:
        print(f"Upload failed for {data['name']}")

if __name__ == "__main__":
    user = os.getenv('USER')
    base_dir = (f'/home/{user}/supplier-data/descriptions/')
    server_url = "http://34.16.143.43/fruits/"

    for filename in os.listdir(base_dir):
        if filename.lower().endswith(".txt"):
            file_path = os.path.join(base_dir, filename)
            fruit_data = process_text_file(file_path)
            upload_to_server(fruit_data, server_url)
