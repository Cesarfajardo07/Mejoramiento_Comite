#2. Calcular la proporción entre dos números:

def proporcion(num1, num2):
    if num1 > num2:
        return num1 / num2
    elif num2 > num1:
        return num2 / num1
    else:
        return 1

resultado=proporcion(2, 30)
print (resultado)