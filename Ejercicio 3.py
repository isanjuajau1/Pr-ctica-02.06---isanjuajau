#Escribir un programa que guarde en un diccionario los precios de los artículos 
#de la tabla, pregunte al usuario por un artículo, un número de unidades y 
#muestre por pantalla el precio de esa cantidad de producto. Si el producto no 
#está en el diccionario debe mostrar un mensaje informando de ello.
precios = {"Pan":1.35 , "Huevos":2.25 , "Cebolla":0.80 , "Aceite":4.55}
articulo = input("Dime el articulo ")
cantidad = int(input("Dime la cantidad "))
if articulo in precios:
    print(cantidad, 'de', articulo, 'valen', precios[articulo]*cantidad, '€')
else: 
    print("No esta disponible ")