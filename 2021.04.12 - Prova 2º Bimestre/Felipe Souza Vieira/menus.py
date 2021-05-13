# Felipe Souza Vieira e Adriano Silva Santos
# Contém partes do sw Financial Management

#  Menus

def cabecalho():
    print("-" * 39)
    print("|", " " * 10, " ATENDIMENTO ", " " * 10, '|')
    print("-" * 39)

def menuUsuario():
    print("\nEscolha um Atendimento:\n")
    print(" --> 1: Atendimento Comum")
    print(" --> 2: Atendimento Prioritário")
    # print(" --> 3: Consultar Nome  (em manutenção)")
    print("\n")
    print(" --> 0: Mudar Perfil")
    print("_" * 39,'\n')

def telaUsuario():
    from limpa_tela import limpa
    limpa()
    cabecalho()
    menuUsuario()

def menuAtendente():
    print("Atendimento:\n")
    # print("Próximas senhas: {}".format(senha))
    print(" --- 1: Chamar o próximo da fila")
    print(" --- 2: Mostrar fila")
    print("\n")
    print(" --- 0: Mudar Perfil")
    print("_" * 39,'\n')

def telaAtendente():
    from limpa_tela import limpa
    limpa()
    cabecalho()
    menuAtendente()