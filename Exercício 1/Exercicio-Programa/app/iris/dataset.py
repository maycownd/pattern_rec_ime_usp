# ==================== Iris Type ==================================
class IrisType:
	def __init__(self, id, name):
		self.id = id
		self.name = name

IrisVersicolor = IrisType(id=0, name="Iris-Versicolor")
IrisSetosa = IrisType(id=1, name="Iris-Setosa")


# TODO: Passo 4 - implemente a classe que representa uma flor de Iris aqui.
class Iris:
	def __init__(self, sepal_width, sepal_length, type):
		self.sepal_width = sepal_width
		self.sepal_length = sepal_length
		self.type = type

	def attr_to_list(self):
		return [self.sepal_width, self.sepal_length, self.type.name]

	def to_csv(self):
		return str(self.sepal_width, ";", self.sepal_length, ";", self.type.id)


# ============== Dataset ===============================================
class Dataset:
	def __init__(self):
		self.data = []

	def add(self, iris):
		self.data.append(iris)

	def get(self, index):
		return self.data[index]

	def set(self, index, iris):
		self.data[index] = iris

	def remove(self, index):
		del self.data[index]

	def __iter__(self):
		return iter(self.data)

	def to_list_header(self):
		return ["sepal width", "sepal length", "type"]

	def csv_header(self):
		return "sepal width;sepal length;type"