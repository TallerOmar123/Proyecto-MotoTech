import random 
def obtener_nombre_jugador():
    while True:
        nombre=input ("hola, ¿Cuál es tu nombre?")
        if nombre.strip():
           return nombre
        else:
            print("por favor introduce un mombre este espacio no puede estar vacio")
def elegir_dificultad():
    while True:
            print("\n--- selecciona un nivel de dificultad ---")
            print("1. facil (1-10)")
            print("2. medio (1-50)")
            print("3. dificil (1-100)")
            eleccion = input ("introduce el numero de tu eleccion (1,2 o 3): ")
            if eleccion == '1':
              return 1,10
            elif eleccion =='2':
              return 1,50
            elif eleccion == '3': 
              return 1,100
            else:
               print("!opcion no valida! por favor elige 1,2 o 3")

def jugar_adivinanza():
    nombre_jugador=obtener_nombre_jugador()
    print(f"/n!Bienvenido, {nombre_jugador}! vamos a jugar a adivinar el numero secreto")
    
    min_num, max_num= elegir_dificultad()
    numero_secreto = random.randint(min_num, max_num)
    intentos = 0

    print(F"\nEstoy pensando en un numero entre {min_num} y {max_num}. intenta adivinarlo")

 
    while True:
     try:
        suposicion= int(input("introduce tu numero"))
        intentos +=1
        if suposicion <min_num or suposicion> max_num:
            print(f"tu numero esta fuera del rango. !intenta un numero entre {min_num} y {max_num}")
        elif suposicion<numero_secreto:
            print("demaciado bajo, intenta con un numero mas grande")
        elif suposicion> numero_secreto:
            print("demaciado alto, intenta con un numero mas pequeño")
        else:
            print((f"/n!felicidades¡, {nombre_jugador}adivinaste el numero{numero_secreto} en {intentos})intentos"))
        break 

       
     except ValueError:
            print("entrada no valida. por favor, introduce un numero entero.")

def main():
        while True:
            jugar_adivinanza()
            repuesta_jugar_de_nuevo= input("\n¿quieres jugar de nuevo?(si/no):").lower()
            if repuesta_jugar_de_nuevo=='no' and repuesta_jugar_de_nuevo== 'si':
             print(f"¡gracias por jugar! hasta la proxima, amigable adivinador!")
            break
            
if __name__ == "__main__":
    main()
        

for ingredientes_de_cocina in cocina("arroz", "azucar","frijoles"):
    print(ingredientes_de_cocina)



