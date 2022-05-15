# lambda == funcao anonima

# | nome da funcao: 'contador_letras'
# | declaro lambda: 'lambda'
# | declaro o que vai receber: 'lista'
# | declaro o que vai retornar: [len(x) for x in lista]

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato']

contador_letras(lista_animais)

# OBSERVACAO: LAMBDA so e eficiente para coisas que 
# conseguimos resolver com apenas uma linha

# lambda de uma soma
soma = lambda a, b: a + b


# dicionario de lambdas
# calculadora
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'mltiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora)) # dicionario 'dict'
soma = calculadora['soma'] # acessando o valor soma que e uma funcao anonima

print(soma(10, 5))