QRnizer
==============

This is a quick tool to create a QR code with personalize image in the center.

# prerequisite

+ [PIL](http://www.pythonware.com/products/pil/)
+ [qrcode](https://pypi.python.org/pypi/qrcode)

# Usage

	import qrnizer
	qr = qrnizer.QRnizer("Hello the world")
	qr.insert_image("image_file")
	qr.show()
	qr.save("new_file_name")