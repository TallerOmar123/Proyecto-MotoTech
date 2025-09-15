import json

# Variable global para guardar los datos cargados del archivo
datos = {}

# Base de datos de las motos
base_de_datos_de_motos = [
    {
        "modelo": "Eco deluxe",
        "cilindraje": 100,
        "intervalo": 5000,
        "mantenimiento": ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
    },
    {
        "modelo": "Discover",
        "cilindraje": 125,
        "intervalo": 5000,
        "mantenimiento": ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
    },
    {
        "modelo": "Apache",
        "cilindraje": 180,
        "intervalo": 5000,
        "mantenimiento": ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
    },
    {
        "modelo": "Suzuki Gixxer",
        "cilindraje": 200,
        "intervalo": 5000,
        "mantenimiento": ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
    },
    {
        "modelo": "Yamaha fz",
        "cilindraje": 150,
        "intervalo": 5000,
        "mantenimiento": ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
    }
]

# Diccionario para guardar la información del cliente
base_de_datos_de_cliente = {}

def listar_motos():
    print("Los diferentes modelos de motos disponibles son:")
    for moto in base_de_datos_de_motos:
        print(f" - {moto['modelo']}")

def buscar_moto_por_modelo(modelo_a_buscar):
    for moto_encontrada in base_de_datos_de_motos:
        if moto_encontrada['modelo'].lower() == modelo_a_buscar.lower():
            return moto_encontrada
    return None

def registrar_cliente():
    solicitud_de_datos_nombre = input("Por favor, agrega tu nombre:").strip().lower()
    solicitud_de_datos_telefono = input("Por favor, agrega tu numero de telefono:")
    solicitud_de_datos_modelo_moto = input("Por favor, agrega el modelo de tu moto:")
    nuevo_cliente = {
        "nombre_cliente": solicitud_de_datos_nombre,
        "telefono_cliente": solicitud_de_datos_telefono,
        "modelo_moto": solicitud_de_datos_modelo_moto,
        "historial_mantenimientos": []
    }
    base_de_datos_de_cliente[solicitud_de_datos_nombre] = nuevo_cliente
    print("Gracias por la informacion, tus datos han sido registrados.")

def registrar_mantenimiento(matricula, fecha, servicio, costo):
    # Primero buscamos si la moto ya existe
    # Como tu base de datos no tiene matrículas, usaremos un ejemplo
    # para ilustrar la lógica.
    mantenimientos = datos.get('mantenimientos', {})
    if matricula not in mantenimientos:
        mantenimientos[matricula] = []
    
    nuevo_mantenimiento = {
        "matricula": matricula,
        "fecha": fecha,
        "servicio": servicio,
        "costo": costo
    }
    mantenimientos[matricula].append(nuevo_mantenimiento)
    datos['mantenimientos'] = mantenimientos
    
    print("Mantenimiento registrado con éxito.")

def ver_historial_mantenimientos():
    solicitud_nombre_cliente = input("Por favor, escribe tu nombre para poder buscar la informacion de tu moto:").strip().lower()
    if solicitud_nombre_cliente in base_de_datos_de_cliente:
        cliente_encontrado = base_de_datos_de_cliente[solicitud_nombre_cliente]
        historial = cliente_encontrado['historial_mantenimientos']
        if historial:
            print(f"\nHistorial de mantenimientos para {solicitud_nombre_cliente.title()}:")
            for servicio in historial:
                print("---")
                for clave, valor in servicio.items():
                    print(f"  {clave.title()}: {valor}")
            print("---")
        else:
            print("Este cliente no tiene mantenimientos registrados.")
    else:
        print("Lo siento, no encontramos este usuario.")

def guardar_datos():
    """Guarda los datos de los clientes en un archivo."""
    with open('mototech_datos.json', 'w') as archivo:
        json.dump(base_de_datos_de_cliente, archivo, indent=4)
    print("Datos guardados con éxito en 'mototech_datos.json'.")

def cargar_datos():
    """Carga los datos de un archivo, si existe."""
    try:
        with open('mototech_datos.json', 'r') as archivo:
            datos = json.load(archivo)
            global base_de_datos_de_cliente
            base_de_datos_de_cliente = datos
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Se iniciará con datos vacíos.")

def obtener_mantenimientos():
    mantenimientos_totales = {}
    for cliente in base_de_datos_de_cliente.values():
        for mantenimiento in cliente.get('historial_mantenimientos', []):
            mantenimientos_totales.append(mantenimiento)
    return list(mantenimientos_totales)

# Aquí es la parte donde creamos el esqueleto del programa
if __name__ == '__main__':
    cargar_datos() # Cargar datos al inicio del programa de consola
    while True:
        print("\n ¡Bienvenido a MotoTech!")
        print("1. ver modelos de motos")
        print("2. buscar una moto por modelo")
        print("3. registrar un nuevo cliente")
        print("4. registrar mantenimiento")
        print("5. ver historial de mantenimientos")
        print("6. salida")
        opcion = input("Por favor selecciona una opcion:").lower().strip()

        if opcion == "1":
            listar_motos()
        elif opcion == "2":
            modelo_buscado = input("Por favor ingresa el modelo de tu moto:").strip().lower()
            moto_ya_econtrada = buscar_moto_por_modelo(modelo_buscado)
            if moto_ya_econtrada:
                print("¡Moto encontrada! Aquí están los detalles:")
                for clave, valor in moto_ya_econtrada.items():
                    print(f"\n{clave} : {valor}")
            else:
                print("Lo siento, no hemos podido encontrar tu modelo de moto.")
        elif opcion == "3":
            registrar_cliente()
        elif opcion == "4":
            registrar_mantenimiento()
        elif opcion == "5":
            ver_historial_mantenimientos()
        elif opcion == "6":
            guardar_datos() # Guardar los datos antes de salir
            print("¡Gracias por usar MotoTech! Hasta pronto.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

