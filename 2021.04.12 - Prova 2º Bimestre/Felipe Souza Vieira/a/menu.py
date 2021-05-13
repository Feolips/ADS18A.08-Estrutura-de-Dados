# Contém partes do sw Financial Management e do trabalho da profª Divani


def cabecalho():
    print("#" * 58)
    print("#" * 17, " ATENDIMENTO ", "#" * 17)
    print("#" * 58)

def menu():
    while opcao != 5:
     print("***********************************")
     print("Escolha uma senha:")
     print(" --- 1: Atendimento Comum")
     print(" --- 2: Atendimento Prioritário")
     print(" --- 3: Cancelar Atendimento")
     print(" --- 4: Consultar fila")
     print(" --- 5: Sair do programa")
     print("***********************************")
     opcao = int(input("-> "))
     if opcao == 1:
          x = int(input(" Informe o valor -> "))
          arv.inserir(x)
     elif opcao == 2:
          x = int(input(" Informe o valor -> "))
          if arv.remover(x) == False:
               print(" Valor nao encontrado!")
     elif opcao == 3:
          x = int(input(" Informe o valor -> "))
          if arv.buscar(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")	 
     elif opcao == 4:
          arv.caminhar()
     elif opcao == 5:
          break