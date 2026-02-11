from abc import ABC

class Celular(ABC):
    def __init__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento
        self.volumen = 50  # volumen inicial
    
    def informacion(self):
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}GB")
        print(f"Nivel de volumen: {self.volumen}%")
    
    def subir_volumen(self):
        if self.volumen < 100:
            self.volumen += 1
        print(f"Volumen aumentado a {self.volumen}%.")

    def bajar_volumen(self):
        if self.volumen > 0:
            self.volumen -= 1
        print(f"Volumen disminuido a {self.volumen}%.")

    def encender(self):
        print("El celular se ha encendido.")
    
    def apagar(self):
        print("El celular se ha apagado.")


class Android(Celular):
    def __init__(self, color, almacenamiento):
        super().__init__(color, almacenamiento)

    def expansion_almacenamiento(self):
        print("Expandiendo almacenamiento de celular Android.")

    def encender(self):
        super().encender()
        print("El celular Android muestra el logo de Android.")

    def apagar(self):
        super().apagar()
        print("El celular Android muestra el logo de Android al apagarse.")


class IPhone(Celular):
    def __init__(self, color, almacenamiento):
        super().__init__(color, almacenamiento)

    def encender(self):
        super().encender()
        print("El iPhone muestra el logo de Apple.")

    def transferir_archivos(self):
        print("Transfiriendo archivos a la computadora.")

    def apagar(self):
        super().apagar()
        print("El iPhone muestra el logo de Apple al apagarse.")


# Pruebas
celular_android = Android("azul", 128)
celular_android.informacion()
celular_android.encender()
celular_android.subir_volumen()

print("\n-----------------\n")

celular_iphone = IPhone("rojo", 256)
celular_iphone.informacion()
celular_iphone.encender()
celular_iphone.transferir_archivos()

