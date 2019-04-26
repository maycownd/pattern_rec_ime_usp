from dataset import Dataset, Iris


def clear_screen():
	print("\n"*100)

def read_iris_dataset(path):
    dataset = Dataset()
    with open(path, "r") as file:
        buffer = file.read().splitlines()
        header = buffer.pop(0)

        for line in buffer:
            width, length, id = line.split(";")
            print(width, length, id)
            id = int(id)
            iris = Iris(width, length, id)
            dataset.add(iris)

    return dataset


def write_iris_dataset(path, dataset):
	with open(path, "w") as file:
		file.write(dataset.csv_header()+"\n")
		for iris in dataset:
			file.write(str(iris.sepal_width)+";"+str(iris.sepal_length)+";"+str(iris.type.id)+"\n")