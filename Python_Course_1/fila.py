class Fila:

	def __init__(self):
		self.fila = []
		self.len_fila = 0

	def push(self, e):
		self.fila.append(e)
		self.len_fila += 1

	def pop(self):
		if not self.empty():
			self.fila.pop(0)
			self.len_fila -= 1

	def empty(self):
		if self.len_fila == 0:
			return True
		else:
			return False

	def length(self):
		return self.len_fila

	def front(self):
		if not self.empty():
			return self.fila[0]
		else:
			return None

	
q = Fila()
q.push(1)
q.push(2)
q.push(3)
print(q.front())