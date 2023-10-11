import os, shutil

# Crear carpeta

if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
else:
    print("El directorio ya existe")

# Borrar directorio

# os.rmdir("./micarpeta")

# Copiar directorio

# ruta_original = "./micarpeta"
# ruta_nueva = "./micarpeta_COPIADA"

# shutil.copytree(ruta_original,ruta_nueva)

# Ver contenido de una carpeta

print("Contenido de mi carpeta")
contenido = os.listdir("./micarpeta")

for elemento in contenido:
    print(elemento)