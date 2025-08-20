#Proyecto: Calculadora de Mantenimiento y Costos

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
def listar_modelos():
    print("La lista de motos disponibles es:")
    for modelos_a_listar in base_de_datos_de_motos:
        print(f" - {modelos_a_listar['modelo']}")
def buscar_moto_por_modelo(modelo_a_buscar):
    for moto in base_de_datos_de_motos:
        if moto["modelo"].strip()==modelo_a_buscar.strip():
            return moto
    return None
def calcular_costo_servicio(costo_repuesto, costo_mano_de_obra):
    operacion_de_costos = costo_repuesto + costo_mano_de_obra
    return operacion_de_costos
ver_lista = input("deseas ver la lista de motos que tenemos disponibles? (si/no):")
if ver_lista.strip().lower() ==  "si":
    listar_modelos()
modelo_buscado = input("por favor ingresa el  modelo de la moto:")
moto_encontrada = buscar_moto_por_modelo(modelo_buscado)
if moto_encontrada:
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
    try:
        solicitud_costo_repuesto = float(input("\npor favor ingresa el costo del repuesto:"))
        solicitud_costo_mano_de_obra = float(input("por favor ingresa el costo de la mano de obra:"))
        costo_total_final = calcular_costo_servicio (solicitud_costo_repuesto,solicitud_costo_mano_de_obra )
        print(f"el costo total de servicio es: {costo_total_final}")
    except ValueError:
        print(f"\nEntrada invalida, por favor, ingresa solo numeros para los costos")
       
else:
    print(f"lo siento, el modelo '{modelo_buscado}' no se encontró ") 


#este es un código que acabo de crear desde el teléfono 





        

    
    
   
   
   
   









