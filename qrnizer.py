from PIL import Image
import qrcode


class QRnizer():
    def __init__(self, message, version=2, box_size=10, border=4):
        """
        Create a QR code with personalized central picture

        :param message: Message for the QR code
        :param version: QR version. from 1 to 40, for grid 21x21 to 177x177
        :param box_size: pixel number for each grid
        :param border: border grid number, minimum is 4
        :return: QRnizer class
        """
        if border < 4:
            raise Exception("border smaller than 4 is not allowed")
        self.conner = (border + 7 + 2) * box_size  # calculate the conner to insert central piture
        self.size = ((version * 4 + 17) - (7 + 2) * 2) * box_size
        qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
        qr.add_data(message)
        self.qrimage = qr.make_image().convert("RGB")

    def insert_image(self, image_file):
        """
        Insert image into the central region of the QR code
        :param image_file:
        :return: Image created
        """
        img = Image.open(image_file)
        img.thumbnail((self.size, self.size))
        box = (self.conner, self.conner, self.conner + self.size, self.conner + self.size)
        self.qrimage.paste(img, box=box)
        return self.qrimage

    def show(self):
        self.qrimage.show()

    def save(self, filename):
        self.qrimage.save(filename)
