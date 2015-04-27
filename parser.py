# -*- Encoding: utf-8 -*-
import Image
from pytesseract import image_to_string

def recog(filename, threshold = 140):
    im = Image.open(filename)
    imgry = im.convert('L') 
    out = imgry.point(lambda i: 0 if i < threshold else 255)
    return image_to_string(out)

if __name__ == '__main__':
    import sys
    print recog(sys.argv[1])
