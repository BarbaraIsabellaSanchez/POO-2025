from django.db import models

ESTADOS = [
    ('disponible', 'Disponible'),
    ('reservado', 'Reservado'),
    ('adoptado', 'Adoptado'),
]

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=50)
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    temperamento = models.CharField(max_length=100)

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in dict(ESTADOS):
            self.estado = nuevo_estado
            self.save()

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    preferencias_raza = models.CharField(max_length=100, null=True, blank=True)
    preferencias_edad = models.IntegerField(null=True, blank=True)
    preferencias_tamaño = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre
