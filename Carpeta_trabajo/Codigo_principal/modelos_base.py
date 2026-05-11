from abc import ABC, abstractmethod

# Clase abstracta base del sistema
class EntidadSistema(ABC):

    def __init__(self, id):
        self.id = id

    # Método abstracto obligatorio
    @abstractmethod
    def mostrar_info(self):
        pass
