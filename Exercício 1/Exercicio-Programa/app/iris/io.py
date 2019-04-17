# TODO: Passo 5.1: importe as classes Dataset, IrisVersicolor, IrisSetosa e Iris 
#       do modulor iris.dataset
from iris.dataset import Dataset, IrisVersicolor, IrisSetosa
import os

def clear_screen():
	print("\n"*100)

# TODO: Passo 5.2: escreva a função read_iris_dataset(path):

def write_iris_dataset(path, dataset):
	with open(path, "w") as file:
		file.write(dataset.csv_header()+"\n")
		for iris in dataset:
			file.write(str(iris.sepal_width)+";"+str(iris.sepal_length)+";"+str(iris.type.id)+"\n")