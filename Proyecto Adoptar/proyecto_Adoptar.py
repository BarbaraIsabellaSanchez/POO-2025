class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, id):
        # Datos básicos del perrito
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño  # "pequeño", "mediano", "grande"
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado  # "disponible", "reservado", "adoptado"
        self.temperamento = temperamento
        self.id = id

    def cambiar_estado(self, nuevo_estado):
        # Cambia el estado del perrito, si es válido
        if nuevo_estado in ["disponible", "reservado", "adoptado"]:
            self.estado = nuevo_estado
            print(f"Se ha cambiado el estado del perro a: {self.estado}")
        else:
            print("Estado no válido. Debe ser 'disponible', 'reservado' o 'adoptado'.")

    def mostrar_informacion(self):
        # Muestra todos los datos del perrito
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"Estado de salud: {self.estado_salud}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")
        print("Este perrito ha contado su historia. Ahora, otro lo hará.\n")


class Adoptante:
    def __init__(self, nombre, dni, email, preferencias=None, historial_adopciones=None):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias if preferencias else {}
        self.historial_adopciones = historial_adopciones if historial_adopciones else []

    def actualizar_preferencias(self, raza=None, edad=None, tamaño=None):
        # El usuario indica qué tipo de perrito busca
        if raza:
            self.preferencias["raza"] = raza
        if edad:
            self.preferencias["edad"] = edad
        if tamaño:
            self.preferencias["tamaño"] = tamaño

        print("Preferencias de adopción actualizadas.")

    def registrarse(self, apellido, telf):
        # Registro básico del usuario
        self.apellido = apellido
        self.telf = telf
        print(f"Registro completo: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telf}")

    def modificar_datos(self, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_email, nuevo_telf, nueva_preferencia):
        # Permite actualizar todos los datos personales del usuario
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        self.dni = nuevo_dni
        self.email = nuevo_email
        self.telf = nuevo_telf
        self.preferencias = nueva_preferencia

        print("Datos actualizados correctamente.")

    def mostrar_datos_usuario(self):
        # Muestra la info del adoptante y su historial
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telf}")
        print(f"Preferencias: {self.preferencias}")

        if self.historial_adopciones:
            print("Perros adoptados:")
            for perro in self.historial_adopciones:
                print(f"- {perro.nombre}, {perro.raza}")
        else:
            print("Aún no ha adoptado ningún perrito.")

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
                print("Perro eliminado correctamente.")
                return
        print("Perro no encontrado con ese ID.")

    def registrar_usuario(self, nuevo_usuario):
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario registrado: {nuevo_usuario.nombre}")

    def postular_a_perro(self, usuario, perro):
        if perro.estado == "disponible":
            perro.cambiar_estado("reservado")
            usuario.historial_adopciones.append(perro)
            print(f"{usuario.nombre} ha postulado a {perro.nombre}.")
        else:
            print(f"{perro.nombre} no está disponible en este momento.")

    def confirmar_adopcion(self, usuario, perro):
        if perro in usuario.historial_adopciones:
            perro.cambiar_estado("adoptado")
            print(f"{usuario.nombre} ha adoptado oficialmente a {perro.nombre}.")
        else:
            print(f"{usuario.nombre} no ha postulado a {perro.nombre} aún.")

    def sugerir_perros(self, usuario):
        sugerencias = []
        for perro in self.perros:
            if perro.estado == "disponible":
                if (
                    perro.raza in usuario.preferencias.get("raza", []) or
                    perro.edad in usuario.preferencias.get("edad", []) or
                    perro.tamaño in usuario.preferencias.get("tamaño", [])
                ):
                    sugerencias.append(perro)
        return sugerencias

    def mostrar_listados(self, estado=None):
        if estado:
            perros_filtrados = [perro for perro in self.perros if perro.estado == estado]
            print(f"Perros en estado '{estado}':")
            for perro in perros_filtrados:
                perro.mostrar_informacion()
        else:
            print("Todos los perritos disponibles:")
            for perro in self.perros:
                perro.mostrar_informacion()

if __name__ == "__main__":
   
    sistema = SistemaAdopcion()

    # añadi algunos perritos al sistema para probarlo
    perro1 = Perro("Toby", "Labrador", 3, "grande", 30, "Sano", True, "disponible", "Juguetón", 1)
    perro2 = Perro("Luna", "Caniche", 5, "pequeño", 7, "Sano", True, "disponible", "Tranquila", 2)
    perro3 = Perro("Rex", "Ovejero", 2, "grande", 28, "Sano", False, "disponible", "Guardia", 3)

    sistema.cargar_perro(perro1)
    sistema.cargar_perro(perro2)
    sistema.cargar_perro(perro3)

    # uso un usuario adoptante para probar el sistema
    isa = Adoptante("Isabella", "12345678", "isa@mail.com")
    isa.registrarse("Sánchez", "1144440000")
    isa.actualizar_preferencias(raza="Labrador", edad=3, tamaño="grande")

    sistema.registrar_usuario(isa)

    # Mostramos todos los perritos disponibles
    print("Listado inicial:")
    sistema.mostrar_listados()

    # Sugerencias según preferencias
    print("\Sugerencias para:" sistema.registrar_usuario(isa))
    sugeridos = sistema.sugerir_perros(isa)
    for p in sugeridos:
        print(f"- {p.nombre}, {p.raza}, {p.tamaño}, {p.edad} años")

    print("Postulación y adopción:")
    sistema.postular_a_perro(isa, perro1)
    sistema.confirmar_adopcion(isa, perro1)

    print("Datos de Isabella:")
    isa.mostrar_datos_usuario()

    # Mostrar perros por estado
    print("Perros adoptados:")
    sistema.mostrar_listados("adoptado")
