class SoftwareFJError(Exception):
    """Clase base para todas las excepciones del sistema Software FJ."""
    pass

class DatoInvalidoError(SoftwareFJError):
    """Se lanza cuando los datos no cumplen con los requisitos de validación."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio solicitado no puede procesarse."""
    pass