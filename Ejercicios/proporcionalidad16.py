#16. Calcular el promedio de notas de un estudiante:

def promedio_notas(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

notas=[1.0, 4.0, 5.0, 5.0]
resultado=promedio_notas(notas)
print(resultado)