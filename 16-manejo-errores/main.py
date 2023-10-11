
try:
    nombre = input("Ingrese su nombre: ")
    if len(nombre) > 1:
        mi_nombre = f"El nombre es {nombre}"
    print(mi_nombre)
except:
    print("Ingrese bien su nombre")