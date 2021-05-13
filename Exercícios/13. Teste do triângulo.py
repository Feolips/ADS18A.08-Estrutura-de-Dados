print('13. Teste do triângulo')

# Entrada de dados
hipotenusa = float(input('Insira em centímetros o valor da maior dimensão: '))
catetoA = float(input('Insira em centímetros o valor da dimensão intermediária: '))
catetoB = float(input('Insira em centímetros o valor da menor dimensão: '))

# Processamento de dados
somaCatetos = catetoA + catetoB

# Retorno ao usuário
if hipotenusa < somaCatetos:
    print(
        f'Os valores de {hipotenusa:.0f}cm, {catetoA:.0f}cm e {catetoB:.0f}cm formam um triângulo viável.')
else:
    print(
        f'Os valores de {hipotenusa:.0f}cm, {catetoA:.0f}cm e {catetoB:.0f}cm não formam um triângulo viável.'
    )