import qrcode
#Información del QR
def generarQR(nombreQR, informacion):
    img = qrcode.make(informacion)
    f = open(nombreQR, "wb")
    img.save(f)
    f.close()