class IrisApplication:
	def __init__(self, dataset=None, filepath=None, should_exit=False):
		self.dataset = dataset
		self.filepath = filepath
		self.should_exit = should_exit


	def run_action(self):
		pass 

	def sort(self):
		print("================== ordenar ========================== ")
		print("(1) sepal width")
		print("(2) sepal length")
		print("(3) iris type")
		print("(0) cancel")
		nr = int(input("Escolha o criterio de ordenacao: "))

		if nr == 1:
			self.dataset.data = sorted(self.dataset.data, key = lambda iris: iris.sepal_width)
		elif nr == 2:
			self.dataset.data = sorted(self.dataset.data, key = lambda iris: iris.sepal_length)
		elif nr == 3:
			self.dataset.data = sorted(self.dataset.data, key = lambda iris: iris.type.id)

	def exit(self):
		self.should_exit = True