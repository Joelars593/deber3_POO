class VehiculoRenta:
    def __init__(self, modelo, tarifa_base):
        self.modelo = modelo
        self.__tarifa_base = tarifa_base

    def obtener_tarifa(self):
        return self.__tarifa_base

    def calcular_alquiler(self, dias):
        pass

class Auto(VehiculoRenta):
    def calcular_alquiler(self, dias):
        total = self.obtener_tarifa() * dias
        if dias > 7:
            total *= 0.90
        return total

class Moto(VehiculoRenta):
    def calcular_alquiler(self, dias):
        seguro_casco = 5 * dias
        return (self.obtener_tarifa() * dias) + seguro_casco

vehiculos = [Auto("Toyota Corolla", 50), Moto("Honda CBR", 30)]
for v in vehiculos:
    print(f"Vehículo: {v.modelo} | Alquiler por 10 días: ${v.calcular_alquiler(10)}")