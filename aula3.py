a = int(input('Primeiro valor:'))
b = int(input('segundo valor: '))
c = int(print('terceiro valor: '))



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


# if/else e and
# else if === elif
if a > b and a > c:
    print('o maior número é {}'.format(a)) 
elif b > a and b > c: 
    print('o maior número é {}'.format(b))
else: 
    print('o maior numero é {}'.format(c))


d = int(input('entre com um valor: '))
resto = d % 2
if resto == 0: 
    print('número é par')
else: 
    print('número é impar')



resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print('foi digitado um número par')
else: 
    print('nenhum número par foi digitado')


if resto_a == 0 or not resto_b > 0:
    print('foi digitado um número par')
else: 
    print('nenhum número par foi digitado')



# pequeno sistema de notas

b1 = int(input('nota primeiro Bimestre: '))
b2 = int(input('nota segundo Bimestre: '))
b3 = int(input('nota terceiro Bimestre: '))
b4 = int(input('nota quarto Bimestre: '))

media = (b1 + b2 + b3 + b4) / 4

if b1 <= 10 and b2 <= 10 and b3 <= 10 and b4 <= 10:
    print('média: {}'.format(media))
else: 
    print('foi informado alguma nota errada')



# alterado dpara ser feito umna verificaçao logo apos a digitacao
b1 = int(input('nota primeiro Bimestre: '))
if b1 > 10:
    b1 = int(input('Você digitou errado. Primeiro bimestre: '))
b2 = int(input('nota segundo Bimestre: '))
if b2 > 10:
    b2 = int(input('Você digitou errado. Primeiro bimestre: '))
b3 = int(input('nota terceiro Bimestre: '))
if b3 > 10:
    b3 = int(input('Você digitou errado. Primeiro bimestre: '))
b4 = int(input('nota quarto Bimestre: '))
if b4 > 10:
    b4 = int(input('Você digitou errado. Primeiro bimestre: '))