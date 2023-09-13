
contador = 1
reprobados = 0
aprobados = 0

for contador in range(1,16):
    cal = int(input("Dame la calificación del alumno {}: ".format(contador)))
    if cal >= 0 and cal <= 10: 
        if cal < 6:
            reprobados +=1
        else:   
            aprobados +=1
    else: 
        print("La calificación debe ser entre 1 y 10")

print("Los alumnos reprobados son: {}".format(reprobados))
print("Los alumnos aprobados son: {}".format(aprobados))          

