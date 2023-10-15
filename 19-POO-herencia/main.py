import clases

persona1 = clases.Persona()
persona1.setNombre("Josué")
persona1.setApellidos("Martinez")
persona1.setAltura("1.70")
persona1.setEdad("39 años")

print(f"La persona es: {persona1.getNombre()} {persona1.getApellidos()}")
print(persona1.hablar())

informatico = clases.Informatico()
informatico.setNombre("Esaú")
informatico.setApellidos("Carrasco")
informatico.setAltura("1.85")
informatico.setEdad("43 años")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"Su experiencia es: {informatico.getLenguajes()}")


TecnicoRedes = clases.tecnicoRedes()
TecnicoRedes.setNombre("Zoe")
print(f"El tecnico en Redes es: {TecnicoRedes.getNombre()} y los lenguajes que domina son: {TecnicoRedes.getLenguajes()}")


