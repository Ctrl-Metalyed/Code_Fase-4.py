from Modulo_de_clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from modulo_reservas import Reserva
from gestion_logs import registrar_log
from excepciones_personalizadas import DatoInvalidoError

def ejecutar_sistema():
    print("=== SISTEMA DE GESTIÓN SOFTWARE FJ - FASE 4 ===")
    
    simulaciones = [
        {"id": 101, "nom": "Jesus Vasquez", "mail": "jesus@unad.edu.co", "dur": 5, "tipo": "Exitoso"},
        {"id": 102, "nom": "", "mail": "error@unad.com", "dur": 2, "tipo": "Fallo: Nombre Vacío"},
        {"id": 103, "nom": "Natalia Chaves", "mail": "natalia.unad", "dur": 3, "tipo": "Fallo: Email sin @"},
        {"id": 104, "nom": "Samuel V", "mail": "sam@unad.com", "dur": -1, "tipo": "Fallo: Duración negativa"},
        {"id": 105, "nom": "Maria Claudia", "mail": "maria@unad.com", "dur": 10, "tipo": "Exitoso"},
        {"id": 106, "nom": "Brayan Piracon", "mail": "brayan@unad.com", "dur": 4, "tipo": "Exitoso"},
        {"id": 107, "nom": "Juan Bohorquez", "mail": "juan@unad.com", "dur": 0, "tipo": "Fallo: Duración cero"},
        {"id": 108, "nom": "Steven Contreras", "mail": "steven@unad.com", "dur": 8, "tipo": "Exitoso"},
        {"id": 109, "nom": "Prueba Error", "mail": "test@unad.com", "dur": 1, "id_bad": "ABC", "tipo": "Fallo: ID no numérico"},
        {"id": 110, "nom": "Cliente Final", "mail": "final@unad.com", "dur": 12, "tipo": "Exitoso"}
    ]

    for i, caso in enumerate(simulaciones, 1):
        print(f"\n>>> Procesando Operación {i}: {caso['tipo']}")
        
        try:
            # Creación de objetos con manejo de excepciones
            cliente = Cliente(caso.get("id_bad", caso["id"]), caso["nom"], caso["mail"])
            
            # Ajuste: Enviamos ID, Nombre y Costo Base
            servicio = ReservaSala(500 + i, "Sala Principal", 45000) 
            
            reserva = Reserva(cliente, servicio, caso["dur"])
            reserva.confirmar()

        except (ValueError, Exception) as e:
            error_msg = f"Error en Op {i}: {str(e)}"
            print(f"❌ {error_msg}")
            registrar_log(error_msg)

        else:
            success_msg = f"✅ Reserva exitosa para {cliente.nombre}"
            print(success_msg)
            registrar_log(success_msg, "INFO")

        finally:
            print(f"--- Fin de validación operación {i} ---")

    print("\nSimulación finalizada. Revise 'sistema_errores.log' para el historial.")

if __name__ == "__main__":
    ejecutar_sistema()
