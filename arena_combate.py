class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.__vida = vida

    def obtener_vida(self):
        return self.__vida

    def reducir_vida(self, cantidad):
        self.__vida = max(0, self.__vida - cantidad)

    def atacar(self):
        return 0

class Guerrero(Personaje):
    def atacar(self):
        return 25

class Mago(Personaje):
    def atacar(self):
        return 40

heroe = Guerrero("Aragorn", 100)
villano = Mago("Sauron", 150)

print(f"{heroe.nombre} ataca causando {heroe.atacar()} de daño.")
villano.reducir_vida(heroe.atacar())
print(f"Vida restante de {villano.nombre}: {villano.obtener_vida()}")