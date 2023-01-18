import qrcode
import image

qr = qrcode.QRCode(
    version = 5,
    box_size = 8,
    border = 2
)
data = "https://pythonhosted.org/PyQRCode/"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")