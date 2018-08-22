"""
Add Image to QR code
====================

Author: Jiayi Liu
Date: 8/21/2018

"""
from .QRnizer import QRnizer

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Create a personalized QR code")
    parser.add_argument('message', type=str, help="Message encoded in QR code")
    parser.add_argument('save', type=str, help="Image path to save")
    parser.add_argument('image', type=str, help="Image to be inserted", nargs='?', default='')
    args = None
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit(1)

    qr = QRnizer(args.message)
    if args.image:
        qr.insert_image(args.image)
    qr.save(args.save)
