class Estudiante:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def imprimir_nombre(self):
        print("Nombre del estudiante:", self.nombre)