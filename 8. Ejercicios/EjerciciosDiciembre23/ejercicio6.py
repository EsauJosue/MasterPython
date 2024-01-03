"""
Mostrar todas las tablas de multiplicar

"""

for tabla in range(0,11):
    print(f"**Tabla del {tabla}**")
    for numero in range(0,11):
        print(f"{tabla} x {numero} = {tabla*numero}")