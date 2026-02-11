from abc import ABC, abstractmethod

from Act3 import Celular, android
class celular(ABC):
    @abstractmethod
    def __init__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento
    
    def informacion(self):
        print( f"Color: {self.color}")
        print( f"Almacenamiento: {self.almacenamiento}GB")
    
    def encender(self):
        print("El celular se ha encendido.")
    
    def apagar(self):
        print("El celular se ha apagado.")
    
    class android(Celular):
        def __init__(self, color, almacenamiento):
            super(android, self).__init__(color, almacenamiento)
        def expansion_almacenamiento(self, ):
            print("Expandiendo almacenamiento de celular Android.")

    class iphone(Celular):
        def tranferir_archivos(self):
            print("Transfiriendo archivos a la computadora.")
    




    