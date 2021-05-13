# Exemplo do Profº Marcus
# Árvores Binárias
# 29/03/2021

# Classe que abriga o nó raiz de cada iteração:
class Tree:
    raiz = None

# Classe que abriga valor do nó e seus filhos:
class Node:
    valor = None                                            # carga do nó
    pe = None                                               # ponteiro esquerdo
    pd = None                                               # ponteiro direito

# Inicialização da árvore, pronta para ser preenchida:
minhaArvore = Tree()                                        # instancia a árvore

# Inicialização e carregamento do valor no nó:
valorObtido = int(input("Insira o valor: "))                # pede novo valor
meuNo = Node()                                              # instancia um novo nó
meuNo.valor = valorObtido                                   # guarda o valor dentro do nó

# Alocação dos nós em seus ramos:
if minhaArvore == None:                                     # se não houver raiz, inicialize uma
    minhaArvore.raiz = meuNo
else:
    if minhaArvore.raiz.valor > valorObtido:                # se houver raiz, compare com o valor do nó
        minhaArvore.raiz = minhaArvore.raiz.pe                  # caso seja menor, grave no ramo esquerdo
    else:                                                       # caso seja maior, grave no ramo direito
        minhaArvore.raiz = minhaArvore.raiz.pe                  

