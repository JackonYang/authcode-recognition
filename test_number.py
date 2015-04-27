# -*- Encoding: utf-8 -*-
import os
from parser import recog

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

test_dir = os.path.join(BASE_DIR, 'img/check')

def get_num(filename):
    return filename[1:filename.index('.')]

testdata = [(os.path.join(test_dir, filename), get_num(filename)) for filename in  os.listdir(test_dir)]

err_cnt = 0

for imgfile, expt in testdata:
    res = recog(imgfile)
    if res != expt:
        err_cnt += 1
        print 'error! filename: %s. got: %s' % (imgfile, res)
print '%d files tested. %d error' % (len(testdata), err_cnt)
