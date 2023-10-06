class proporcionalidad:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def set_numeros(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def get_numeros(self):
        return self.num1, self.num2, self.num3, self.num4

    def son_proporcionales(self):
        if self.num1 * self.num4 == self.num2 * self.num3:
            return True
        else:
            return False