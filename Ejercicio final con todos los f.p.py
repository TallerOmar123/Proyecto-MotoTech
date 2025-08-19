mantenimientos=  [
    {
        "moto":  "hero 190",
        "tarea": "cambio de aceite",
        "completada" : True,
        "precio": 5


    },
    {
        "moto":  "suzuki gixxer",
        "tarea": "cambiar kit de arrastre",
        "completada" : True,
        "precio": 20
    },
    {
        "moto":  "yamaha crypton",
        "tarea": "cambio de pastillas",
        "completada" :  False,
        "precio": 5
    },
    {
        "moto":  "apache 200",
        "tarea": "reparacion del motor",
        "completada" : True,
        "precio": 100
    }
]
total_pendientes=0
for tareas_de_mantenimiento in mantenimientos:
    if tareas_de_mantenimiento ["completada"] == False:
        total_pendientes=  total_pendientes + tareas_de_mantenimiento ["precio"]
        print(f"Pendiente: {tareas_de_mantenimiento['tarea']} para la moto {tareas_de_mantenimiento['moto']}. Costo estimado: {tareas_de_mantenimiento['precio']} USD")
     
print(f"costo total de tareas pendientes: {total_pendientes} USD")


#2do ejercicio:

ventas= [
    { 
        "repuesto" : "bujia",
        "precio_venta" : 5,
        "precio_costo" : 2,
        "cantidad" : 5
    },
    {
        "repuesto" : "bandas",
        "precio_venta" : 15,
        "precio_costo" : 10,
        "cantidad" : 10
    },
    {
        "repuesto" : "pastilas",
        "precio_venta" : 13,
        "precio_costo" : 8,
        "cantidad" : 15
    },
    {
        "repuesto" : "guayas",
        "precio_venta" : 2,
        "precio_costo" : 1,
        "cantidad" : 20
    }
]
total_ingresos = 0
total_ganancias = 0
for repuesto in ventas:
    ingreso_por_venta = repuesto["precio_venta"] * repuesto["cantidad"]
    ganancia_por_venta = (repuesto["precio_venta"] - repuesto["precio_costo"]) * repuesto["cantidad"]
    if ganancia_por_venta  > 0:
        total_ingresos = ingreso_por_venta + total_ingresos 
        total_ganancias = ganancia_por_venta + total_ganancias
print(f"total ingresos por ventas: {total_ingresos} USD")
print(f"ganancia neta total: {total_ganancias} USD")