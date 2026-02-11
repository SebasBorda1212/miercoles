class Celular:
    def __init__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento
        
    def information(self):
        print(f"color: {self.color}")
        print(f"almacenamiento:{self.almacenamiento}Gb")
        
    def encerder(self):
        print("encender celular")
        
    def apagar(self):
        print("apagar celular")
class android (Celular):
    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento de celular")

class Iphone (Celular):
    def transferir_archivos(self):
        print("transfiriendo archivos a la computadora")

celular_android = android ("blanco",64)
celular_android.expandir_almacenamiento()
celular_android.information()