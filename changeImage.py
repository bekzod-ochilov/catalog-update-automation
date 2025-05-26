#!/usr/bin/env python3
from PIL import Image
import os

image_dir = "/home/student/supplier-data/images"
for image_name in os.listdir(image_dir):
    if image_name.endswith(".tiff") or image_name.endswith(".tif"):
        im = Image.open(os.path.join(image_dir, image_name)).convert("RGB")
        im = im.resize((600, 400))
        im.save(os.path.join(image_dir, image_name.split('.')[0] + ".jpeg"), "JPEG")
