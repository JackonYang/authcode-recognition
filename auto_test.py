# -*- Encoding: utf-8 -*-
from parser import recog

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


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        filename = raw_input(u'picture filename: ')
        filenames = [filename]
    elif len(sys.argv) == 2:
        filenames = [sys.argv[1]]
    else:
        filenames = sys.argv[1:]

    print test(filenames)
