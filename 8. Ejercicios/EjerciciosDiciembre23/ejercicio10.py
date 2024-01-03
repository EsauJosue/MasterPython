"""
En este ejercicio el usuario va a ingresar la calificación de 15 alumnos, y al final va a contabilizar el programa cuantos alumnos aprobaron y cuantos alumnos pasaron

"""

alumno = 0
reprobados = 0
aprobados = 0

for alumno in range(1,15):
    calificacion = int(input("Ingrese la calificación del alumno: "))

    if calificacion >=0 and calificacion <= 10:
        if calificacion >= 6:
            aprobados = aprobados +1
        elif calificacion < 6:
            reprobados = reprobados +1

    else:
        print("Debe elegir una calificación entre 1 y 10")

print(f"La cantidad de reprobados son: {reprobados}")
print(f"La cantidad de aprobados son: {aprobados}")
         
