"""Diccionarios y bucles
Crear un diccionario que tenga países y capitales
"""

capitales = {"Colombia":"Bogotá", "Canadá":"Ottawa", "Estados Unidos":"Washington DC", "Uruguay":"Montevideo"}

#Bucle determinado for
for clave in capitales:

    #si deseo recorrer claves y valores. Agrego
    #lo siguiente valor=capitales[clave]
    valor=capitales[clave]
    print(clave)
    print(valor)

print(capitales.items())