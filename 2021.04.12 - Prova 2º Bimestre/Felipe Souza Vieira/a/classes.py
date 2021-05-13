# Contém partes do sw Financial Management e dos trabalhos dos
# profª Divani e Marcus Aurelius


# senhaComum = []
senhaPrioritaria = []
#  Menus

def cabecalho():
    print("-" * 39)
    print("|", " " * 10, " ATENDIMENTO ", " " * 10, '|')
    print("-" * 39)

def menuUsuario():
    opcao = None
    print("\nEscolha um Atendimento:\n")
    print(" --> 1: Atendimento Comum")
    print(" --> 2: Atendimento Prioritário")
    # print(" --- 3: Consultar Posição na Fila")
    # print(" --- 4: Cancelar Atendimento")
    print("_" * 39,'\n')

def telaUsuario():
    from limpa_tela import limpa
    limpa()
    cabecalho()
    menuUsuario()

def menuAtendente():
    print("\Atendimento:\n")
    # print("Próximas senhas: {}".format(senha))
    print(" --- 1: Chamar o próximo da fila")
    # print(" --- 2: ")
    # print(" --- 3: ")
    # print(" --- 4: ")
    print("_" * 39,'\n')

def telaAtendente():
    from limpa_tela import limpa
    limpa()
    cabecalho()
    menuAtendente()

# Métodos dos programas



# Criação da Fila de senhas
# class Senha:
# 	def __init__(self):
# 		self.senha = []




# def consultaPosicaoFila():
    # print()




    # opcao = int(input("-> "))
    #     if opcao == 1:
    #       emiteSenhaComum()
    #       mostraSenha()
    #       vezNaFila

    #       x = int(input(" Informe o valor -> "))
    #       arv.inserir(x)
    #     elif opcao == 2:
    #       x = int(input(" Informe o valor -> "))
    #       if arv.remover(x) == False:
    #            print(" Valor nao encontrado!")
    #     elif opcao == 3:
    #       x = int(input(" Informe o valor -> "))
    #       if arv.buscar(x) != None:
    #            print(" Valor Encontrado")
    #       else:
    #            print(" Valor nao encontrado!")	 
    #     elif opcao == 4:
    #       arv.caminhar()
    #     elif opcao == 5:
    #       break