#20. Comparar tres números y encontrar el mayor usando estructuras if-elif-else:

def encontrar_mayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    
reslutado=encontrar_mayor(7, 2, 3)
print(reslutado)