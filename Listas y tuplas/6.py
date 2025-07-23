asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobado = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if (nota >= 5):
        aprobado.append(asignatura)
for asignatura in aprobado:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))