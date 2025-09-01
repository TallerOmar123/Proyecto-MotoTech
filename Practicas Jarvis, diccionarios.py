mi_moto = {
    "marca" : "honda",
    "modelo" : "CB500f",
    "anio" : 2023
   
}


print(mi_moto["anio"])
mi_moto  ["anio"] = 2024
print(mi_moto["anio"])


catalogo_motos = [
    {
        "marca" : "Yamaha",
        "modelo" : "ybr 125",
        "precio" : 13

    },
    {
        "marca" : "Suzuki",
        "modelo" : "gixxer",
        "precio" : 15
    },
    {    
        "marca" : "Honda",
        "modelo" : "Wave",
        "precio" : 10
        
    }
]
for moto in catalogo_motos:
    print(f"la {moto ["marca"]} {moto["modelo"]} tiene un precio de {moto["precio"]} USD")


inventario = (
        {
            "nombre" : "filto de aceite",
            "marca" : "KyN",
            "stock" : 15
        },
        {
            "nombre" : "bujia",
            "marca" : "brembo",
            "stock" : 8
        },
        {
            "nombre" : "pastillas de freno",
            "marca" : "brembo",
            "stock" : 8
        }
    )
for repuesto in inventario:
        print(f"tenemos {repuesto["stock"]} unidades  de {repuesto["nombre"]}  de la marca {repuesto["marca"]}")


moto_cliente = {
    "marca" : "kawasaki",
    "modelo" : "ninja 400",
    "anio" : 2022
}      
moto_cliente ["color"]= "verde"
del moto_cliente ["anio"] 
print (moto_cliente)

#crea un diccionario que trate de repuestos de motos
repuestos_motos ={
    "carburador" : "sistema_alimentacion",
    "cadenilla" : "sistema_distribucion",
    "bandas" : "sistema de freno"
}
repuestos_motos["pastillas"]= "sistema de freno"
del repuestos_motos["cadenilla"]
print(repuestos_motos)


def calcular_iva(precio):
     precio_con_iva = precio  *1.16
     return precio_con_iva

precio_final = calcular_iva(100)
print(precio_final)


def calcular_costo_total(precio_moto, precio_accesorios):
    costo_general= precio_moto + precio_accesorios
    return costo_general
costo_total = calcular_costo_total(1000,500)
print(costo_total)

inventario =[
    {
        "nombre" : "bujia",
        "precio" : 12.0,
        "cantidad" : 10
    },
    {
        "nombre" : "carburador",
        "precio" : 20.0,
        "cantidad" : 5
    },
    {
        "nombre" : "bandas",
        "precio" : 15.0,
        "cantidad" : 20
    }
]
def calcular_valor_inventario (inventario):
    acumulador= 0
    for repuesto in inventario:
        valor_total = repuesto["precio"]*repuesto["cantidad"]
        acumulador= acumulador+valor_total
    return acumulador
resultado_final=calcular_valor_inventario (inventario)
print(f"el valor total del inventario es: {resultado_final} SD")


inventario= [
    {
        "nombre" : "filtro de aire",
        "cantidad" : 5,
        "precio" : 25.5
    },
    {
        "nombre" : "carburador",
        "cantidad" : 10,
        "precio" : 50
    },
    {
        "nombre" : "bandas",
        "cantidad" : 15,
        "precio" : 70
    }

]
for repuesto in inventario:
    if repuesto["cantidad"] <= 5:
        print(f"Alerta! el {repuesto ["nombre"]} esta bajo en stock. Cantidad actual: {repuesto ["cantidad"]} unidades")
    else:
        print(f"el repuesto {repuesto ["nombre"]} tiene un buen nivel de stock")


nivel_bateria = 75
if nivel_bateria >=80:
    print("la bateria esta en un nivel optimo")
elif nivel_bateria >= 40:
    print("la bateria tiene un nivel aceptable, considera cambiarla pronto")
elif nivel_bateria > 0:
    print("la bateria esta en un nivel muy bajo, es necesario cargarla")
else:
    print("la bateria esta completamente descargada")


#Ejercicios de flujo de control con bucles  while 
#El bucle se ejecutara mientras contador sea menor a 5

contador= 0
while contador <5:
    print(f"el contador es: {contador}")
    contador = contador +1


kms_recorridos = 0
while kms_recorridos  <= 5:
    print(f"hemos recorrido {kms_recorridos} kilometros")
    kms_recorridos = kms_recorridos+1


#Ejercicio con bucle for y con break y continue

repuestos= ["fitro de aceite", "cadena", "llanta", "fitro de aire"]
for repuesto in repuestos:
    if repuesto == "cadena":
        print("saltando el repueso cadena")
        continue
    print(f"revisando el repuesto : {repuesto}")

repuestos= ["fitro de aceite", "cadena", "llanta", "fitro de aire"]
for repuesto in repuestos:
    if repuesto == "llanta":
        print("saliendo del bucle despues de encontrar el repuesto llanta")
        break
    print(f"revisando el respuesto : {repuesto}")

    




