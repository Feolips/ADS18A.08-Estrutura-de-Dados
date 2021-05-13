
# Profº Marcus Aurelius
# Slide 16/03/2021

# Usando Orientação a objetos
class Fila(object):
	def __init__(self):
		self.dados = []

	def insere(self, elemento):
		self.dados.append(elemento)

	def retira(self):
		return self.dados.pop(0)

	def vazia(self):
		return len(self.dados) == 0


# Nodo de uma estrutura duplamente encadeada.

class Nodo:
	def __init__(self, dado=0, proximo_nodo=None):
		self.dado = dado
		self.proximo = proximo_nodo
	def __repr__(self):
		return '%s -> %s' % (self.dado, self.proximo)

# Fila em estrutura encadeada
class Fila:
	def __init__(self):
		self.primeiro = None
		self.ultimo = None
	def __repr__(self):
		return "[" + str(self.primeiro) + "]"ados) == 0

"""Insere um elemento no final da fila."""
	def insere(self, novo_dado):

# Cria um novo nodo com o dado a ser armazenado.
		novo_nodo = Nodo(novo_dado)
		
# Insere em uma fila vazia.
		if self.primeiro == None:
			self.primeiro = novo_nodo
			self.ultimo = novo_nodo
		else:
		# Faz com que o novo nodo seja o último da fila.
			self.ultimo.proximo = novo_nodo
# Faz com que o último da fila referencie o novo nodo.
			self.ultimo = novo_nodo

"""Remove o último elemento da fila."""
	def remove(self):
		assert self.primeiro != None, "Impossível remover elemento de fila
vazia."
		self.primeiro = self.primeiro.proximo
		if self.primeiro == None:
			self.ultimo - None

# Cria uma fila vazia:
fila = Fila()
print("Fila vazia: ", fila)
# Insere elementos na fila.
for i in range(5):
	fila.insere(i)
	print("Insere o valor {0} final da fila: {1}".format(i, fila))
# Remove elementos da fila.
while fila.primeiro != None:
	fila.remove()
	print("Removendo elemento que está no começo da fila: ", fila)


