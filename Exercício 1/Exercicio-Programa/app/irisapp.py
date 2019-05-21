from app import IrisApplication
from dataset import Dataset
from ioiris import read_iris_dataset

"""
    Declarações das funções visíveis nesse programa.
"""
def print_menu():
    print(" ========================= Menu ============================= ")
    print("(1) carregar arquivo")
    print("(2) criar arquivo")
    print("(0) sair")

def read_option():
    return int(input("Entre com a opção: "))


def load_file():

    path = input("Entre com o caminho do arquivo:")
    dataset = read_iris_dataset(path)
    irisApp = IrisApplication(dataset=dataset, filepath=path)
    return irisApp

def new_file():
    filepath = input("Entre com o nome do caminho: ")
    return IrisApplication(dataset=Dataset(), filepath=filepath)

def exit():
    return IrisApplication(should_exit=True)

def get_app_from_options_menu():
    print_menu()

    option = read_option()
    if option == 1:
        return load_file()
    elif option == 2:
        return new_file()
    elif option == 0:
        return exit()
    else:
        print("Opção inválida! Tente novamente")
        get_app_from_options_menu()
    return exit()

""" 
    Aqui começa o código executado ao iniciar o programa no 
    prompt de comando
"""

print("========= Programa de Cadastro de Flores de Iris ===============")
app = get_app_from_options_menu()

while not app.should_exit:
    app.run_action()