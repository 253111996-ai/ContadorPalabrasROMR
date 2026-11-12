import sys
from PyQt5 import QtWidgets, uic

class contadorPalabras(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #carga nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)

    def ContarPalabras(self):
        #Recuperar texto✅
        texto = self.edtCaracteres.text()
        print(texto)

        #SepararTexto✅|    
        textoSeparado = texto.split()
        print(textoSeparado)

        #Contar palabras
        #Contar CAracteres

        print("Se ha presionado el boton")

app= QtWidgets.QApplication(sys.argv)
ventana = contadorPalabras()
ventana.show()
sys.exit(app.exec())