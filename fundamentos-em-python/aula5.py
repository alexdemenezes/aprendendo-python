# em python array == list

lista = [1, 2, 3, 4, 5]
print(lista[0])

soma = 0
for x in lista:
    print(x)
    soma += x



#funcao sum() do python soma os items da lista, porem eles tem que ser do mesmo tipo

print(sum(lista))

# funcao max() retorna o maior item da listam 
print(max(lista))


# para pegar o menor valor min()
print(min(lista))


# verificar se tem um valor especifico na lista
if 1 in lista:
    print('existe o número 1 na lista!')
else: 
    print('o número 1 não está na lista!')


# multiplicar uma lista
lista_m = [1, 2]

nova_lista = lista_m * 2
# resultado = [1, 2, 1, 2]

# adicionar um item na lista
lista.append(6)

# retirar item na lista
lista.pop()
# retira o ultimo item da lista ou eu posso passar a posicao como parametro


#caso queira remover um item especifico.
# passo o item como parametro
lista.remove(1)


# ordenar uma lista
lista.sort()



# reverter a lista
lista.reverse()


# diferenca entre lista e tupla: a lista pode ser alterada, já os valores da tupla não.


#declarando uma tupla usando (valor1, valor2, etc...)
tupla = (1, 2, 3, 4)


# descobrir tamanho da lista ou tupla: len()
print(len(lista))
print(len(tupla))


# converter uma lista para tupla
tupla_lista = tupla(lista)
print(type(tupla_lista))


#converter tupla em lista
lista_tupla = list(tupla)
print(type(lista_tupla))