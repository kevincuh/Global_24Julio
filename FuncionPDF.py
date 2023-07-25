from reportlab.pdfgen import canvas
ruta = "C:/Users/Kevo/Escritorio/Modularidad python/prueba funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"

def generarPDF():
    c = canvas.Canvas(nombreArchivo)
    c.drawString(200,600,"Hola desde una función")
    c.save()
    print("Reporte generado----------")