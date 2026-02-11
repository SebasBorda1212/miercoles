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


class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, id, salario_base, ventas_realizadas):
        super().__init__(nombre, id, salario_base)
        self.ventas_realizadas = ventas_realizadas

    def calcular_pago(self):
        pago_total = self.salario_base + (self.ventas_realizadas * 0.10)
        print(f"Pago total con comisión: ${pago_total}")


class EmpleadoHorasExtras(Empleado):
    def __init__(self, nombre, id, salario_base, horas_extras, valor_hora):
        super().__init__(nombre, id, salario_base)
        self.horas_extras = horas_extras
        self.valor_hora = valor_hora

    def calcular_pago(self):
        pago_total = self.salario_base + (self.horas_extras * self.valor_hora)
        print(f"Pago total con horas extras: ${pago_total}")
