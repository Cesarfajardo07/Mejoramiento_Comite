#10. Verificar si dos números son proporcionales:

def son_proporcionales(num1, num2, num3, num4):
    if num1 * num4 == num2 * num3:
        return True
    else:
        return False
    
resultado=son_proporcionales(2, 4, 3, 5)
print(resultado)