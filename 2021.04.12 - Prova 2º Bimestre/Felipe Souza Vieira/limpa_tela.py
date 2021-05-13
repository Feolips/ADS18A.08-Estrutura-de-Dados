# Método limpar a tela em qualquer sistema Windows ou Unix
# Desenvolvido com base no exemplo:
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python

def limpa():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Depois de importar basta chamar o método
# limpa()