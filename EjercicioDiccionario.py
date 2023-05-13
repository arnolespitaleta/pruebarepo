#Ejercicio

#inicializo el diccionario
paises={}

pais = input("Introduce nombre de país: ")

#Bucle indeterminado while
while pais!="x":

    ciudad=input("Introduzca la ciudad perteneciente a ese país: ")

    lista_ciudades=paises.setdefault(pais,[ciudad])

    if lista_ciudades!=[ciudad]:
       
       paises[pais].append(ciudad)

    pais=input("Introduce el país:")

print(paises)