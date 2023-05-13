#Trabajando con excepciones

#Funciones de operaciones básicas (para sumar, restar, multiplicar y dividir)
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por cero: 0, simboliza infinito")
        return("Error en la operación")
#Capturo de usuario los datos para operar
# Y qué tipo de operación

numero1=int(input("Introduzca primer número: "))
numero2=int(input("Introduzca segundo número: "))

#Leo que tipo de operación escoge el usuario
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División

operacion=int(input("Escoja Operación: (1). Suma, (2). Resta" +
                    " (3). Multiplicación, (4). División: , (5). Sálida ..."))

match operacion:
    case 1:
        print('Suma es: ',suma(numero1, numero2))
    case 2:
        print('Resta es: ',resta(numero1, numero2))
    case 3:
        print('Multiplicación es: ',multiplica(numero1, numero2))
    case 4:
        print('Divide es: ',divide(numero1, numero2))
    case 5:
        print('Ha salido ... ')
        exit