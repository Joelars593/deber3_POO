class Notificacion:
    def __init__(self, destino):
        self.__destino = destino

    def obtener_destino(self):
        return self.__destino

    def enviar(self, mensaje):
        pass

class CorreoElectronico(Notificacion):
    def enviar(self, mensaje):
        return f"Enviando Email a [{self.obtener_destino()}]: <html><body>{mensaje}</body></html>"

class MensajeTexto(Notificacion):
    def enviar(self, mensaje):
        mensaje_corto = mensaje[:160]
        return f"Enviando SMS al número ({self.obtener_destino()}): {mensaje_corto}"

alertas = [CorreoElectronico("user@email.com"), MensajeTexto("+593999999")]
for alerta in alertas:
    print(alerta.enviar("Tu código de verificación de seguridad de la cuenta es 4829"))