# -*- Encoding: utf-8 -*-
import os
import socket
from httplib2 import Http

download_dir = 'img/download'

if not os.path.exists(download_dir):
    os.mkdir(download_dir)

start_idx = len(os.listdir(download_dir))

def get_name():
    file_seq = len(os.listdir(download_dir))
    return os.path.join(download_dir, '%s.jpg' % file_seq)

def req(url, method='POST'):
    h = Http(timeout=2)

    try:
        rsp, content = h.request(url, method)
    except socket.timeout:
        return None
    else:
        with open(get_name(), 'w') as f:
            f.write(content)

    return content

def reqs(url, num=20):
    for i in range(num):
        print 'authcode downloading. %d / %d' % (i+1, num)
        req(url)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        url = raw_input(u'validation code url: ')
    else:
        url = sys.argv[1]

    reqs(url)
