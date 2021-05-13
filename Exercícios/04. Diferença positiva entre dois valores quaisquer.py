# Enunciado
print('4. Diferença positiva entre dois valores quaisquer')

# Entrada de dados
v1 = float(input('Insira um valor: '))
v2 = float(input('Insira outro valor: '))

# Estrutura de decisão
if v1 >= v2:
    delta = float(v1-v2)
else:
    delta = float(v2-v1)

# Resposta ao usuário
print('A diferença entre {:.0f} e {:.0f} é {:.0f}.'.format(v1, v2, delta))
