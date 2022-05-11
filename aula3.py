a = int(input('Primeiro valor:'))
b = int(input('segundo valor: '))



# operador condicional if
if a > b:
    print('o maior número é {}'.format(a))


# o código dentro do if é definido pela identacao

# os dois prints só irao ocorrer caso a condicao seja verdadeira
if a > b:
    print('o maior número é {}'.format(a))
    print('final do programa')


# o segundo print ira ocorrer mesmo sem que a condicao do if seja verdadeira
if a > b:
    print('o maior número é {}'.format(a)) 
print('final do programa')