import clases as cl

persona = cl.Persona()
persona.setNombre("Josue")
persona.setApellidos("Martínez Carrasco")
persona.setAltura("1.70")
persona.setEdad("39")

print("La persona es: {} , sus apellidos son: {}, su altura es de: {} y su edad es de: {}".format(persona.getNombre(),persona.getApellidos(),persona.getAltura(),persona.getEdad()))

informatico = cl.Informatico()
informatico.setNombre("Esau")
informatico.setAltura("180 cm")
informatico.setEdad("39 años")
lenguajes = ["Python","Django","Git"]
informatico.aprender(lenguajes)

print(informatico.getNombre())
print(informatico.getLenguajes())

tecnico = cl.TecnicoRedes()
print(tecnico.auditoria())