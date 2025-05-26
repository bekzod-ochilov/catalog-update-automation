#!/usr/bin/env python3
import os
import requests

desc_dir = "/home/student/supplier-data/descriptions"
url = "http://[YOUR_SERVER_IP]/fruits/"
for file in os.listdir(desc_dir):
    if file.endswith(".txt"):
        with open(os.path.join(desc_dir, file)) as f:
            lines = f.read().splitlines()
            data = {
                "name": lines[0],
                "weight": int(lines[1].split()[0]),
                "description": lines[2],
                "image_name": file.replace(".txt", ".jpeg")
            }
            requests.post(url, json=data)