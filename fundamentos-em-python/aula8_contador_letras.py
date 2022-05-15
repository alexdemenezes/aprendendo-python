# criando umn metodo que recebe uma lista de palavras
# e retorna uma lista com o tamanho de cada palavra

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)

    return contador


# evitar que o import rode o teste
if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista)) # teste
