# Enunciado
print('6. Mais velha de 02 pessoas')

# Entrada de dados
pessoaA = str(input("Insira o nome da 1ª pessoa: "))
idadeA = int(input(f"Insira a idade de {pessoaA}: "))
pessoaB = str(input("Insira o nome da 2ª pessoa: "))
idadeB = int(input(f"Insira a idade de {pessoaB}: "))

# Execução
if idadeA > idadeB:
    pVelha = pessoaA
    idadeMaior = idadeA
if idadeA < idadeB:
    pVelha = pessoaB
    idadeMaior = idadeB
else:
    pVelha = 'qualquer uma das duas'
    idadeMaior = idadeA

# Retorno ao usuário
print('A pessoa mais velha é {}, com {:.0f} anos!'.format(pVelha, idadeMaior))
