

# Programa Principal:
##############################################################
def main():
    # senhaComum = []
    senhaPrioritaria = []
    limpa()
    print(" 1. Atendente\n", "2. Usuário")
    opcao = None
    opcao = int(input("Atendente ou Usuário: "))
    if opcao == 1:
        programaAtendente()
    elif opcao == 2:
        programaUsuario()
    else:
        main()

# Programa Atendente:
##############################################################
def programaAtendente():
    telaAtendente()
    opcao = None
    opcao = int(input("--> "))
    if opcao == 1:
        chamaProximo()
        input("Enter para continuar")
    elif opcao == 2:
        telaAtendente()
        # todaFila()
    elif opcao == 3:
        main()
    else:
        programaAtendente()

def chamaProximo():
    if senhaPrioritaria != None:
        print("Chamando {}".format(senhaPrioritaria.pop(0)))
    else:
        print("Chamando {}".format(senhaComum.pop(0)))


# Programa Usuário:
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
        main()
    else:
        programaUsuario()
    # else:
    #     telaUsuario()
    #     print(" Não existe opção {}, [ENTER] para tentar novamente:".format(opcao))
    #     input()
    #     telaUsuario()


    # Entrada na fila, mostrando posição ao usuário


# Abre as filas e inicia o programa
#################################################
senhaComum = []
main()


# Atender o próximo da fila
# Mostrar fila inteira
# Tentar colocar na vertical
    # for i in "senhaPrioritaria":
    #     print(i"º", senhaPrioritaria(i))
# def todaFila():
#     print(senhaPrioritaria, end="")
#     print(senhaComum)



#   Chama Programa
#################################################

# senhaComum = []
# senhaPrioritaria = []
# ordemAtendimento = []