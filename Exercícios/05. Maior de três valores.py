print('5. Maior de três valores')
# Entrada de dados
v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
v3 = float(input('Insira o terceiro valor: '))

# Estrutura de decisão
if v1 > v2 and v1 > v3:
    maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

# Resposta ao usuário
print('O maior valor é {:.0f}'.format(maior))
