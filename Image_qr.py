import qrcode
from PIL import Image

face= Image.open('/home/pi/Desktop/Antitheft1/dataset/Ibrahim/image_0.jpg').crop((175,90,235,150))
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)




qr_big.add_data('Verified Qr Code')
qr_big.make()
img_qr_big=qr_big.make_image().convert('RGB')


pos = ((img_qr_big.size[0] - face.size[0])// 2, (img_qr_big.size[1]-face.size[1])//2)

img_qr_big.paste(face,pos)
img_qr_big.save('qr_ibrahim.png')

