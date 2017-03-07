#!/usr/bin/env python3
from PIL import Image
from os.path import splitext
import sys
import glob
def resizeFactory(x,y,name):
	im = Image.open(name)
	nim = im.resize((x,y), Image.BILINEAR)
	new = splitext(name)[0]+"_"+str(x)+"x"+str(y)
	nim.save(new+".png","PNG")
def main():
    if ( len(sys.argv) > 1 ):
        name = sys.argv[1]
        x = sys.argv[2]
        y = sys.argv[3]
    else:
	    name = input("Enter File name:")
	    x = input("weight:")
	    y = input("height:")
    print("Start Conversion")
    resizeFactory(int(x),int(y),name)
	#print "ldpi"
	#resizeFactory(36,36,name)
	#print "mdpi"
	#resizeFactory(48,48,name)
	#print "hdpi"
	#resizeFactory(72,72,name)
	#print "xhdpi"
	#resizeFactory(96,96,name)

if __name__ == "__main__":
	main()
