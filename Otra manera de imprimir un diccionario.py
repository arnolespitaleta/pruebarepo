#Otra manera de imprimir un diccionario
"""Diccionarios y bucles
Crear un diccionario que tenga países y capitales
"""

capitales = {"Colombia":"Bogotá", "Canadá":"Ottawa", "Estados Unidos":"Washington DC", "Uruguay":"Montevideo"}

#Bucle determinado for
#Otra forma de imprimir un diccionario
for clave,valor in capitales.items():

    #Para imprimir puedo concatenar el contenido
    #del diccionario para diferenciar. Ejemplo "->"
    print(clave + " -> " + valor)