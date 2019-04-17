from iris.dataset import Dataset
from iris.app import IrisApplication

"""
	Declarações das funções visíveis nesse programa.
"""
def print_menu():
	print(" ========================= Menu ============================= ")
	print("(1) carregar arquivo")
	print("(2) criar arquivo")
	print("(0) sair")

# TODO: Passo 2 - implemente aqui a função read_option

def load_file():
	# TODO: passo 6 - implemente essa função e retorne um IrisApplication com um 
	#       dataset preenchido.
	pass

def new_file():
	filepath = input("Entre com o nome do caminho: ")
	return IrisApplication(dataset=Dataset(), filepath=filepath)

def exit():
	return IrisApplication(should_exit=True)

def get_app_from_options_menu():
	print_menu()

	# TODO: passo 2 - chame aqui sua função read_option
	option = 0 # substituir essa linha pela chamada de read_option e atribua o resultado a variável option.

	# TODO: passo 3 - incluir as chamadas as funções load_file, new_file, exit
	return exit()

""" 
	Aqui começa o código executado ao iniciar o programa no 
	prompt de comando
"""

# TODO: Ex. Passo 1. Insira aqui o código para imprimir a mensagem.  
app = get_app_from_options_menu()

while not app.should_exit:
	app.run_action()