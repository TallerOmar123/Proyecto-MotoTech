#Proyecto: Calculadora de Mantenimiento y Costos
#-- Base de Datos --
#Base de datos (mi codigo original)
base_de_datos_de_motos =[
    {
        "modelo" : "discover 125",
        "mantenimiento" : ["cambio de aceite", "revision de frenos","cambio filtro de aire"],
        "intervalo" : 5000,
        "tipo_aceite" : "mobile 20w50",
        "cilindraje" : "125"
    },
    {
        "modelo" : "eco deluxe",
        "mantenimiento" : ["cambio de aceite", "revision de frenos","cambio filtro de aire"],
        "intervalo" : 5000,
        "tipo_aceite" : "GP 20w50",
        "cilindraje" : "100"
    },
    {
        "modelo" : "hunk 160 r",
        "mantenimiento" : ["cambio de aceite", "revision de frenos","cambio filtro de aire"],
        "intervalo" : 5000,
        "tipo_aceite" : "shell 10w30",
        "cilindraje" : "160"
    },
    {
        "modelo" : "apache 180",
        "mantenimiento" : ["cambio de aceite", "revision de frenos","cambio filtro de aire"],
        "intervalo" : 5000,
        "tipo_aceite" : "castrol 10w40",
        "cilindraje" : "180"
    }
]


# --- Base de datos de cliente ---(variable global)
base_de_datos_de_clientes = {}



#---  Funciones ---

def listar_modelos():
#imprime una lista de los modelos de motos disponibles
    print("La lista de motos disponibles es:")
    for modelos_a_listar in base_de_datos_de_motos:
        print(f" - {modelos_a_listar['modelo']}")

def buscar_moto_por_modelo(modelo_a_buscar):
#busca y devuelva los datos de una moto po su modelo
    for moto in base_de_datos_de_motos:
        if moto["modelo"].strip()==modelo_a_buscar.strip():
            return moto
    return None

def calcular_costo_servicio(costo_repuesto, costo_mano_de_obra):
#calcula el costo total del servicio
    operacion_de_costos = costo_repuesto + costo_mano_de_obra
    return operacion_de_costos

def crear_cliente(nombre,  telefono, moto_asociada):
#crea un nuevo cliente y lo añade a la base de datos global
    nuevo_cliente = {
        "nombre" : nombre,
        "telefono" : telefono,
        "moto" : moto_asociada,
        "historial_mantenimientos": []
    }
#la clave del diccionario sera el nombre del cliente
    base_de_datos_de_clientes[nombre] = nuevo_cliente
    print(f"\n{nombre} ha sido agregado a la base de datos de clientes")



# --- Logica principal del programa --- 


print("Proyecto MotoTech: software para mecanicos")

ver_lista = input("deseas ver la lista de motos que tenemos disponibles? (si/no):")
if ver_lista.strip().lower() ==  "si":
    listar_modelos()

modelo_buscado = input("por favor ingresa el  modelo de la moto:")
moto_encontrada = buscar_moto_por_modelo(modelo_buscado)


if moto_encontrada:
    #1 . creamos y guardamos el cliente
    nombre_cliente = input("por favor ingresa tu nombre:")
    telefono_cliente = input("por favor ingresa tu numero de telefono:")
    crear_cliente (nombre_cliente, telefono_cliente, moto_encontrada)


    #2. revisamos el kilometraje
    try:
       solictud_kilometraje_actual  = int(input("ingresa el kilometraje actual de la moto:"))
       if solictud_kilometraje_actual >= moto_encontrada["intervalo"]:
            print(f"\n¡Alerta! es hora de realizar el mantenimiento de la {moto_encontrada["modelo"]}")
            print(f"\nlas tareas reomendadas son: {moto_encontrada["mantenimiento"]}")
            print(f"recuerda aplicar el aceite recomendado para este modelo de moto, el: {moto_encontrada["tipo_aceite"]}" )
       else:
            kilometraje_restante = moto_encontrada["intervalo"] - solictud_kilometraje_actual
            print(f"\nAun no es necesario realizar al mantenimiento")
            print(f"\nfaltan {kilometraje_restante} para el proximo servicio")
    except ValueError:
        print(f"/nEntrada invalida. Por favor, ingresa un numero valido para el kilometraje")

        
    # 3. calculamos los costos
    try:
        solicitud_costo_repuesto = float(input("\npor favor ingresa el costo del repuesto:"))
        solicitud_costo_mano_de_obra = float(input("por favor ingresa el costo de la mano de obra:"))
        costo_total_final = calcular_costo_servicio (solicitud_costo_repuesto,solicitud_costo_mano_de_obra )
        print(f"el costo total de servicio es: {costo_total_final}")
    except ValueError:
        print(f"\nEntrada invalida, por favor, ingresa solo numeros para los costos")
       
else:
    print(f"lo siento, el modelo '{modelo_buscado}' no se encontró ") 






        

    
    
   
   
   
   









