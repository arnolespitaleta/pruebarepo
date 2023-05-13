class Usuario:
    #self hace referencia a la clase actual, es decir a la clase Usuario
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def registrar(self):
        print(f"El usuario: {self.nombre} ha sido registrado")

    #Método __str__ definido por defecto en Python
    #en este caso para la clase persona retornar
    #una cadena de texto y mostrar toda la información
    #relacionada a la misma clase
    def __str__(self):
        return f"El usuario se llama: {self.nombre} y su edad es: {self.edad}"

#Le asigno valores, para construir mi objeto desde el método init    
usuario = Usuario("Arnol Espitaleta", 40)

print(usuario)

#Accedo a un comportamiento de un usuario, en este caso cuando es registrado
usuario.registrar()

#Ejemplo de la herencia con subclases
class Cliente(Usuario):
    def __init__(self, nombre, edad, numero_compras):
        Usuario.__init__(self, nombre, edad)
        #tambien se podría
        super().__init__(nombre,edad)
        self.numero_compras = numero_compras


cliente = Usuario('Dell', 65)
cliente.registrar()

class Vendedor(Usuario):
    pass

vendedor = Vendedor("Andrea", 28)
vendedor.registrar()