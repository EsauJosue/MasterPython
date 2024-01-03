'''
Programa que compruebe si una variable está vacia, y si está vacía, rellenarla con texto en minusculas y mostrarlo en mayusculas

'''

texto = "mi nombre es esau"

if len(texto.strip()) <= 0:
    texto = "hola soy un texto"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")
