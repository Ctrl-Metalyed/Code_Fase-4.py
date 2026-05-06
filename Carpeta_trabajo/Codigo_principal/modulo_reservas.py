class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"  #pendiente, confirmada, cancelada (pendiente es el valor inicial)

        self.validar_datos()

#validar datos de entrada
    def validar_datos(self):
        if self.cliente is None:
            raise ValueError("La reserva debe tener un cliente")

        if self.servicio is None:
            raise ValueError("La reserva debe tener un servicio")

        if self.duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")

#confirmacion de la reserva con validaciones
    def confirmar(self):
        if self.estado == "cancelada":
            raise Exception("No se puede confirmar una reserva cancelada")

        if not self.servicio.disponible():
            raise Exception("El servicio no está disponible")

        self.estado = "confirmada"
        print("Reserva confirmada")

#Cancelar reserva con validaciones
    def cancelar(self):
        if self.estado == "cancelada":
            raise Exception("La reserva ya está cancelada")

        self.estado = "cancelada"
        print("Reserva cancelada")

#procesamos la reserva con manejo de errores
    def procesar(self):
        try:
            self.confirmar()
        except Exception as error:
            print("Error al procesar la reserva:", error)

#Calcular costo
    def calcular_costo(self):
        try:
            return self.servicio.calcular_costo(self.duracion)
        except AttributeError:
            return 0

#imprimir detalles de la reserva 
    def mostrar(self):
        print("Reserva:")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Duración: {self.duracion}")
        print(f"Estado: {self.estado}")
        print(f"Costo: {self.calcular_costo()}")