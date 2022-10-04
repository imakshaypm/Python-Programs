class MyComplexNumbers:
    def __init__(self, real = 0, imag = 0):
        self.real_part = real
        self.imag_part = imag

    def display(self):
        print("{0} + {1}j".format(self.real_part, self.imag_part))

cmp = MyComplexNumbers(60, 70)
cmp.new_atribute = 80
cmp.display()
print(cmp.real_part, cmp.imag_part, cmp.new_atribute)