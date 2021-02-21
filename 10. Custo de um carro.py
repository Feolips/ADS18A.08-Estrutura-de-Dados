print('10. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem')
# do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
# distribuidor seja de 28% e os impostos de 45%, escreva um programa que leia o custo de
# fábrica de um carro e escreva o custo ao consumidor.

# Entrada de dados
print('O custo final do produto ao valor de fabricação acrescido a 28% de custos de distribuição mais 45% de impostos.')
vInicial = float(input('Insira o valor de fábrica do produto: '))

# Processamento dos dados
vDistribuicao = vInicial * 0.28  # O valor aqui poderia ser integrado ao montante, porém é mais conveniente separar.
vImpostos = (vInicial + vDistribuicao) * 0.45  # Aqui considera-se que os impostos incidem tanto sobre o produto quanto sobre a distribuição.
vTotal = vInicial + vDistribuicao + vImpostos  # Custo total ao consumidor

# Retorno ao usuário
print(f'O custo de produção é de R${vInicial:.2f}.')
print(f'O custo de distribuição é de R${vDistribuicao:.2f}')
print(f'O custo dos impostos é de R${vImpostos:.2f}')
print(f'O custo total do produto é de R${vTotal:.2f}')