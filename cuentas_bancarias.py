class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return self.__saldo

    def modificar_saldo(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        pass

class CuentaAhorros(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad <= self.consultar_saldo():
            self.modificar_saldo(-cantidad)
            return f"Retiro exitoso de ${cantidad}"
        return "Error: Fondos insuficientes."

class CuentaCorriente(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad > self.consultar_saldo():
            self.modificar_saldo(-(cantidad + 15))
            return f"Sobregiro aplicado. Retiraste ${cantidad} (Multa: $15)"
        self.modificar_saldo(-cantidad)
        return f"Retiro estándar de ${cantidad}"

c1 = CuentaAhorros("Juan", 100)
c2 = CuentaCorriente("Maria", 100)

print(c1.retirar(150))
print(c2.retirar(150))