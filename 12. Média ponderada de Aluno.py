print('12. Média ponderada do Aluno')
# Escrever um programa que receba três notas e calcule a média ponderada desse aluno,
# considerando que: a primeira nota tem peso 2,5; a segunda nota tem peso 3,5; e a terceira
# nota tem peso 4. Exibir as três notas e a média calculada.

peso1 = 2.5
peso2 = 3.5
peso3 = 4

# Entrada de dados
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))

# Processamento de dados
media = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/(peso1+peso2+peso3)

# Retorno ao usuário
print(' NOTA 1  NOTA 2  NOTA 3  MEDIA')
print(' {:.2f}   {:.2f}    {:.2f}    {:.2f}'.format(nota1, nota2, nota3, media))