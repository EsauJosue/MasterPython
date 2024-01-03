"""
Crear una lista con el contenido de esta tabla:

ACCION AVENTURA DEPORTES
GTA     ASSINS  FIFA21
COD     CRASH   PRO 21
PUGB    Prince of Persia    MOTO GP 21

Mostrar esta información ordenada

"""

tabla = [
    {
        "categoria": "Acción",
        "juegos" : ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "Aventura",
        "juegos" : ["ASSINS", "CRASH", "Prince of Persia"]
    },
      {
        "categoria": "Deportes",
        "juegos" : ["FIFA23", "PRO 21", "MOTO GP 21"]
    }
]
for categoria in tabla:
    print(f"---------------{categoria['categoria']}--------")
    for juego in categoria['juegos']:
        print(f"Juego: {juego}")
