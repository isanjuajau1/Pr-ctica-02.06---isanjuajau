#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o 
#un mensaje de aviso si la divisa no está en el diccionario.

Divisa = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
Usuario = input("Introduce una ")
if Usuario.title() in Divisa:
    print(Divisa[Usuario.title()])
else:
    print("La divisa no se encuentra")