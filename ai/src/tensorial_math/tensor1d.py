import numpy as np


def sigmoid(x):
    return np.longdouble(1 / (1 + np.exp(-x)))


class Tensor1D:
    def __init__(self, content: [float]):
        self.content = content

    def reduce(self):
        reduced_string: str = ''

        for idx, value in enumerate(self.content):
            reduced_string += str(self.content[idx] * 10)

        reduced_value: np.longdouble = sigmoid(
            int(reduced_string) / 10 ** (len(reduced_string) + 1))

        return reduced_value
