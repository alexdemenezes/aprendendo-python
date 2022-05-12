# o que é um conjunto
# métodos de uniao
# metodos de interseccao
# metodos de diferenca
# metodos de diferenca simetrica
# remocao de duplicidade de listas utilizando conjunto
# nao tem como haver duplicidade de dados





conjunto = {1, 2, 3, 4,  4}
print(conjunto) # resultado = {1, 2, 3, 4}


# adicionar elementos a um conjunto
conjunto.add('valor') # elemento vai ser adicionado ao conjunto


# remover elementos de um conjunto
conjunto.discard('valor') # o elemento que passei em paramereo sera removido


# unir conjuntos = union()
conjuntoA = {1, 2, 3, 4, 5}
conjuntoB = {5, 6, 7, 8}

conjunto_uniao = conjuntoA.union(conjuntoB)

print(conjuntoA) # resultado == {1, 2, 3, 4, 5, 6, 7, 8} obs: ele retira a duplicidade



# pegar interseccao = intersection()
conjunto_interseccao = conjuntoA.intersection(conjuntoB)
print(conjunto_interseccao) # resultado = {5} 


# pegar diferenca entre conjuntos = difference()
conjunto_diferenca = conjuntoA.difference(conjuntoB) # vai pegar numeros que só tem no conjunto a
conjunto_diferencaB = conjuntoB.difference(conjuntoA) # vai pegar numeros que só tem no conjunto b


#  diferenca simetrica = pega os valores que sao individuais de cada um e soma: symmetric_difference()
conjunto_diff_simetrica = conjuntoA.symmetric_difference(conjuntoB)
print(conjunto_diff_simetrica) # resutado {1, 2, 3, 4, 6, 7, 8} obs: nao pega o 5 pois o valor exxiste nos dois



# como saber se um conjunto está contido em outro = issubset()
conjunto_a = {1, 2, 3, }
conjunto_b = { 1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b) 
print(conjunto_subset) # resultado = true    obs: o conjunto_a  está contido no conjunto b.


conjunto_subset2 = conjunto_b.issubset(conjunto_a) # resultado = false    obs: o conjunto_b  nao está  contido no conjunto a.


# verificar se o conjunto tem um outro contido =  issuperset()
conjunto_superset = conjunto_b.issuperset(conjunto_a) 
print(conjunto_superset) # retorna true pois o conjunto b tem o conjunto a contido


# retirar duplicidade de lista utilizando conjunto

lista = [1, 2, 3, 3]

conjunto_lista = set(lista) # converto para conjunto

lista_ = list(conjunto_lista) # retorno para lista ejá estará sem a duplicidade