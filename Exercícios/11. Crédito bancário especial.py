print('11. Crédito bancário de acordo com o saldo médio anual do cliente')

# Entrada de dados
saldoMedio = float(input('Insira o saldo médio no ultimo ano, em Reais: '))

# Processamento de dados
if 200 < saldoMedio <= 400:
    credito = saldoMedio * 0.2
if 400 < saldoMedio <= 600:
    credito = saldoMedio * 0.3
if saldoMedio > 600:
    credito = saldoMedio * 0.4
else:
    print('Infelizmente você não tem cacife para ganhar crédito extra.')
    credito = 0
# Resposta ao usuário
print('Você recebeu R${:.2f} de crédito extra!'.format(credito))