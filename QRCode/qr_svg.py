import qrcode
import qrcode.image.svg


factory = qrcode.image.svg.SvgPathImage

data = input("Enter Data You Want To Convert Into QR: ")

svg_img = qrcode.make(data, image_factory = factory)
svg_img.save("myqr.svg")