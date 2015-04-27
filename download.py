# -*- Encoding: utf-8 -*-
import os
import socket
from httplib2 import Http

num = 20

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
output_dir = os.path.join(BASE_DIR, 'img/download')

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

start_idx = len(os.listdir(output_dir))
file_seq = len(os.listdir(output_dir))

def get_name():
    global file_seq
    file_seq = len(os.listdir(output_dir))
    filename = os.path.join(output_dir, '%s.jpg' % file_seq)
    print 'authcode downloading. %d / %d | fliename = %s' % (file_seq-start_idx, num, filename)
    return filename

def download(url, method='POST'):
    h = Http(timeout=2)

    try:
        rsp, content = h.request(url, method)
    except socket.timeout:
        return None
    else:
        with open(get_name(), 'w') as f:
            f.write(content)

    return content

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        url = raw_input(u'validation code url: ')
    else:
        url = sys.argv[1]

    for i in range(num):
        download(url)
