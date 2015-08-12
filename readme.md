QRnizer
==============

This is a quick tool to create a QR code with personalize image in the center.

# Prerequisite

+ [PIL](http://www.pythonware.com/products/pil/)
+ [qrcode](https://pypi.python.org/pypi/qrcode)

## PIL Installation

[Python Imaging Library (PIL)]((http://www.pythonware.com/products/pil/)) is not easy to install.  The easiest way
is to install [pillow](https://python-pillow.github.io/).  For people
using [conda](http://conda.pydata.org/docs/), please find the
corresponidng version of pillow.

### qrcode Installation

[qrcode](https://pypi.python.org/pypi/qrcode) is a package to render
qrcode.  It can be installed by package management systems like `pip`
or `conda`.

# Package Installation

## Easy Way

Simply copy the `qrnizer.py` into your `PYTHONPATH` directory.

# Usage

    # import QRnizer
	from qrnizer import QRnizer
    # Create your message (or link)
	qr = QRnizer("Hello the world")
    # insert the image
	qr.insert_image("image_file")
    # show the result and test
	qr.show()
    # save the result into a file
	qr.save("new_file_name")

# TODO

1. Covert to package
2. Provide auto scale calculation
