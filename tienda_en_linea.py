class Producto:
    def __init__(self, nombre, precio_costo):
        self.nombre = nombre
        self.__precio_costo = precio_costo

    def obtener_costo(self):
        return self.__precio_costo

    def calcular_precio_venta(self):
        return self.__precio_costo * 1.20

class ProductoFisico(Producto):
    def __init__(self, nombre, precio_costo, peso_kg):
        super().__init__(nombre, precio_costo)
        self.peso_kg = peso_kg

    def calcular_precio_venta(self):
        costo_envio = self.peso_kg * 5
        return super().calcular_precio_venta() + costo_envio

class ProductoDigital(Producto):
    def calcular_precio_venta(self):
        impuesto_digital = super().calcular_precio_venta() * 0.05
        return super().calcular_precio_venta() + impuesto_digital

libro_fisico = ProductoFisico("Enciclopedia", 20, 3)
libro_digital = ProductoDigital("E-book", 10)

print(f"Precio venta {libro_fisico.nombre}: ${libro_fisico.calcular_precio_venta()}")
print(f"Precio venta {libro_digital.nombre}: ${libro_digital.calcular_precio_venta()}")