#!/usr/bin/env python3
import os
import requests

url = "http://[YOUR_SERVER_IP]/upload/"
image_dir = "/home/student/supplier-data/images"
for image in os.listdir(image_dir):
    if image.endswith(".jpeg"):
        with open(os.path.join(image_dir, image), 'rb') as opened:
            requests.post(url, files={'file': opened})
