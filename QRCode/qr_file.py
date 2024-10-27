import qrcode

def generate_qrcode(data):
    
    global count
    #Create QR Object
    qr = qrcode.QRCode(version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 20,
                    border = 1)
    
    #Convert User Input To QR
    qr.add_data(data)
    qr.make(fit=True)

    #Specify Colors
    img = qr.make_image(fill_color = "black", back_color = "white")

    #Save Image With File Name
    img.save(f"./myqr{count}.png")



#User Data
count = 0
input_file = input("Enter File Name: ")
with open(input_file, "r") as file:
    for i in file:
        count += 1
        data = i.strip()
        generate_qrcode(data)

