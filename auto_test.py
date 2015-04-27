# -*- Encoding: utf-8 -*-
import os
from parser import recog
import codecs
from jinja2 import Environment, FileSystemLoader


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
template_dir = os.path.join(BASE_DIR, "templates")

def test(filenames):
    total = len(filenames)
    result = []
    for f, i in zip(filenames, range(total)):
        print 'recognizing. %d / %d | fliename = %s' % (i, total, f)
        result.append({
            'result': recog(f),
            'filename': f,
            })
    return result


def disp(data):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('index.html')

    filename = 'result.html'
    with codecs.open(filename, 'w', 'utf8') as f:
        f.write(template.render(data=data))
    print 'success! saved in %s' % os.path.abspath(filename)

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        filename = raw_input(u'picture filename: ')
        filenames = [filename]
    elif len(sys.argv) == 2:
        filenames = [sys.argv[1]]
    else:
        filenames = sys.argv[1:]

    disp(test(filenames))
