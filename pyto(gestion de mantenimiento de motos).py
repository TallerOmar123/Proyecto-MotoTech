# proyecto = Gestión de Mantenimiento de Motos 
#Baase de datos de las motos que encuentro para hacer los respectivos mantenimientos
base_de_datos_de_motos= [
    {
        "modelo" : "Eco deluxe",
        "cilindraje" :  100,
        "intervalo" : 5000,
        "mantenimiento" : ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],


    },
    { 
        
        "modelo" : "Discover",
        "cilindraje" :  125,
        "intervalo" : 5000,
        "mantenimiento" : ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
        
    },
    {
        
        "modelo" : "Apache",
        "cilindraje" :  180,
        "intervalo" : 5000,
        "mantenimiento" : ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
        
    },
    { 
        
        "modelo" : "Suzuki Gixxer",
        "cilindraje" :  200,
        "intervalo" : 5000,
        "mantenimiento" : ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
        
    },
    {
        
        "modelo" : "Yamaha fz",
        "cilindraje" :  150,
        "intervalo" : 5000,
        "mantenimiento" : ["cambio de aceite", "revision de frenos", "lubricacion de guayas", "cambio de filtros", "revision de luces"],
        
    }
]

# agrego un diccionario vacio en este software para basicamente guardar en 
# el toda la informacion del usuario que se me entegara en el input de los 
#datos para poder ejecutar el programa
base_de_datos_de_cliente = {}


        
#Ahora la tarea es definir una funcion que me muestre los modelos de motos 
# disponibles que tengo en este programa.
#nota: los parentesis vacios indican que no necesito ningun argumento
def listar_motos ():
    print("Los diferentes modelos de motos disponibles son:")
    for moto in base_de_datos_de_motos:
        print(f" - {moto['modelo']}")



#ahora creo otra funcion que me permita recorrer la moto en base de datos
#con el input que me entregue el cliente
def buscar_moto_por_modelo(modelo_a_buscar):
    for moto_encontrada in base_de_datos_de_motos:
        if moto_encontrada['modelo'].lower() == modelo_a_buscar.lower():
            return moto_encontrada
    return None 

#creo una funcion que me permite recibir los datos de mi cliente, y ademas 
#agrego un diccionario para trabajar desde un bloque que pueda manejar mejor
#por ultimo agrego este diccionario a la basde de datos del cliente
def registrar_cliente():
    solicitud_de_datos_nombre = input("Por favor agrega tu nombre:")
    solicitud_de_datos_telefono = input("Por favor agrega tu numero de telefono:")
    solicitud_de_datos_modelo_moto = input("Por favor agrega el modelo de tu moto:")
    nuevo_cliente = {
    
        "nombre_cliente" : solicitud_de_datos_nombre,
        "telefono_cliente" : solicitud_de_datos_telefono,
        "modelo_moto" : solicitud_de_datos_modelo_moto,
        "historial_mantenimientos" : []
    }
    base_de_datos_de_cliente[solicitud_de_datos_nombre] = nuevo_cliente
    print("Gracias por la informacion, tus datos han sido registrados")
#Nota: la diferencia de esta solicitud de nombre en este caso es el registro del cliente. pues aqui estoy guardando en base de datos
#de cliente. bajo la etiqueta nuevo cliente. pero en registrar mantenimiento utilizo el nombre que ya ha sido registrado en registrar
# cliente, esa es la diferencia de los dos, basicamente uno se liga con el otro

def registrar_mantenimiento():
    solicitud_de_datos = input("por favor escribe aqui tu nombre:").strip() .lower()
    if solicitud_de_datos in base_de_datos_de_cliente:
        solicitud_kilometraje_actual = input("Por favor escribe el kilometraje de tu moto")
        solicitud_costo_servicio = input("Por favor, escribe el costo del servicio")
        solicitud_descripcion_trabajo_realizado = input("coloca aqui el trabajo que se le ha realizado a tu moto")
        nuevo_mantenimiento = {
            "kilometraje" : solicitud_kilometraje_actual,
            "costo" : solicitud_costo_servicio,
            "descipcion" : solicitud_descripcion_trabajo_realizado
        }
        cliente_encontrado = base_de_datos_de_cliente[solicitud_de_datos] #esta primera linea tiene una variable que guarda en base
#de datos de cliente, garda todo el diccionario que relaciona registrar mantenimiento.
        cliente_encontrado ['historial_mantenimientos'].append (nuevo_mantenimiento) #aqui es diferente pues no hay una variable que 
# guarda en base de datos, es una modificacion con append en el deccionario que habia dejado abierto en nuevo cliente... historial
#mantenimientos
        print("!felicidades, has sido encontrado!")
    else:
        print("lo siento, no hemos encontrado tu usuario")

def ver_historial_mantenimientos():
    solicitud_nombre_cliente = input("Pr favor, escribe tu nombre para poder buscar la informacion de tu moto")
    if solicitud_nombre_cliente in base_de_datos_de_cliente:
        cliente_encontrado = base_de_datos_de_cliente[solicitud_nombre_cliente]
        historial = cliente_encontrado['historial_mantenimientos']
        if historial: # Verificamos si la lista no está vacía
            print(f"\nHistorial de mantenimientos para {solicitud_nombre_cliente.title()}:")
            for servicio in historial:
                print("---")
                for clave, valor in servicio.items():
                    print(f"  {clave.title()}: {valor}")
            print("---")
        else:
            print("Este cliente no tiene mantenimientos registrados.") 
        
        
    else:
        print("Lo siento, no encontramos este usuario")




#aqui es la parte donde creo el esqueleto del porgrama... para ir dando una 
#mejor estructura

while True:
    print("\n !Bienvenido a MotoTech!")
    print("1. ver modelos de motos")
    print("2. buscar una moto por modelo")
    print("3. registrar un nuevo cliente")
    print("4. salir")
    opcion = input("Por favor selecciona una opcion:").lower().strip()

    if opcion == "1":
        listar_motos() ##aqui empiezo a dar logica al programa
    elif opcion == "2":
        modelo_buscado = input("Por favor ingresa el modelo de tu moto:").strip() .lower() #aqui hago una llamada a 
#la funcion de buscar modelo con un input
        moto_ya_econtrada = buscar_moto_por_modelo(modelo_buscado)   #luego creo otra variable en el que guardo en retorno de 
#la operacion cuando llamo a la funcion
        if moto_ya_econtrada:
            print("!Moto encontrada¡ aqui estan los detalles")
            for clave, valor in moto_ya_econtrada.items():
                print(f"\n{clave} : {valor}")
        else:
            print("lo siento, no hemos podido encontrar tu modelo de moto")
    elif opcion == "3":
        registrar_cliente()
    elif opcion == "4":
        print("!Gracias por usar MotoTech! hasta pronto")
        break # este comando finaliza el bucle
    else:
        print("opcion no valida, por favor intenta de nuevo ")








