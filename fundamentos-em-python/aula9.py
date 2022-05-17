# Aprender a ler e escrever arquivos
# manipular informacoes dos arquivos
# Copiar e mover arquivos


# build in do python  'open' => cria arquivos, abre arquivos
# 'w'  > sobrepoe o que tem no arquivo
# 'a' > adiciona a escrita ao arquivo sem sobrepor
# 'r' > ler arquivo
# arquivo = open('teste.txt', 'a') # caso esse arquivo nao exista ele ira criar
# arquivo.write('\nMinha segunda escrita') # '\n' para excrever na outra linha
# arquivo.close() # fecha o arquivo que foi aberto

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w') # caso esse arquivo nao exista ele ira criar
    arquivo.write(texto) # '\n' para excrever na outra linha
    arquivo.close() # fecha o arquivo que foi aberto


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)



def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') # transformo em uma lista
    lista_media = []
    for x in aluno_nota: 
        lista_notas = x.split(',') # transformo o aluno e as notas em uma lista
        aluno = lista_notas[0]
        lista_notas.pop(0) # retira o primeiro elemento que e o nome do aluno
        media = lambda notas: sum([int(i) for i in notas]) / 4 # trasnformo ca elemento em numero e faco a logica da media
        lista_media.append({aluno:media(lista_notas)})
    return lista_media    



def copia_arquivo(nome_arquivo, destino):
    import shutil #  modulo do python para fazer copia
    shutil.copy(nome_arquivo, destino)
    

def move_arquivo(nome_arquivo, caminho):
    import shutil
    shutil.move(nome_arquivo, caminho)


if __name__ == '__main__':
    escrever_arquivo('Minha primeira linha\n')
    aluno = '\nRafael, 10, 10, 5, 5\n'
    atualizar_arquivo('nota.txt', aluno)
    ler_arquivo('teste.txt')
    copia_arquivo('nota.txt', './') 

