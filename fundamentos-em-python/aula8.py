# essa linha roda qunado eu importo esse arquivo
print('caso eu import esse arquivo essa linha sera executada')

# caso eu queira colocar codigos que 
# nao rodem quando importar esse arquivo
if __name__ == '__main__':
    print('roda quando esse arquivo e executado')


# importar so o que eu necessito de um modulo
# importei a classe Televisao do arquivo aula7_televisao
from aula7_televisao import Televisao

televisao = Televisao() # instancia da classe
print(televisao.ligada)# resultado False
televisao.power() # utilizando funcao da classe
print(televisao.ligada) # resultado True



# interagindo com a classe calculadora
from aula7_calculadora1 import Calculadora
calculadora = Calculadora(5, 10)
print(calculadora.soma)


# interagindo com contador de letras
from aula8_contador_letras import contador_letras

lista = ['cavalo', 'zebra', 'pato']
contador_letras(lista) # resultado [6, 5, 4]



