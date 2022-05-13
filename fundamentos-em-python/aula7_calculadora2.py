# funcao calculadora sem receber valores no construtor e com  os metodos esperando parametros
class Calculadora:
    def __init__(self): #funcao igual ao constructor do js
        pass # o __init__ nao pode ser vazio, quando nao for utilizar eu coloco o pass ou retiro o metodo init
      
    def soma(self, a, b):
        return a + b


    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b




calculadora = Calculadora()
print(calculadora.soma(1, 2)) # resultado 3