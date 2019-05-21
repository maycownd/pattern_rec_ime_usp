from tabulate import tabulate

from dataset import Iris
from ioiris import write_iris_dataset


class IrisApplication:
    def __init__(self, dataset=None, filepath=None, should_exit=False):
        self.dataset = dataset
        self.filepath = filepath
        self.should_exit = should_exit


    def run_action(self):
        print("="*15, "MENU", "="*15)
        print("(1) criar registro")
        print("(2) visualizar banco de dados")
        print("(3) remover registro")
        print("(4) ordenar")
        print("(5) salvar banco de dados em arquivo")
        print("(0) sair")
        opcao = int(input("Entre com uma opção (0 a 5)"))
        if opcao == 1:
            width = float(input("Entre com o valor da largura da sépala: "))
            length = float(input("Entre com o valor do comprimento da sépala: "))
            type = int(input("Entre com o tipo da iris (0 - Versicolor, 1 - Setosa, 2 - Virginica)"))
            iris = Iris(width, length, type)
            self.dataset.add(iris)
        elif opcao == 2:
            print(tabulate(self.dataset, headers=["Sepal Width", "Sepal Length", "Type"]))
        elif opcao == 3:
            index = int(input("Entre com o valor da linha a ser removida (começando pelo 0)"))
            self.dataset.remove(index)
        elif opcao == 4:
            self.sort()
        elif opcao == 5:
            write_iris_dataset(self.filepath, self.dataset)
        elif opcao == 0:
            self.exit()
        else:
            print("Opção inválida")

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