print('14. Tipo de triângulo')

# Entrada de dados
hipotenusa = float(input('Insira em centímetros o valor da maior dimensão: '))
catetoA = float(input('Insira em centímetros o valor da dimensão intermediária: '))
catetoB = float(input('Insira em centímetros o valor da menor dimensão: '))

# Processamento de dados
if hipotenusa == catetoA and hipotenusa == catetoB:
    tipoTriangulo: str = 'equilátero'
if catetoA == catetoB:
    tipoTriangulo: str = 'isósceles'
if hipotenusa != catetoA and catetoB != hipotenusa:
    tipoTriangulo: str = 'escaleno'

# Retorno ao usuário
print(f'Os valores de {hipotenusa:.0f}cm, {catetoA:.0f}cm e {catetoB:.0f}cm formam um triângulo {tipoTriangulo}.')
