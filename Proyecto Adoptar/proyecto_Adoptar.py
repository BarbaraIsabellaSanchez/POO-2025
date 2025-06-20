class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.id = id
        
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "reservado", "adoptado"]:
            self.estado = nuevo_estado
            print("Estado actualizado")
        else:
            print("Estado inválido") 
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Estado salud: {self.estado_salud}")
        print(f"Vacunado: {self.vacunado}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")

class Adoptante:
    def __init__(self, nombre, dni, email, preferencias=None, historial_adopciones=None):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias if preferencias else {}
        self.historial_adopciones = historial_adopciones if historial_adopciones else []
        
    def actualizar_preferencias(self, raza=None, edad=None, tamaño=None):
        if raza:
            self.preferencias["raza"] = raza
        if edad:
            self.preferencias["edad"] = edad
        if tamaño:
            self.preferencias["tamaño"] = tamaño
        print("Preferencias actualizadas")
        
    def registrarse(self, apellido, telf):
        self.apellido = apellido
        self.telf = telf
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Teléfono: {self.telf}")
    
    def modificar_datos(self, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_email, nuevo_telf, nueva_preferencia):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        self.dni = nuevo_dni
        self.email = nuevo_email
        self.telf = nuevo_telf
        self.preferencias = nueva_preferencia
        print("Datos actualizados correctamente")
    
    def mostrar_datos_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telf}")
        print(f"Preferencias: {self.preferencias}")
        if self.historial_adopciones:
            print("Perros adoptados:")
            for perro in self.historial_adopciones:
                print(perro.nombre, perro.raza)
        else:
            print("Aún no ha adoptado ningún perro")
    
    def ver_historial(self):
        return self.historial_adopciones

class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []
        
    def cargar_perro(self, nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"Perro cargado: {nuevo_perro.nombre}")
        
    def eliminar_perro(self, id):
        for perro in self.perros:
            if perro.id == id:
                self.perros.remove(perro)
                print("Perro eliminado")
                return
        print("Perro no encontrado")
    
    def registrar_usuario(self, nuevo_usuario):
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario registrado: {nuevo_usuario.nombre}")
    
    def postular_a_perro(self, usuario, perro):
        if perro.estado == "disponible":
            perro.cambiar_estado("reservado")
            usuario.historial_adopciones.append(perro)
            print(f"{usuario.nombre} ha postulado a {perro.nombre}")
        else:
            print(f"{perro.nombre} no está disponible para adopción")
    
    def confirmar_adopcion(self, usuario, perro):
        if perro in usuario.historial_adopciones:
            perro.cambiar_estado("adoptado")
            print(f"{usuario.nombre} ha adoptado a {perro.nombre}")
        else:
            print(f"{usuario.nombre} no ha postulado a {perro.nombre}")
    
    def sugerir_perros(self, usuario):
        sugerencias = []
        for perro in self.perros:
            if (perro.estado == "disponible" and
                (perro.raza in usuario.preferencias.get("raza", []) or
                 perro.edad in usuario.preferencias.get("edad", []) or
                 perro.tamaño in usuario.preferencias.get("tamaño", []))):
                sugerencias.append(perro)
        return sugerencias
    
    def mostrar_listados(self, estado=None):
        if estado:
            perros_filtrados = [perro for perro in self.perros if perro.estado == estado]
            print(f"Perros en estado '{estado}':")
            for perro in perros_filtrados:
                perro.mostrar_informacion()
        else:
            print("Todos los perros disponibles:")
            for perro in self.perros:
                perro.mostrar_informacion()
                print("Este perrito ha contado su historia. Ahora, otro lo hará.")
