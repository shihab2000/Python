# #command
# #pip install qrcode[pil]
# import qrcode 

# text=input("Enter the text or url to be converted in Qrcode : ")
# filename=input("Enter filename to save the qrcode image : ")

# def generate_qr_code(text,filename):
#     image_qrcode=qrcode.make(text)
#     image_qrcode.save(filename)

# generate_qr_code(text,filename)

# import qrcode

# # user input
# url = input("Enter URL or text: ")
# filename = input("Enter file name (with .png): ")

# # QR setup
# qr = qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=5
# )

# qr.add_data(url)
# qr.make(fit=True)

# # create image
# img = qr.make_image(fill_color="black", back_color="white")
# img.save(filename)

# print("✅ QR Code generated successfully!")


import qrcode

def generate_qe_code(filepath="input.txt"):
    with open(filepath,"r") as file:
        lines=file.readlines()
    
    text=lines[0].strip()
    filename=lines[1].strip()
    
    image_qrcode=qrcode.make(text)
    image_qrcode.save(filename)

generate_qe_code("input.txt")