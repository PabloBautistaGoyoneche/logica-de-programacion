# Un profesor necesita contabilizar cuantos alumnos aprueban y cuantos desaprueban.
# Ingresa su nombre
# Ingresa el número de alumnos
# Ingresa solo las notas según el número de alumnos
# Al final se imprime un resumen donde se ve cuantos alumnos aprueban y cuantos desaprueban.

profesor = str(input("Profesor, ingrese su nombre: "))
alumnos = int(input("Ingrese su numero de alumnos: "))

contador = 1
aprobados = 0
desaprobados = 0

while contador <= alumnos:
    calificacion = int(input(f"Ingresa la nota del alumno {contador}: "))
    
    if calificacion <= 10:
        desaprobados += 1
    else:
        aprobados += 1
    contador += 1

print(f"######### PROFESOR {profesor} ######### ")
print(f"El total de alumnos es: {alumnos}")
print("-----------------------------------")
print(f"Los desaprobados son {desaprobados}")
print(f"Los aprobados son {aprobados}")
    
