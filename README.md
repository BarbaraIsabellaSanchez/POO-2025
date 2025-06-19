# POO-2025
Sistema de Adopción de Perros
 
Este sistema permite gestionar una base de datos de perros en adopción, usuarios adoptantes, y facilitar el proceso de adopción a través de un entorno web usando Django.

Objetivo:
Aplicar los principios de la Programación Orientada a Objetos para construir un sistema funcional y realista.

Tecnologías:
- Python
- Django
- HTML
- GitHub Codespaces

Funcionalidades:
- Modelo `Perro` con atributos como nombre, raza, estado, vacunación, etc.
- Modelo `UsuarioAdoptante` con preferencias de adopción.
- Carga de datos desde el panel de administración (`/admin`).
- Visualización web de los perros disponibles en `/perros/`.
- Redirección automática desde `/` a `/perros/`.

Instrucciones para correr el proyecto

1. Clonar el repositorio o abrirlo en GitHub Codespaces.
2. Instalar dependencias:
   ```bash
   pip install django
