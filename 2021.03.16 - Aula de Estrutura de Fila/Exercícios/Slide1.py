
# Profº Marcus Aurelius
# Slide 16/03/2021


# Cria um vetor:
fila = []
# Cabeçalho: 
print("Informe os valores da Fila")
print()

# Preenche a fila
# for cont in range(7):
for cont in range(3):
	fila.append(str(input('Informe o valor ' + str(cont + 1) + ' para a fila: ')))
print(fila)

# fila.insert(2, 3)
print(fila)


# Escoa a fila
print()
print("Removendo os valores da Fila:")
print(fila)

print("")
while len(fila) > 0:
	print("chamando: ",fila.pop(0))
	print()
	# print(fila)

# FINALIZANDO O PROGRAMA
print("Fim...")
