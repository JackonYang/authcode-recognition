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

    if len(sys.argv) == 1:
        filename = raw_input(u'picture filename: ')
        filenames = [filename]
    elif len(sys.argv) == 2:
        filenames = [sys.argv[1]]
    else:
        filenames = sys.argv[1:]

    for f in filenames:
        print 'res:%s, filename=%s' % (recog(f), f)
