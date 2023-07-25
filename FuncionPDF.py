from reportlab.pdfgen import canvas
ruta = "C:/Users/Kevo/Escritorio/Modularidad python/prueba funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"

def generarPDF(listaNombres, listaEdades):
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    c.setFont('Helvetica', 20)
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial + 120,yInicial,"Nombre")
    for i in range(len(listaNombres)):
        yInicial = yInicial - 20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombres[i])
    c.save()
    print("Reporte generado----------")