#Ejercicio lista


hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1:
hat_list[2] = int(input("Ingresa un numero entero: "))

# Paso 2:
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("\nLista con el ultimo elemento de la lista eliminado: ", hat_list)
print("\nEsta es la longitud de final de la lista: ",len(hat_list))