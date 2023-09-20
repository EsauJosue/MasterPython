#Programa que compruebe si una variable esta vacia y si esta vacia llenarla con texto en minusculas y mostrarla en mayusculas

texto = " "

if len(texto.strip()) <= 0: #si es vacio
    texto = 'hola como estas'
    print(texto.upper())
else:
    print(f"La variable contiene este contenido {texto}")