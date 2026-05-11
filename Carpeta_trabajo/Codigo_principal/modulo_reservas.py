from excepciones_personalizadas import SoftwareFJError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        self.validar_datos()

    def validar_datos(self):
        if self.cliente is None:
            raise ValueError("La reserva debe tener un cliente")
        if self.servicio is None:
            raise ValueError("La reserva debe tener un servicio")
        if self.duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")

    def confirmar(self):
        if self.estado == "cancelada":
            raise SoftwareFJError("No se puede confirmar una reserva cancelada")
        
        # Ahora esto funcionará porque agregamos .disponible() en servicios.py
        if not self.servicio.disponible():
            raise SoftwareFJError("El servicio no está disponible actualmente")
            
        self.estado = "confirmada"
        print(">>> Estado interno: Reserva validada y confirmada.")

    def cancelar(self):
        self.estado = "cancelada"
        print(">>> Estado interno: Reserva anulada.")
