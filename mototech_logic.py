import json

# Esta es la única variable global que usaremos para manejar todos los datos.
datos = {}

def cargar_datos():
    """Carga los datos de un archivo, si existe."""
    try:
        with open('mototech_datos.json', 'r') as archivo:
            global datos
            datos = json.load(archivo)
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Se iniciará con datos vacíos.")
        # Aseguramos que 'mantenimientos' sea siempre una lista
        datos = {'clientes': {}, 'mantenimientos': []}

def guardar_datos():
    """Guarda los datos en un archivo."""
    with open('mototech_datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Datos guardados con éxito en 'mototech_datos.json'.")

def registrar_cliente(nombre, telefono, modelo_moto):
    """Registra un nuevo cliente en los datos."""
    if 'clientes' not in datos:
        datos['clientes'] = {}
    
    nuevo_cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "modelo_moto": modelo_moto
    }
    datos['clientes'][nombre.lower()] = nuevo_cliente
    print(f"Cliente {nombre} registrado con éxito.")

def registrar_mantenimiento(matricula, fecha, servicio, costo):
    """Registra un nuevo mantenimiento en los datos."""
    # Aseguramos que 'mantenimientos' sea siempre una lista antes de usar 'append'
    if 'mantenimientos' not in datos:
        datos['mantenimientos'] = []
    
    nuevo_mantenimiento = {
        "matricula": matricula,
        "fecha": fecha,
        "servicio": servicio,
        "costo": costo
    }
    
    datos['mantenimientos'].append(nuevo_mantenimiento)
    print(f"Mantenimiento para la moto {matricula} registrado con éxito.")

def obtener_mantenimientos():
    """Retorna la lista de todos los mantenimientos registrados."""
    return datos.get('mantenimientos', [])