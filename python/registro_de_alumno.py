# Registro de alumno

class Estudiante():
    def __init__(self, nombre, edad, institucion_educativa ,especialidad):
        self.nombre = nombre
        self.edad = edad
        self.institucion_educativa = institucion_educativa
        self.especialidad = especialidad

    def estudiar(self):
        print(f"El alumno {self.nombre} es estudiante de {self.institucion_educativa}")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
institucion_educativa = input("Ingresa tu institución educativa: ")
especialidad = input("Ingresa tu especialidad: ")

alumno1 = Estudiante(nombre, edad, institucion_educativa, especialidad)

def imprimir_alumno():
    print("\n")
    print("------- Registro de alumno(a) exitosos -------")
    print("\n")
    print(f"Nombre: {alumno1.nombre}")
    print(f"Edad: {alumno1.edad}")
    print(f"IE: {alumno1.institucion_educativa}")
    print(F"Grado: {alumno1.especialidad}")
    alumno1.estudiar()
    print("\n")

imprimir_alumno()

        
    