#!/usr/bin/env python
"""
Add Image to QR code
====================

Author: Jiayi Liu
Date: 8/21/2018

"""
import logging
from PIL import Image
import qrcode

logger = logging.getLogger(__name__)


class QRnizer:
    """
    Create a QR code with personalized central picture

    :param message: Message for the QR code
    :param version: QR version. from 1 to 40, for grid 21x21 to 177x177
    :param box_size: pixel number for each grid
    :param border: border grid number, minimum is 4
    """

    def __init__(self, message, version=2, box_size=10, border=4):
        if border < 4:
            raise Exception("border smaller than 4 is not allowed")
        self.conner = (border + 7 + 2) * box_size  # calculate the conner to insert central picture
        self.size = ((version * 4 + 17) - (7 + 2) * 2) * box_size
        qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
        qr.add_data(message)
        self.qr_image = qr.make_image().convert("RGB")

    def insert_image(self, image_file):
        """
        Insert image into the central region of the QR code
        :param image_file:
        """
        img = Image.open(image_file)
        logger.info("Input image size is %dx%d" % (img.width, img.height))
        img.thumbnail((self.size, self.size))
        logger.info("Resize to %dx%d"%(self.size, self.size))
        box = (self.conner, self.conner, self.conner + self.size, self.conner + self.size)
        self.qr_image.paste(img, box=box)

    def show(self):
        self.qr_image.show()

    def save(self, filename):
        """
        Save to file

        :param filename: output filename
        """
        self.qr_image.save(filename)
