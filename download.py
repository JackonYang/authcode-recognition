# -*- Encoding: utf-8 -*-
import os
import socket
from httplib2 import Http

output_dir = 'img/download'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

start_idx = len(os.listdir(output_dir))

def get_name():
    file_seq = len(os.listdir(output_dir))
    return os.path.join(output_dir, '%s.jpg' % file_seq)

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
