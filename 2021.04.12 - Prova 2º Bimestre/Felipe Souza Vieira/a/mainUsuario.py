# 2ª Prova de Estrutura de Dados
# Felipe Souza Vieira
# Gestão de senhas por ordem de chegada

from menus import telaUsuario, telaAtendente

senhaComum = []
senhaPrioritaria = []
ordemAtendimento = []

# Entrada na fila, mostrando posição ao usuário
def emiteSenhaComum():
    senhaComum.append(str(input('Insira seu nome completo: ')))
    print("Você é o {}º da fila.".format(len(senhaComum) + len(senhaPrioritaria)))
def emiteSenhaPrioritaria():
    senhaPrioritaria.append(str(input("Insira seu nome completo: "))
    print("Você é o {}º da fila.".format(len(senhaPrioritaria)))

# Atender o próximo da fila
def chamaProximo():
    if senhaPrioritaria != None:
        print("Chamando {}".format(senhaPrioritaria.pop(0)))
    else:
        print("Chamando {}".format(senhacomum.pop(0)))

# Mostrar fila inteira
# Tentar colocar na vertical
    # for i in "senhaPrioritaria":
    #     print(i"º", senhaPrioritaria(i))
def todaFila():
    print(senhaPrioritaria, end="")
    print(senhaComum)

# Início do programa Usuário:
def programaUsuario:
    telaUsuario()
    opcao = None
    opcao = int(input("--> "))
    if opcao == 1:
        telaUsuario()
        emiteSenhaComum()
        input('[ENTER] para continuar')
    elif opcao == 2:
        telaUsuario()
        emiteSenhaPrioritaria()
    # else:
    #     telaUsuario()
    #     print(" Não existe opção {}, [ENTER] para tentar novamente:".format(opcao))
    #     input()
    #     telaUsuario()

# Início do programa Atendente:
##############################################################
def programaAtendente:
    telaAtendente()
    opcao = None
    opcao = int(input("--> "))
    if opcao == 1:
        chamaProximo()
        input("Enter para continuar")
    if opcao == 2:
        telaAtendente()
        todaFila()

###################################################




# Início do programa:
##############################################################
print("1. Atendente\n", "2. Usuário")
opcao = input(int("Atendente ou Usuário: "))
if opcao == 1:


