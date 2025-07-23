asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    score = input("¿Qué nota has sacado en " + asignatura + "?")
    notas.append(score)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])