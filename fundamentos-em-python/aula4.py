#laço for

# comando range vai pegar o numero de 0 até o valor que eu passar no parametro
# tenho a opcao de passar o numero que inicia e o que termina
for x in range(1, 100):
    print(x)


#  verificar se o numero digitado é um numero primo
a = int(input('entre com um número: '))
div = 0

for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print('número {} é primo!'.format(a))
else:
    print('número {} não é primo'.format(a))



# laço while
a = 0

while a <= 10: 
    print(a)
    a += 1


nota = int(print('Entre com uma nota: '))

while nota > 10:
    nota = int(print('Nota inválida. Entre com a nota correta: '))

