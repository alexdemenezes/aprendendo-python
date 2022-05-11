# valor do input sendo convertido para inteiro
a = int(input('entre com o primeiro valor: '))
b = int(input('entre com o segundo valor: '))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)


# funcao type() para saber o tipo de alguma variavel
print(type(soma))

# converter inteiro para string
soma = str(soma)
print(soma)


# int sendo convertido para string para ser concatenado 
print('soma: ' + str(soma))

# arredondar numero float - retirar as casas decimais
print(int(divisao))


# adicionar variavel dentro da string 
print('soma: {}'.format(soma))
print('soma: {}, subtracao: {}'.format(soma, subtracao))


# imprimir pulando linha
print('soma: {} \nSubtração: {}'.format(soma, subtracao))
