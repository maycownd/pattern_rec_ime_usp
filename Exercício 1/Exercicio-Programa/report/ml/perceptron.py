import numpy as np


class PerceptronBatch:
    def __init__(self, random_state=0, eta=0.001):
        self.random_state = random_state
        self.eta = eta
        self.w = None
        self.b = None

    def __phi(self, z):
        return np.sign(z)

    def fit(self, x, y):
        """
        Fit method for Perceptron Batch: https://www.cis.upenn.edu/~cis519/fall2014/lectures/04_LinearClassificationPerceptron.pdf
        """
        epochs = 0
        m, n = x.shape
        np.random.seed(self.random_state)
        self.w = np.random.rand(1, n)
        self.b = np.random.rand(1, 1)
        while True:
            z = np.dot(self.w, x.T) + self.b
            e = y.T - self.__phi(z)
            delta_w = np.dot(e, x)
            delta_b = np.sum(e)
            delta_w = delta_w / n
            delta_b = delta_b / n
            self.w = self.w + self.eta * delta_w
            self.b = self.b + self.eta * delta_b
            epochs = epochs + 1
            if sum(e.T) == 0:
                break

    def predict(self, x):
        """
        predict method to return the class
        :param x: numpy array
        :return: numpy array
        """
        return self.__phi(np.dot(self.w, x.T) + self.b)
