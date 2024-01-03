# No se pueden declarar variables con guion medio
# mi-texto = "Hola"
#Para colocar comillas dentro de un texto 
#Las diagonales invertidas son para escapar caracteres
mi_texto1 = "Hola \"Josué\" "
mi_texto2 = "en \"Python\" "

texto_unido = mi_texto1 + " " + mi_texto2
print(texto_unido)

texto_unido = mi_texto1 + " \n" + mi_texto2
print(texto_unido)  

texto_unido = mi_texto1 + " \t" + mi_texto2
print(texto_unido)

texto_unido = mi_texto1 + " \r" + mi_texto2
print(texto_unido)

texto_unido = mi_texto1 + " \r\n" + mi_texto2
print(texto_unido)

