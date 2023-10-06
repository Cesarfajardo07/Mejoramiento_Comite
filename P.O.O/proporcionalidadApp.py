from Proporcionalidad import proporcionalidad

proporcion1 = proporcionalidad(2, 4, 3, 6)
print("¿Son proporcionales?", proporcion1.son_proporcionales())

proporcion1.set_numeros(15, 2, 20, 8)
print("¿Son proporcionales?", proporcion1.son_proporcionales())