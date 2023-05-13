#While 2

edad = int(input("Digite su edad, por favor: "))

while edad<=0:
   
    print("Ha introducido una edad negativa o igual a cero: ",edad)
    edad=int(input("Digite su edad, por favor: "))
             
print("Gracias, introdujo edad positiva: "+str(edad))