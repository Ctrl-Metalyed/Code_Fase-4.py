from modelos_base import EntidadSistema
from abc import abstractmethod

class Servicio(EntidadSistema):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas, limpieza=False):
        total = self.costo_base * horas
        return total + 50 if limpieza else total

    def obtener_detalles(self):
        return f"Sala: {self.nombre}"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, seguro=True):
        total = self.costo_base * dias
        return total * 1.15 if seguro else total

    def obtener_detalles(self):
        return f"Equipo: {self.nombre}"

class Asesoria(Servicio):
    def calcular_costo(self, sesiones):
        return self.costo_base * sesiones

    def obtener_detalles(self):
        return f"Asesoría técnica: {self.nombre}"