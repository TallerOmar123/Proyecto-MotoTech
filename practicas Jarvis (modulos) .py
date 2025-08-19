#modulos : ramdon

import random
numero_aleatorio = random.randint (1, 10)
print(numero_aleatorio)

import random
cantidad_de_motos_del_taller = random.randint(1,20)
print(cantidad_de_motos_del_taller)

import random
dado = random.randint (1,6)
print(f"el resultado del lanzamiento del dado es: {dado}")

#parametro por defecto

def calcular_presupuesto(precio_repuesto, mano_de_obra=20) :
    total= precio_repuesto + mano_de_obra
    print(f"el presupuesto total es: {total} USD")
calcular_presupuesto(50)
calcular_presupuesto(50,30)

def cotizar_repuesto(precio_repuesto, costo_envio=10):
    costo_final=precio_repuesto+costo_envio
    print(f"el costo total del repuesto es: {costo_final} USD")
cotizar_repuesto(45)
cotizar_repuesto(45,25)


#argumentos de palabra clave

def generar_factura(cliente, fecha, total):
    print(f"factura para {cliente}, emitida el {fecha}, por un total de  {total }USD")
generar_factura (cliente= "omar", fecha="15/08/2025", total= 250 )
generar_factura ( fecha= "15/08/2025", total= 250, cliente= "omar")

#if anidado y bloque try... except

def calcular_descuento (precio_original, porcentaje_descuento):
    try:
        monto_descuento = precio_original * (porcentaje_descuento / 100) 
        precio_final = precio_original - monto_descuento
        if porcentaje_descuento > 0:
            return precio_final
        else:
            return "no se aplico ningun descuento"
    except (ValueError, TypeError):
        return "entrada invalida, asegurate de ingresar numeros"
calcular_descuento(100,10)
calcular_descuento(100," diez")
print(calcular_descuento(100,10))
print(calcular_descuento(100," diez"))


#ejercicio completo reuniendo todos los elementos
def calcular_presupuesto_completo (precio_repuesto, mano_de_obra, descuento=0):
    try:
        precio_total = precio_repuesto + mano_de_obra
        if descuento > 0:
            monto_descuento = precio_total * (descuento / 100)
            precio_total_final = precio_total - monto_descuento
            return precio_total_final
        else:
            return precio_total
    except(ValueError, TypeError):
        return "entrada invalida. Asegurate de ingresar numeros"
calcular_presupuesto_completo (50,20)
calcular_presupuesto_completo (precio_repuesto=50, mano_de_obra=20, descuento=10)
calcular_presupuesto_completo (50, "veinte", 10)
print(calcular_presupuesto_completo (50,20))
print(calcular_presupuesto_completo (precio_repuesto=50, mano_de_obra=20, descuento=10))
print(calcular_presupuesto_completo (50, "veinte", 10))


# 2do ejercicio completo de aplicacion de todos los elementos aprendidos
def calcular_calificacion_final (califacion_examen_escrito, calificacion_examen_oral, puntos_extras= 0):
    try:
        operacion_total = califacion_examen_escrito + (calificacion_examen_oral + puntos_extras)
        calificacion_final = operacion_total
        if calificacion_final > 100:
            calificacion_final = 100
            return calificacion_final
        else:
            return calificacion_final
            pass 
    except(ValueError, TypeError):
        return "entrada invalida. asegurate de ingresar numeros"
calcular_calificacion_final (50,40)
calcular_calificacion_final (califacion_examen_escrito= 50, calificacion_examen_oral= 40, puntos_extras= 15)
calcular_calificacion_final(50, "cuarenta", 10)
print(calcular_calificacion_final (50,40))
print(calcular_calificacion_final (califacion_examen_escrito= 50, calificacion_examen_oral= 40, puntos_extras= 15))
print(calcular_calificacion_final(50, "cuarenta", 10))


#3 ejercicio de aplicacion de todos los elementos aprendidos
def calcular_calificacion_final (califacion_examen_escrito, calificacion_examen_oral, puntos_extras=0):
    try:
        calificacion_final = califacion_examen_escrito + calificacion_examen_oral + puntos_extras
        if calificacion_final >100:
            calificacion_final = 100
            return calificacion_final
        else:
            return calificacion_final


    except(ValueError,TypeError):
        return "entrada invalida, asegurate de ingresar numeros"
calcular_calificacion_final (50,40)
calcular_calificacion_final (califacion_examen_escrito= 50,  calificacion_examen_oral= 40, puntos_extras = 15)
calcular_calificacion_final (50 , "cuarenta", 10)
print (calcular_calificacion_final (50,40))
print (calcular_calificacion_final (califacion_examen_escrito= 50,  calificacion_examen_oral= 40, puntos_extras = 15))
print (calcular_calificacion_final (50 , "cuarenta", 10))

#ejercicio 4 de reforzamiento

def calcular_descuento_cuenta (total_cuenta, porcentaje_descuento= 0):
    try:
        if total_cuenta >50:
            monto_descuento = total_cuenta * (porcentaje_descuento / 100)
            total_con_descuento = total_cuenta - monto_descuento
            return total_con_descuento
        else:
            return total_cuenta
    except (ValueError, TypeError):
        return "Error: por favor ingresar solo numeros"
calcular_descuento_cuenta (30)
calcular_descuento_cuenta (60,10)
calcular_descuento_cuenta("setenta", 10)
print(calcular_descuento_cuenta (30))
print(calcular_descuento_cuenta (60,10))
print(calcular_descuento_cuenta("setenta", 10))










