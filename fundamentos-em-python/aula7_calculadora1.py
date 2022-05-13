# contruindo metodos, funcoes e classes em python

# diferenca entre metodo e funcao: funcao é tudo que retorna um valor e o metodo nao retorna

# declarar uma funcao
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


print(soma(1, 2))
print(subtracao(3, 2))
print(multiplicacao(1, 2))
print(divisao(1, 2))


# declarar uma classe
class Calculadora:
    def __init__(self, num1, num2): #funcao igual ao constructor do js
        self.a = num1
        self.b = num2
      
    def soma(self):
        return self.a + self.b


    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a /self.b



# instanciando uma classe
calculadora = Calculadora(10, 2)

print(calculadora.a) # resultado = 10
print(calculadora.soma()) # resultado 12