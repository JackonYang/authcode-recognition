# Validation Code Recognition

## Usage

#### command line

```shell
$ python parser.py img/check/n1313.jpg
# output: 1313
$ python test_number.py
# output: 5 files tested. 0 error
```

#### web page

under constructing

## Dependencies

1. [PIL](http://effbot.org/imagingbook/pil-index.htm).
    Python Imaging Library, userd for noise reduction. workflow: RGB -> grayscale image -> binary image 
2. [Tesseract-OCR](https://github.com/justin/tesseract-ocr). google OCR Engine
3. [pytesseract](https://github.com/madmaze/pytesseract). a wrapper for google's Tesseract-OCR


## Installation

For ubuntu, just run `install.sh`

```bash
$ ./install.sh
```
