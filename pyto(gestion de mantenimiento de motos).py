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

# agrego un diccionario vacion en este software para basicamente guardar en 
# el toda la informacion del usuario que se me entegara en el input de los 
#datos para poder ejecutar el programa
base_de_datos_de_cliente = {}

#Ahora la tarea es definir una funcion que me muestre los modelos de motos 
# disponibles que tengo en este programa.
#nota: los parentesis vacios indican que no necesoto ningun argumento
def listar_motos ():
    print("Los diferentes modelos de motos disponibles son:")
    for moto in base_de_datos_de_motos:
        print(f" - {moto['modelo']}")

listar_motos()