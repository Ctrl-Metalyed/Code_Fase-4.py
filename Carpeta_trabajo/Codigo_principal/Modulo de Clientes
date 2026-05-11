from modelos_base import EntidadSistema

class Cliente(EntidadSistema):

    def __init__(self, id, nombre, correo):
        super().__init__(id)

        # Validaciones
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.nombre = nombre
        self.correo = correo

    def mostrar_info(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")

# Crear cliente de prueba
cliente1 = Cliente(1, "Natalia", "natalia.unad@prueba.com")

# Mostrar información
cliente1.mostrar_info()
