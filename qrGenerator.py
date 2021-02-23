#!python3
# qrGenerator.py - generates QR code

import pyqrcode
from pyqrcode import QRCode

data = input("Enter text to insert in QR: ")

qr = pyqrcode.create(data)

filename = input("Enter filename to save as: ")

qr.png(f"{filename}.png", scale = 8)  # saves qr code as image
qr.svg(f"{filename}.svg", scale = 8)  # saves qr code as svg


