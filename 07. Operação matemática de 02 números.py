# Enunciado
print('7. Operação matemática entre 02 números')

# Entrada do usuário
v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
print('Insira a operação matemática a executar (+, −, ×, ou ÷): ')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
op = int(input('Insira sua opção: '))

# Execução da Operação
if op == 1:
    res = v1 + v2
    sinal = str('+')
if op == 2:
    res = v1 - v2
    sinal = str('−')
if op == 3:
    res = v1 * v2
    sinal = str('×')
if op == 4:
    res = v1 / v2
    sinal = str('÷')
else:
    print('{:.0f} não é uma opção válida!'.format(op))
# Resposta ao usuário
print("Resultado da operação: {:.0f} {} {:.0f} = {:.0f}.".format(v1, sinal, v2,res))