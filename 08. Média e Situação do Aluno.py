print('8. Média e Situação do Aluno')
# Recebe o nome de um aluno, suas quatro notas, calcula e exibe
# Média final + Situação (Aprovado/Recuperação/Reprovado).
# Entrada de dados
nome = str(input('Insira o nome do aluno: '))
nota1 = float(input('Insira a 1ª nota: '))
nota2 = float(input('Insira a 2ª nota: '))
nota3 = float(input('Insira a 3ª nota: '))
nota4 = float(input('Insira a 4ª nota: '))
# Processamento dos dados
media = (nota1+nota2+nota3+nota4)/4
# Retorno ao usuário
print("Média: {:.2f}".format(media))
if media>=5:
    print('Aprovado! 😃')
if media<5:
    if media>=4:
        print('Recuperação. 🧐')
if media<4:
    print('Reprovado! 🤬')
