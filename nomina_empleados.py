
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.__salario_base = salario_base 
    def obtener_salario_base(self):
        return self.__salario_base

    def calcular_pago(self):
        return self.__salario_base
    
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_pago(self):
        return self.obtener_salario_base() + self.bono

class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, horas_extra):
        super().__init__(nombre, salario_base)
        self.horas_extra = horas_extra

    def calcular_pago(self):
        pago_extra = self.horas_extra * 20
        return self.obtener_salario_base() + pago_extra

empleados = [Gerente("Ana", 3000, 500), Desarrollador("Luis", 2000, 10)]
for e in empleados:
    print(f"Empleado: {e.nombre} | Pago Total: ${e.calcular_pago()}")