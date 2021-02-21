print('9. Idade atual de uma pessoa')
# Lê nome e data de nascimento (dia, mês e ano) de uma pessoa e retorna a idade atual.
# Entrada de dados:
nome = str(input('Insira o nome: '))
print('Data de nascimento: ')
anoNasc = int(input('Insira o ano (4 dígitos): '))
mesNasc = int(input('Insira o mês (1-12): '))
diaNasc = int(input('Insira o dia (1-31): '))
# Processamento dos dados
# (consultado em: https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python)
from datetime import date

dataHoje = date.today()  # Captura a data no formato ANSI
diaHoje = dataHoje.day  # Captura o dia atual
mesHoje = dataHoje.month  # Captura o mês atual
anoHoje = dataHoje.year  # Captura o ano atual

qtdeAno = anoHoje - anoNasc  # Contagem simples de diferença de anos
qtdeMes = mesHoje - mesNasc  # Contagem simples de diferença de meses
qtdeDia = diaHoje - diaNasc  # Contagem simples de diferença de dias

if mesNasc == mesHoje:  # Caso o aniversário ocorra no futuro e ainda esse mês, o mês incompleto deve ser subtraído.
    if diaHoje < diaNasc:
        qtdeMes = qtdeMes - 1
if mesHoje < mesNasc:  # Caso o aniversário ocorra no futuro e ainda esse ano, o ano incompleto deve ser subtraído.
    qtdeAno = qtdeAno - 1

# Retorno ao usuário
print("{}, nascido(a) em {:.0f}/{:.0f}/{:.0f}, tem hoje {:.1f} anos, {:.1f} meses e {:.1f} dias.".format(nome, diaNasc, mesNasc, anoNasc, qtdeAno, qtdeMes, qtdeDia))
