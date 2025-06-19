class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def presentarse(self):
        return f"Hola, soy {self.nombre}, un {self.especie}."

class Perro(Animal):
    def ladrar(self):
        return "¡Guau! ¡Guau!"
class Gato(Animal):
    def maullar(self):
        return "¡Miau! ¡Miau!"
    