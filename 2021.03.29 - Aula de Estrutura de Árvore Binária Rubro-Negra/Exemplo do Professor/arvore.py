# Exercício do aluno: Felipe Souza Vieira
# Árvores Binárias
# Fonte: https://www.youtube.com/watch?v=f5dU3xoE6ms ; https://youtu.be/dyLwOXBA3Ws
# Baseado no trabalho da Profª. Divani Barbosa Gavinier e Profª Marcus Aurelius
# 11/04/2021

import os
os.system('cls' if os.name == 'nt' else 'clear') # Identifica o sistema e limpa a tela

# Classe que constrói nós:
class Nó:
    def __init__(self, carga=None):           # Construtor de nós vazios/nulos
        self.carga = carga                    # Quando recebe um valor, guarda no objeto
        self.ramo_esquerdo = None             # Cria um ramo esquerdo vazio (nil)
        self.ramo_direito = None              # Cria um ramo direito vazio (nil)

#  Classe que maneja a árvore
class Árvore:
  # def __init__(self, raiz=None):
    def __init__(self):                       # Construtor de raízes cruas/vazias
        self.raiz = None
    
    def inserção(self, carga):                # Função que pendura nós na árvore
        if self.raiz == None:                   # Primeiro testa se já não existe uma raiz na árvore
            self.raiz = Nó(carga)               # Se não existir, instancia um novo nó-raiz e carrega ele
        else:                                   # Se existir, compara com o nó atual e decide se direita ou esquerda
            if carga < self.raiz:
                Nó.ramo_esquerdo = self.raiz  # Caso a carga seja menor que a raiz atual, pendura à esquerda
            elif carga > self.raiz:
                Nó.ramo_direito = self.raiz   # Caso a carga seja maior que a raiz atual, pendura à direita
            else:
                return                        # Árvores binárias não repetem cargas, então se a carga for igual à raiz atual, ignora-se

    def busca(self, chave):                   # Função de busca de um valor na árvore
        if self.raiz == None:                   # Ao encontrar uma raiz vazia, cancela a busca e retorna
            return None
        else

    def remoção(self, carga):                 # Função de remoção de uma carga da árvore
        if self.carga == folha:                                    # Caso 01: se for uma folha, simplesmente deletar o nó  
            Nó.carga = None                      # O nó é substituído por um Nil
        elif :                                  # Caso 02: se for um ramo solitário, um único nó filho toma seu lugar
            Nó.carga = Nó.seguinte               # O nó é substituído por seu nó filho
        elif :                                  # Caso 03: se for um ramo com irmão, um único nó filho será escolhido para tomar seu lugar
            Nó.carga = Nó.sucessor               # O menor nó filho à direita substitui seu pai
