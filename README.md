# Validation Code Recognition

## Usage

#### command line

```shell
$ python download.py http://XXX.XXX/authcode  # effective url
#authcode downloading. 1 / 20
#authcode downloading. 2 / 20
#authcode downloading. 3 / 20
#authcode downloading. 4 / 20
#authcode downloading. 5 / 20
#authcode downloading. 6 / 20
#......
#authcode downloading. 20 / 20
$ python parser.py img/check/n1313.jpg  # 1 file
# output: 1313
$ python parser.py img/check/*  # multi file
#res:1313, filename=img/check/n1313.jpg
#res:3825, filename=img/check/n3825.jpg
#res:5444, filename=img/check/n5444.jpg
#res:7293, filename=img/check/n7293.jpg
#res:7690, filename=img/check/n7690.jpg
```

#### Test

```shell
# 使用 img/check 目录下的图片验证正确性
$ python test_number.py
# output: 5 files tested. 0 error
# 自动下载新图片并识别, 结果呈现在 HTML 页面中
$ python auto_test.py http://XXX.XXX/authcode  # effective url
```

也可以通过一行命令开启一个简单的 HTTP 服务器,
方便异地通过 IP 地址查看结果.

```shell
$ python -m SimpleHTTPServer  # start a http server
```

visit [http://127.0.0.1:8000/result.html][http://www.safebang.org:8000/result.html]

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
