class Persona:
    #self hace referencia a la clase actual, es decir a la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def caminar(self):
        print(f"{self.nombre} está caminando")

    def correr(self):
        print(f"{self.nombre} está corriendo")

    #Método __str__ definido por defecto en Python
    #en este caso para la clase persona retornar
    #una cadena de texto y mostrar toda la información
    #relacionada a la misma clase
    def __str__(self):
        return f"La persona se llama: {self.nombre} y su edad es: {self.edad}"

#Le asigno valores, para construir mi objeto desde el método init    
persona = Persona("Arnol Espitaleta", 40)
persona1 = Persona("Diana", 35)
persona2 = Persona("Leonardo", 45)
print(persona)
print(persona1)
print(persona2)

#Accedo a un comportamiento de persona, en este caso cuando camina
persona.caminar()
persona1.caminar()
persona2.caminar()


#Accedo a un comportamiento de persona, en este caso cuando corre
persona.correr()
persona1.correr()
persona2.correr()

print(persona.nombre)
print(persona.edad)

print(persona1.nombre)
print(persona1.edad)


print(persona2.nombre)
print(persona2.edad)