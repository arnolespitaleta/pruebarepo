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
        return f"La persona se llama{self.nombre} y su edad es {self.edad}"