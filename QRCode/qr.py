import qrcode

#Create QR Object
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border = 1)

#User Data

data = input("Enter Data You Want To Convert Into QR: ")

#Convert User Input To QR
qr.add_data(data)
qr.make(fit=True)

#Specify Colors
img = qr.make_image(fill_color = "black", back_color = "white")

#Save Image With File Name
img.save("myqr.png")