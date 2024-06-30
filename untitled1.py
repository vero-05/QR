!pip install qrcode[pil]

import qrcode
from google.colab import files

def generar_qr(texto):
    qr = qrcode.make(texto)
    qr.save("qr.png")
    files.download("qr.png")

texto = input("texto: ")
generar_qr(texto)