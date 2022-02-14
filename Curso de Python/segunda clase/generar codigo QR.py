import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create("https://www.googlesnake.com/")
url.svg("portafolio.svg", scale=8)
