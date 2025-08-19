

productos=["manzanas", "pan", "leche"]
precios= [2.5, 3.0, 1.5]
costo_total=0.0
print("el producto manzana cuesta 2.5")
print("el producto pan cuesta 3.0")
print("el producto leche cuesta 1.5")

for elementos in precios:
    costo_total+=elementos
print(f"el costo total de la compra es {costo_total}")

productos= ["manzanas", "pan", "leche"]
precios = [2.5, 3.0, 1.5]
costo_total=0.0
for elementos, valores in zip (productos, precios):
    costo_total+=valores
print(costo_total)

producto= ["manzanas", "pan", "leche"]
precio= [2.5, 1.8, 3.2]
for producto,precio in zip (producto,precio):
    print(f"el precio de {producto} es ${precio}")


moto= ["yamaha", "suzuki", "honda"]
valor = [9.5, 7.2, 6.7]
for moto,valor in zip (moto,valor):
    print(f" la moto {moto} tiene el siguiente valor {valor}") 



carro = [ "mazda", "mercedez", "peugeot"]
valor = [10.5, 15.3 , 16,8]
for carro,valor in zip (carro,valor): 
    print(f"el carro {carro} tiene un valor de {valor}")

productos= ["manzanas", "pan", "leche", "huevos"]
precios= [2.5, 1.8, 3.2, 4.5]
stock= [10, 5, 20, 8]
for productos, precios, stock in zip (productos,precios,stock):
    print(f"tenemos {stock} de {productos} que cuestan {precios} cada una")


 #comprension de listas
precios_locales = [10.5 , 15.3, 20.5, 12.4]
resultado_factor_conversion =[]
for precio in precios_locales:
    resultado_factor_conversion. append (precio * 0.87)
print(resultado_factor_conversion)


# crea un codigo que me muestre el valor de una moto multiplicado 
#por dos usando un bucle 
valor_moto=[1.5, 10.3, 16.5]
valor_final =[]
for valor in  valor_moto:
    valor_final.append(valor*2)
print(valor_final)

valor_moto = [1.5, 10.3, 16.5]
valor_final= [valor*2 for valor in valor_moto]
print(valor_final)


precios_locales = [10.5 , 15.3, 20.5, 12.4]
resultado_factor_conversion =[]
for precio in precios_locales:
    resultado_factor_conversion. append (precio * 0.87)
print(resultado_factor_conversion)

precios_locales = [10.5 , 15.3, 20.5, 12.4]
resultado_factor_conversion=[precio*0.87 for precio in precios_locales]
print(resultado_factor_conversion)


precios_repuestos = [5.5, 12.0, 8.5, 15.0, 9.9, 21.5]
precios_mayores_10 = [precio for precio in precios_repuestos if precio > 10.0]
print(f"los precios mayores a 10 son {precios_mayores_10}")





marca_moto ="yamha"
modelo ="MT-07"
cilindrada_cc = 689
print(f" la moto {marca_moto} {modelo} tiene una cilindrad de {cilindrada_cc}")


repuestos = ["filtro_aire","bujia", "pastillas_freno", "cadena"]
for repuesto_moto in repuestos:
    print(f"necesito comprar un repuesto que diga: {repuesto_moto}")

#hasta aqui con jarvis he visto:
#Variable y tipos de datos, listas, bucles for, funcion zip() 


#Ejercicio usando for y zip
repuestos = ["filtro_aire","bujia", "pastillas_freno", "cadena"] 
precios = [25.5, 12.0, 45.75, 80.0]
for repuestos, precios in zip(repuestos, precios):
    print(f"el precio de {repuestos} is {precios}")


repuestos = ["filtro_aire","bujia", "pastillas_freno", "cadena"] 
precios = [25.5, 12.0, 45.75, 80.0]   
stock=[ 5,10,2,8]
for repuestos, precios, stock in zip (repuestos, precios, stock):
    print(f"del repuesto {repuestos}, tenemos {stock} unidades a un precio de {precios} cada una")
    

#ejercicio usando coprension delistas
precios = [25.5, 12.0, 45.75, 80.0]  
precios_promocion =[precio * 2 for precio in precios]
print(precios_promocion)

#ejercicio 2 usando comprension de listas
precios_nuevos = [15.0, 22.5, 5.0, 30.0,  18.0]
precios_descuento = [precio for precio in precios_nuevos if precio < 20.0]
print(precios_descuento)

#ejercicio 4, comprension de lista
precios = [25.5, 12.0, 45.75, 80.0] 
precios_con_iva = [precio *1.16 for precio in precios]
print(precios_con_iva)

