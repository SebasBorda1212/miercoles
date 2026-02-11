class Empleado:
    def __init__(self, nombre, id, salario_base):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base

    def calcular_pago(self):
        print(f"Salario base: ${self.salario_base}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
