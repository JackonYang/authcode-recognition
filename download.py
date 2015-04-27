# -*- Encoding: utf-8 -*-
import os
import socket
from httplib2 import Http


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
output_dir = os.path.join(BASE_DIR, 'img/download')

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

file_seq = len(os.listdir(output_dir))
print file_seq

def get_name():
    return os.path.join(output_dir, '%s.jpg' % file_seq)

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
    download(sys.argv[1])
