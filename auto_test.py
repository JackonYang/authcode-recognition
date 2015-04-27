# -*- Encoding: utf-8 -*-
import os
from parser import recog
import download
import codecs
from jinja2 import Environment, FileSystemLoader


template_dir = "templates"

def disp(data):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('index.html')

    filename = 'result.html'
    with codecs.open(filename, 'w', 'utf8') as f:
        f.write(template.render(data=data))
    print 'success! saved in %s' % filename

def run_test(url):
    download.reqs(url, 2)

    filenames = [os.path.join(download.download_dir, f) for f in os.listdir(download.download_dir)]
    total = len(filenames)

    result = []
    for f, i in zip(filenames, range(total)):
        print 'recognizing. %d / %d | fliename = %s' % (i, total, f)
        result.append({
            'result': recog(f),
            'filename': f,
            })
    disp(result)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        url = raw_input(u'validation code url: ')
    else:
        url = sys.argv[1]

    run_test(url)
