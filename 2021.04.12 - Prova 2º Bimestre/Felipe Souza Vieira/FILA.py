# 2ª Prova de Estrutura de Dados
# Felipe Souza Vieira e Adriano Silva Santos
# Gestão de fila por ordem de chegada

from menus import telaUsuario, telaAtendente
from limpa_tela import limpa


# Programa Principal:
##############################################################
def main():
    limpa()
    print("\n    1. Atendente\n    2. Usuário")
    opcao = None
    opcao = int(input("--> "))
    if opcao == 1:
        programaAtendente()
    elif opcao == 2:
        programaUsuario()
    else:
        main()

# Programas do Atendente:
##############################################################
def programaAtendente():
    telaAtendente()
    opcao = None
    opcao = int(input("--> "))
    if opcao == 1:
        chamaProximo()
        input("Enter para continuar")
        programaAtendente()
    elif opcao == 2:
        telaAtendente()
        todaFila()
    elif opcao == 0:
        main()
    else:
        programaAtendente()

 # Chama o próximo usuário respeitando a fila de prioridade
def chamaProximo():
    if len(senhaPrioritaria) != 0:
        print("Chamando {}".format(senhaPrioritaria[0]))
        senhaPrioritaria.pop(0)
    elif len(senhaPrioritaria) == 0:
        print("Chamando {}".format(senhaComum[0]))
        senhaComum.pop(0)
    else:
        chamaProximo()

def todaFila():
    print("Prioritários em ordem: ",senhaPrioritaria, end=", ")
    print(" Demais em ordem: ",senhaComum)
    print()
    input('[ENTER para continuar]')
    programaAtendente()

# Programas do Usuário:
##############################################################
def programaUsuario():
    telaUsuario()
    opcao = None
    opcao = int(input("--> "))
    if opcao == 1:
        telaUsuario()
        emiteSenhaComum()
        input('[ENTER] para continuar')
        programaUsuario()
    elif opcao == 2:
        telaUsuario()
        emiteSenhaPrioritaria()
        input('[ENTER] para continuar')
        programaUsuario()
    elif opcao == 3:
        buscaPessoa()
    elif opcao == 0:
        main()
    else:
        telaUsuario()
        print(" Não existe opção {}, [ENTER] para tentar novamente:".format(opcao))
        input()
        programaUsuario()

# Busca alguém na fila
def buscaPessoa():
    telaUsuario()
    print()
    # Ainda tentando desenvolver essa joça
    # pessoa = str(input("Digite o nome: "))
    # max = (len(senhaComum) + len(senhaPrioritaria))
    # i = 0
    # while len(senhaComum) > 0:
    #     if pessoa == senhaComum[i]:
    #         print("{} é a {}ª pessoa da fila.".format(senhaComum[i], i))
    #     i += 1
    # while len(senhaPrioritaria) > 0:
    #     if pessoa == senhaPrioritaria[i]:
    #         print("{} é a {}ª pessoa da fila.".format(senhaPrioritaria[i], i))
    #     i += 1
    input("Opção em mautenção. [ENTER] para voltar")
    programaUsuario()


# Usuário entra na fila e vê quantas pessoas faltam
def emiteSenhaComum():
    senhaComum.append(str(input('Insira seu nome completo: ')))
    print("Você está em {}º na fila.".format((len(senhaComum) + len(senhaPrioritaria))), end="")
def emiteSenhaPrioritaria():
    senhaPrioritaria.append(str(input("Insira seu nome completo: ")))
    print("Você está em {}º na fila.".format((len(senhaPrioritaria))), end="")


#   Inicializa as Filas e o Programa
#################################################

senhaComum = []
senhaPrioritaria = []
main()