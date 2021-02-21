# Enunciado
print('15. Raízes reais ou imaginárias')
# Escrever um programa para calcular o valor do discriminante de uma equação do segundo
# grau. Se o discriminante for menor que zero, exibir a mensagem “Raízes imaginárias”; caso
# contrário exibir a mensagem “Raízes reais”, seguida dos valores calculados das raízes.

# Entrada de dados
a = float(input(f"Insira o valor de a: "))
b = float(input(f"Insira o valor de b: "))
c = float(input(f"Insira o valor de c: "))

# Processamento de dados
discriminante = b ** 2 - 4 * (a * c)
if discriminante < 0:
    raizes: str = 'imaginárias'
    existemRaizes: str = 'não assumem'
    R1 = 0
    R2 = 0
else:
    raizes: str = 'reais'
    existemRaizes: str = 'assumem'
    from math import sqrt
    sqrtDiscriminante = math.sqrt(discriminante)
    R1 = float((b * (-1) + sqrtDiscriminante) / (2 * a))
    R2 = float((b * (-1) - sqrtDiscriminante) / (2 * a))

# Retorno ao usuário
print(f'As raízes são {raizes} e {existemRaizes} valores ({R1:.2f} e {R2:.2f}).')

