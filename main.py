import qrcode
from qrcode.main import QRCode

qr = qrcode.QRCode(
    version= 1,
    error_correction = qrcode.ERROR_CORRECT_L,
    box_size= 40,
    border= 1
)

qr.add_data('https://docs.google.com/document/d/1ehqSl2sZCrYeX-nAmSbhXsixbCnfhGQnG51ex1xHpyg/edit?usp=sharing')
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save('qrcodeteste.png')