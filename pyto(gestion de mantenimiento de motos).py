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
        if moto_encontrada['modelo'] == modelo_a_buscar:
            return moto_encontrada
    return None 





#aqui empiezo a dar logica al programa
listar_motos()
#en la llamda a la funcion "buscar moto por modelo" primero coloco un input
modelo_buscado = input("Por favor ingresa el modelo de tu moto")
#despues llamo a la funcion
buscar_moto_por_modelo(modelo_buscado)
#luego creo otra variable en el que guardo en retorno de la operacion cuando llamo a la funcion
moto_ya_econtrada = buscar_moto_por_modelo (modelo_buscado)
if moto_ya_econtrada:
    print("hemos encontrado tu  modelo de moto")
else:
    print("lo siento, no hemos podido encontrar tu modelo de moto")

