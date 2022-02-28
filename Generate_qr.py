import qrcode
from PIL import Image
import requests

face= Image.open('/home/pi/Desktop/Antitheft1/dataset/Ajit/image_0.jpg').crop((175,90,235,150))
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)




qr_big.add_data('Verified Qr Code')
qr_big.make()
img_qr_big=qr_big.make_image().convert('RGB')


pos = ((img_qr_big.size[0] - face.size[0])// 2, (img_qr_big.size[1]-face.size[1])//2)

img_qr_big.paste(face,pos)
img_qr_big.save('qr_Ajit.png')


#! /usr/bin/python

# Imports


def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandboxded521de48ff43d882fd24ac0e37f192.mailgun.org/messages",
        auth=("api", "9ff2862027ac32335ef517d658dce8c4-054ba6b6-308e33d7"),
        files = [("attachment", ("qr_Ajit.png", open("qr_Ajit.png", "rb").read()))],
        data={"from": "Antitheft-QR Code: Antitheft@mailgun.co",
            "to":["sahayaajith202@gmail.com"],
            "subject": "QR Code",
            "html": "<html> Please use this QR Code as an alternative to receiver your item.Thank You!! </html> "})
                  
request = send_simple_message()

print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))





