 #Crear una lista con el contenido de esta tabla

tabla = [
    {
        "categoria" : "accion",
        "juegos" : ["GTA", "Call of Duty", "Pugb"]
    },
    {
        "categoria" : "aventura",
        "juegos" : ["Assasins", "Crash Bandicoot", "Prince of Persia"]
    },
     {
        "categoria" : "deportes",
        "juegos" : ["FIFA 23", "PES23", "MOTO GP 23"]
    }

]
for categoria in tabla:
    print(f"---------{categoria['categoria']}----------")
    for juego in categoria["juegos"]:
        print(f"Juego: {juego}")
