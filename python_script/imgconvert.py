#!/usr/bin/python
import os
import img2pdf
# This script will get all img file(jpg, png, gif) in the working folder, then convert them in to a single pdf file. 
with open("output.pdf", "wb") as f:
    target = [i for i in os.listdir(os.getcwd()) if i.endswith((".jpg",".png","gif"))]
    if len(target) > 0:
        f.write(img2pdf.convert(target))


