import datetime

def registrar_log(mensaje, nivel="ERROR"):
    """Guarda los eventos en sistema_errores.log sin detener la ejecución."""
    try:
        with open("sistema_errores.log", "a", encoding="utf-8") as archivo:
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{fecha_hora}] {nivel.upper()}: {mensaje}\n")
    except Exception as e:
        print(f"Error crítico al escribir en el log: {e}")
