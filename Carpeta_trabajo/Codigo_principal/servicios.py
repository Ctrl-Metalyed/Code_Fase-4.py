from modelos_base import EntidadSistema
from abc import abstractmethod

class Servicio(EntidadSistema):
    def __init__(self, id, nombre, costo_base):
        super().__init__(id)
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    def disponible(self):
        """Indica si el servicio está habilitado (Requerido por la clase Reserva)."""
        return True

    def mostrar_info(self):
        print(f"Servicio: {self.nombre} | Costo Base: {self.costo_base}")

class ReservaSala(Servicio):
    def calcular_costo(self, horas, limpieza=False):
        total = self.costo_base * horas
        return total + 50 if limpieza else total

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, seguro=True):
        total = self.costo_base * dias
        return total * 1.15 if seguro else total

class Asesoria(Servicio):
    def calcular_costo(self, sesiones):
        return self.costo_base * sesiones
